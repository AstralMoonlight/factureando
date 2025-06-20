# app/models/negocio.py

from sqlalchemy import Column, String, Boolean, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from app.database import Base

class Negocio(Base):
    __tablename__ = "negocios"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    nombre_fantasia = Column(String, nullable=False)
    razon_social = Column(String, nullable=False)
    rut = Column(String, unique=True, nullable=False)
    giro = Column(String, nullable=True)
    direccion_principal = Column(String, nullable=True)
    cantidad_sucursales = Column(Integer, default=1)
    activo = Column(Boolean, default=True)

    sucursales = relationship("Sucursal", back_populates="negocio", cascade="all, delete")
    certificados = relationship("CertificadoDigital", back_populates="negocio", cascade="all, delete")
