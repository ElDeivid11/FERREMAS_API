from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.routes import productos, contacto, conversion  
from app.routes.contacto import router as contacto_router

from app.database.db import Base, engine  

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(productos.router)  
app.include_router(contacto.router) 
app.include_router(conversion.router, prefix="/api")  

app.include_router(contacto_router)

# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine) 

@app.get("/")
def root():
    return {"mensaje": "FERREMAS API funcionando"}
