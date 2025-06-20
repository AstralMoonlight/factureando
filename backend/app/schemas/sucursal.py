# app/schemas/sucursal.py

from pydantic import BaseModel, UUID4
from typing import Optional

class SucursalBase(BaseModel):
    nombre: str
    direccion: Optional[str] = None
    es_principal: Optional[bool] = False

class SucursalCreate(SucursalBase):
    negocio_id: UUID4

class SucursalUpdate(SucursalBase):
    pass

class SucursalOut(SucursalBase):
    id: UUID4
    negocio_id: UUID4

    class Config:
        from_attributes = True
