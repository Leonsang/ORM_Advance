from sqlalchemy.orm import Session
from . import models

def get_producto(db: Session, producto_id: int):
    """
    Obtiene un producto por su ID.
    """
    return db.query(models.Producto).filter(models.Producto.id == producto_id).first()

def get_productos(db: Session, skip: int = 0, limit: int = 100):
    """
    Obtiene una lista de productos.
    """
    return db.query(models.Producto).offset(skip).limit(limit).all()

def create_producto(db: Session, producto_data: dict):
    """
    Crea un nuevo producto.
    """
    nuevo_producto = models.Producto(**producto_data)
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    return nuevo_producto

def update_producto(db: Session, producto_id: int, producto_data: dict):
    """
    Actualiza un producto existente.
    """
    producto = get_producto(db, producto_id)
    if producto:
        for key, value in producto_data.items():
            setattr(producto, key, value)
        db.commit()
        db.refresh(producto)
    return producto

def delete_producto(db: Session, producto_id: int):
    """
    Elimina un producto.
    """
    producto = get_producto(db, producto_id)
    if producto:
        db.delete(producto)
        db.commit()
    return producto
