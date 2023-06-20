from pydantic import BaseModel


class Fruit(BaseModel):
    name: str
    description: str
    category: str
    nutrients: str
    benefits: str
