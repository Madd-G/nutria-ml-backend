from pydantic import BaseModel


class FruVeg(BaseModel):
    name: str
    description: str
    category: str
    nutrients: str
    benefits: str
