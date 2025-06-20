# app/models/usuario.py

from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from app.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    nombre = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    rol = Column(String, default="vendedor")  # admin, vendedor, superadmin
    activo = Column(Boolean, default=True)

    negocio_id = Column(UUID(as_uuid=True), ForeignKey("negocios.id", ondelete="CASCADE"), nullable=False)
