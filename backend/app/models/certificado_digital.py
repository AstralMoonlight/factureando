# app/models/certificado_digital.py

from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime
from app.database import Base

class CertificadoDigital(Base):
    __tablename__ = "certificados_digitales"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    nombre_archivo = Column(String, nullable=False)
    ruta_archivo = Column(String, nullable=True)
    password_encriptado = Column(String, nullable=False)
    fecha_inicio = Column(DateTime, default=datetime.utcnow)
    fecha_expiracion = Column(DateTime, nullable=False)
    es_activo = Column(Boolean, default=True)

    negocio_id = Column(UUID(as_uuid=True), ForeignKey("negocios.id", ondelete="CASCADE"), nullable=False)
    negocio = relationship("Negocio", back_populates="certificados")
