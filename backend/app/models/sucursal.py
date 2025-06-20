# app/models/sucursal.py

from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from app.database import Base

class Sucursal(Base):
    __tablename__ = "sucursales"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    nombre = Column(String, nullable=False)
    direccion = Column(String, nullable=True)
    es_principal = Column(Boolean, default=False)

    negocio_id = Column(UUID(as_uuid=True), ForeignKey("negocios.id", ondelete="CASCADE"), nullable=False)
    negocio = relationship("Negocio", back_populates="sucursales")
