# app/routes/sucursal.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from app.schemas.sucursal import SucursalCreate, SucursalUpdate, SucursalOut
from app.crud import sucursal as crud
from app.database import get_db

router = APIRouter(prefix="/sucursales", tags=["Sucursales"])

@router.post("/", response_model=SucursalOut)
def crear_sucursal(payload: SucursalCreate, db: Session = Depends(get_db)):
    return crud.crear_sucursal(db, payload)

@router.get("/negocio/{negocio_id}", response_model=list[SucursalOut])
def listar_por_negocio(negocio_id: UUID, db: Session = Depends(get_db)):
    return crud.listar_sucursales_por_negocio(db, negocio_id)

@router.get("/{sucursal_id}", response_model=SucursalOut)
def obtener_sucursal(sucursal_id: UUID, db: Session = Depends(get_db)):
    sucursal = crud.obtener_sucursal(db, sucursal_id)
    if not sucursal:
        raise HTTPException(status_code=404, detail="Sucursal no encontrada")
    return sucursal

@router.put("/{sucursal_id}", response_model=SucursalOut)
def actualizar_sucursal(sucursal_id: UUID, payload: SucursalUpdate, db: Session = Depends(get_db)):
    sucursal = crud.actualizar_sucursal(db, sucursal_id, payload)
    if not sucursal:
        raise HTTPException(status_code=404, detail="Sucursal no encontrada")
    return sucursal

@router.delete("/{sucursal_id}")
def eliminar_sucursal(sucursal_id: UUID, db: Session = Depends(get_db)):
    if not crud.eliminar_sucursal(db, sucursal_id):
        raise HTTPException(status_code=404, detail="Sucursal no encontrada")
    return {"ok": True}
