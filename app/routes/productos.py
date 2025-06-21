from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.db import SessionLocal
from app.models.producto import Producto
from app.schemas.producto_schema import ProductoSchema

router = APIRouter(prefix="/productos", tags=["Productos"])

#  Función para obtener sesión de la DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#  GET /productos → Listar productos
@router.get("/", response_model=list[ProductoSchema])
def listar_productos(db: Session = Depends(get_db)):
    return db.query(Producto).all()

#  POST /productos → Crear nuevo producto
@router.post("/", response_model=ProductoSchema, status_code=status.HTTP_201_CREATED)
def crear_producto(producto: ProductoSchema, db: Session = Depends(get_db)):
    # Verifica si ya existe un producto con el mismo código
    existe = db.query(Producto).filter(Producto.codigo == producto.codigo).first()
    if existe:
        raise HTTPException(status_code=400, detail="El código ya está registrado")

    nuevo = Producto(**producto.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.get("/{codigo}", response_model=ProductoSchema)
def obtener_producto_por_codigo(codigo: str, db: Session = Depends(get_db)):
    producto = db.query(Producto).filter(Producto.codigo == codigo).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.put("/{codigo}", response_model=ProductoSchema)
def actualizar_producto(codigo: str, datos: ProductoSchema, db: Session = Depends(get_db)):
    producto = db.query(Producto).filter(Producto.codigo == codigo).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    for key, value in datos.dict().items():
        setattr(producto, key, value)

    db.commit()
    db.refresh(producto)
    return producto

@router.delete("/{codigo}", status_code=204)
def eliminar_producto(codigo: str, db: Session = Depends(get_db)):
    producto = db.query(Producto).filter(Producto.codigo == codigo).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    db.delete(producto)
    db.commit()
    return

