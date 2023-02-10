from pydantic import BaseModel


class Car(BaseModel):
    id: int
    model: str
    make: str
    colour: str
    age: int
