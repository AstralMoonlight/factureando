# app/schemas/certificado_digital.py

from pydantic import BaseModel, UUID4
from typing import Optional
from datetime import datetime

class CertificadoDigitalBase(BaseModel):
    nombre_archivo: str
    ruta_archivo: Optional[str] = None
    password_encriptado: str
    fecha_inicio: Optional[datetime] = None
    fecha_expiracion: datetime
    es_activo: Optional[bool] = True

class CertificadoDigitalCreate(CertificadoDigitalBase):
    negocio_id: UUID4

class CertificadoDigitalUpdate(CertificadoDigitalBase):
    pass

class CertificadoDigitalOut(CertificadoDigitalBase):
    id: UUID4
    negocio_id: UUID4

    class Config:
        from_attributes = True
