# app/crud/certificado_digital.py

from sqlalchemy.orm import Session
from app.models.certificado_digital import CertificadoDigital
from app.schemas.certificado_digital import CertificadoDigitalCreate, CertificadoDigitalUpdate
from uuid import UUID

def crear_certificado(db: Session, cert: CertificadoDigitalCreate) -> CertificadoDigital:
    db_cert = CertificadoDigital(**cert.dict())
    db.add(db_cert)
    db.commit()
    db.refresh(db_cert)
    return db_cert

def obtener_certificado(db: Session, certificado_id: UUID) -> CertificadoDigital | None:
    return db.query(CertificadoDigital).filter(CertificadoDigital.id == certificado_id).first()

def listar_certificados_por_negocio(db: Session, negocio_id: UUID):
    return db.query(CertificadoDigital).filter(CertificadoDigital.negocio_id == negocio_id).all()

def actualizar_certificado(db: Session, certificado_id: UUID, datos: CertificadoDigitalUpdate) -> CertificadoDigital | None:
    cert = obtener_certificado(db, certificado_id)
    if cert:
        for key, value in datos.dict(exclude_unset=True).items():
            setattr(cert, key, value)
        db.commit()
        db.refresh(cert)
    return cert

def eliminar_certificado(db: Session, certificado_id: UUID) -> bool:
    cert = obtener_certificado(db, certificado_id)
    if cert:
        db.delete(cert)
        db.commit()
        return True
    return False
