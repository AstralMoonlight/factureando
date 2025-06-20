# app/crud/negocio.py

from sqlalchemy.orm import Session
from app.models.negocio import Negocio
from app.schemas.negocio import NegocioCreate, NegocioUpdate
from uuid import UUID

def crear_negocio(db: Session, negocio: NegocioCreate) -> Negocio:
    db_negocio = Negocio(**negocio.dict())
    db.add(db_negocio)
    db.commit()
    db.refresh(db_negocio)
    return db_negocio

def obtener_negocio(db: Session, negocio_id: UUID) -> Negocio | None:
    return db.query(Negocio).filter(Negocio.id == negocio_id).first()

def listar_negocios(db: Session):
    return db.query(Negocio).all()

def actualizar_negocio(db: Session, negocio_id: UUID, datos: NegocioUpdate) -> Negocio | None:
    negocio = obtener_negocio(db, negocio_id)
    if negocio:
        for key, value in datos.dict(exclude_unset=True).items():
            setattr(negocio, key, value)
        db.commit()
        db.refresh(negocio)
    return negocio

def eliminar_negocio(db: Session, negocio_id: UUID) -> bool:
    negocio = obtener_negocio(db, negocio_id)
    if negocio:
        db.delete(negocio)
        db.commit()
        return True
    return False
