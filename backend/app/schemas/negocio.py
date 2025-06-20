# app/schemas/negocio.py

from pydantic import BaseModel, UUID4
from typing import Optional

class NegocioBase(BaseModel):
    nombre_fantasia: str
    razon_social: str
    rut: str
    giro: Optional[str] = None
    direccion_principal: Optional[str] = None
    cantidad_sucursales: Optional[int] = 1
    activo: Optional[bool] = True

class NegocioCreate(NegocioBase):
    pass

class NegocioUpdate(NegocioBase):
    pass

class NegocioOut(NegocioBase):
    id: UUID4

    class Config:
        from_attributes = True
