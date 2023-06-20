from pydantic import BaseModel


class FruVeg(BaseModel):
    image: str
    title: str
    profileImage: str
    pictureDescription: str
    introduction: str
    article: str
    category: str
    author: str
    date: str
