from pydantic import BaseModel
from typing import List, Optional

class ProductoSchema(BaseModel):
    codigo: str
    marca: str
    nombre: str
    modelo: str
    stock: int

    class Config:
        orm_mode = True
