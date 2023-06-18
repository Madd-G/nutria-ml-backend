from fastapi import APIRouter
from sqlalchemy.sql.sqltypes import String
from config.db import conn
from model.articles import article
from model.fru_veg_model import fruveg
from model.fruit_model import fruits
from model.vegetable_model import vegetables
from schemas.fru_veg import FruVeg
from schemas.fruit import Fruit
from schemas.vegetable import Vegetable
from fastapi import FastAPI, File, UploadFile
from PIL import Image
from io import BytesIO
import torch

# import time

route = APIRouter()


@route.get('/nutria/get-all')
def fetch_all():
    return {'data': conn.execute(fruveg.select()).fetchall()}


@route.get('/nutria/get-articles')
def fetch_all_article():
    return {'data': conn.execute(article.select()).fetchall()}


@route.get('/nutria/get-fruit')
def fetch_fruit():
    return {'data': conn.execute(fruveg.select().where(fruveg.c.category == 'Fruit')).fetchall()}


@route.get('/nutria/get-vegetable')
def fetch_vegetable():
    return {'data': conn.execute(fruveg.select().where(fruveg.c.category == 'Vegetable')).fetchall()}


@route.post('/nutria/create-fruit/')
def post_fruit(fruit: Fruit):
    return conn.execute(fruits.insert().values(name=fruit.name, category=fruit.category, description=fruit.description))


@route.post('/nutria/create-vegetable/')
def post_vegetable(vegetable: Vegetable):
    return conn.execute(
        vegetables.insert().values(name=vegetable.name, category=vegetable.category, description=vegetable.description))


@route.put('/nutria/update-fruit/{id}')
def update_fruit(id: int, fruit: Fruit):
    return conn.execute(
        fruits.update().values(name=fruit.name, category=fruit.category, description=fruit.description).where(
            fruits.c.id == id))


@route.put('/nutria/update-vegetable/{id}')
def update_vegetable(id: int, vegetable: Vegetable):
    return conn.execute(
        vegetables.update().values(name=vegetable.name, category=vegetable.category,
                                   description=vegetable.description).where(vegetables.c.id == id))


@route.get('/nutria/get-all/{name}')
def fetch_one(name: str):
    return conn.execute(fruveg.select().where(fruveg.c.name == name)).fetchall()


@route.delete('/nutria/delete-fruit/{id}')
def delete_fruit(id: int):
    # c = column
    return conn.execute(fruits.delete().where(fruits.c.id == id))


@route.delete('/nutria/delete-vegetable/{id}')
def delete_vegetable(id: int):
    # c = column
    return conn.execute(vegetables.delete().where(vegetables.c.id == id))


@route.post("/nutria/detect")
async def detect(file: UploadFile = File(...), model_name: str = 'last-s'):
    model = torch.hub.load('ultralytics/yolov5', 'custom', model_name)
    results = model(Image.open(BytesIO(await file.read())))
    # print('results: ' + str(results))
    json_results = results_to_json(results, model)
    json_results = json_results[0]
    return json_results


def results_to_json(results, model):
    result = [
        [
            {
                "class_label": str(int(pred[5])),
                "class_name": model.model.names[int(pred[5])],
                # "bbox": [int(x) for x in pred[:4].tolist()],
                "confidence": str(float(pred[4] * 100)),
            }
            for pred in result
        ]
        for result in results.xyxy
    ]

    return result
