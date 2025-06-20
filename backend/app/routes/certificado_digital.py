# app/routes/certificado_digital.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from app.schemas.certificado_digital import CertificadoDigitalCreate, CertificadoDigitalUpdate, CertificadoDigitalOut
from app.crud import certificado_digital as crud
from app.database import get_db

router = APIRouter(prefix="/certificados", tags=["Certificados Digitales"])

@router.post("/", response_model=CertificadoDigitalOut)
def crear_certificado(payload: CertificadoDigitalCreate, db: Session = Depends(get_db)):
    return crud.crear_certificado(db, payload)

@router.get("/negocio/{negocio_id}", response_model=list[CertificadoDigitalOut])
def listar_por_negocio(negocio_id: UUID, db: Session = Depends(get_db)):
    return crud.listar_certificados_por_negocio(db, negocio_id)

@router.get("/{certificado_id}", response_model=CertificadoDigitalOut)
def obtener_certificado(certificado_id: UUID, db: Session = Depends(get_db)):
    cert = crud.obtener_certificado(db, certificado_id)
    if not cert:
        raise HTTPException(status_code=404, detail="Certificado no encontrado")
    return cert

@router.put("/{certificado_id}", response_model=CertificadoDigitalOut)
def actualizar_certificado(certificado_id: UUID, payload: CertificadoDigitalUpdate, db: Session = Depends(get_db)):
    cert = crud.actualizar_certificado(db, certificado_id, payload)
    if not cert:
        raise HTTPException(status_code=404, detail="Certificado no encontrado")
    return cert

@router.delete("/{certificado_id}")
def eliminar_certificado(certificado_id: UUID, db: Session = Depends(get_db)):
    if not crud.eliminar_certificado(db, certificado_id):
        raise HTTPException(status_code=404, detail="Certificado no encontrado")
    return {"ok": True}
