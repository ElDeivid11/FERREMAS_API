from pydantic import BaseModel, EmailStr

class ContactoSchema(BaseModel):
    nombre: str
    correo: EmailStr
    asunto: str
    mensaje: str

    class Config:
        orm_mode = True
