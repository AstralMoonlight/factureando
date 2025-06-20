# app/routes/negocio.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from app.schemas.negocio import NegocioCreate, NegocioOut, NegocioUpdate
from app.crud import negocio as crud
from app.database import get_db

router = APIRouter(prefix="/negocios", tags=["Negocios"])

@router.post("/", response_model=NegocioOut)
def crear_negocio(payload: NegocioCreate, db: Session = Depends(get_db)):
    return crud.crear_negocio(db, payload)

@router.get("/", response_model=list[NegocioOut])
def listar_negocios(db: Session = Depends(get_db)):
    return crud.listar_negocios(db)

@router.get("/{negocio_id}", response_model=NegocioOut)
def obtener_negocio(negocio_id: UUID, db: Session = Depends(get_db)):
    negocio = crud.obtener_negocio(db, negocio_id)
    if not negocio:
        raise HTTPException(status_code=404, detail="Negocio no encontrado")
    return negocio

@router.put("/{negocio_id}", response_model=NegocioOut)
def actualizar_negocio(negocio_id: UUID, payload: NegocioUpdate, db: Session = Depends(get_db)):
    negocio = crud.actualizar_negocio(db, negocio_id, payload)
    if not negocio:
        raise HTTPException(status_code=404, detail="Negocio no encontrado")
    return negocio

@router.delete("/{negocio_id}")
def eliminar_negocio(negocio_id: UUID, db: Session = Depends(get_db)):
    if not crud.eliminar_negocio(db, negocio_id):
        raise HTTPException(status_code=404, detail="Negocio no encontrado")
    return {"ok": True}
