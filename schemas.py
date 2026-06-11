from pydantic import BaseModel

class CarBase(BaseModel):
    brand: str
    model: str
    year: int
    price: float
    color: str

class CarCreate(CarBase):
    pass

class CarUpdate(CarBase):
    pass

class CarResponse(CarBase):
    id: int

    class Config:
        from_attributes = True
