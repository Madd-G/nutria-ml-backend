from fastapi import APIRouter
from fastapi import FastAPI, File, UploadFile
from PIL import Image
from io import BytesIO
import torch

route = APIRouter()


@route.post("/nutria/detect")
async def detect(file: UploadFile = File(...), model_name: str = 'last-s'):
    model = torch.hub.load('ultralytics/yolov5', 'custom', model_name)
    results = model(Image.open(BytesIO(await file.read())))
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
