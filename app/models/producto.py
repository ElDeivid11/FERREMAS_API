from sqlalchemy import Column, String, Float, Integer
from app.database.db import Base

class Producto(Base):
    __tablename__ = "productos"
    codigo = Column(String, primary_key=True, index=True)
    marca = Column(String, nullable=False)
    nombre = Column(String, nullable=False)
    modelo = Column(String, nullable=False)
    stock = Column(Integer, nullable=False)
