# app/crud/sucursal.py

from sqlalchemy.orm import Session
from app.models.sucursal import Sucursal
from app.schemas.sucursal import SucursalCreate, SucursalUpdate
from uuid import UUID

def crear_sucursal(db: Session, sucursal: SucursalCreate) -> Sucursal:
    db_sucursal = Sucursal(**sucursal.dict())
    db.add(db_sucursal)
    db.commit()
    db.refresh(db_sucursal)
    return db_sucursal

def obtener_sucursal(db: Session, sucursal_id: UUID) -> Sucursal | None:
    return db.query(Sucursal).filter(Sucursal.id == sucursal_id).first()

def listar_sucursales_por_negocio(db: Session, negocio_id: UUID):
    return db.query(Sucursal).filter(Sucursal.negocio_id == negocio_id).all()

def actualizar_sucursal(db: Session, sucursal_id: UUID, datos: SucursalUpdate) -> Sucursal | None:
    sucursal = obtener_sucursal(db, sucursal_id)
    if sucursal:
        for key, value in datos.dict(exclude_unset=True).items():
            setattr(sucursal, key, value)
        db.commit()
        db.refresh(sucursal)
    return sucursal

def eliminar_sucursal(db: Session, sucursal_id: UUID) -> bool:
    sucursal = obtener_sucursal(db, sucursal_id)
    if sucursal:
        db.delete(sucursal)
        db.commit()
        return True
    return False
