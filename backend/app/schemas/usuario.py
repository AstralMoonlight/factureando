# app/schemas/usuario.py

from pydantic import BaseModel, EmailStr, UUID4
from typing import Optional

class UsuarioBase(BaseModel):
    nombre: str
    email: EmailStr
    rol: Optional[str] = "vendedor"
    activo: Optional[bool] = True

class UsuarioCreate(UsuarioBase):
    password: str
    negocio_id: UUID4

class UsuarioOut(UsuarioBase):
    id: UUID4
    negocio_id: UUID4

    class Config:
        from_attributes = True

class UsuarioLogin(BaseModel):
    email: EmailStr
    password: str
