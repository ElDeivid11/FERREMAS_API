from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
import smtplib
from email.mime.text import MIMEText

router = APIRouter(prefix="/contacto", tags=["Contacto"])

class ContactoSchema(BaseModel):
    nombre: str
    correo: EmailStr
    asunto: str
    mensaje: str

@router.post("/")
def enviar_contacto(contacto: ContactoSchema):
    try:
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        smtp_user = "ferremascasoprueba@gmail.com"        
        smtp_password = "aujd pmgy hyxm eogs"  

        # Crear mensaje
        msg = MIMEText(f"Nombre: {contacto.nombre}\nCorreo: {contacto.correo}\n\nMensaje:\n{contacto.mensaje}")
        msg["Subject"] = contacto.asunto
        msg["From"] = smtp_user
        msg["To"] = smtp_user  

        # Enviar correo
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, [smtp_user], msg.as_string())
        server.quit()

        return {"mensaje": "Correo enviado con éxito"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al enviar correo: {str(e)}")
