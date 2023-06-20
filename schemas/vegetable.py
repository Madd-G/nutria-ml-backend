from pydantic import BaseModel


class Vegetable(BaseModel):
    name: str
    description: str
    category: str
    nutrients: str
    benefits: str
