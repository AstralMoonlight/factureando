# app/crud/usuario.py

from sqlalchemy.orm import Session
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate
from app.utils.security import hash_password
from uuid import UUID

def crear_usuario(db: Session, usuario: UsuarioCreate):
    db_usuario = Usuario(
        nombre=usuario.nombre,
        email=usuario.email,
        password_hash=hash_password(usuario.password),
        rol=usuario.rol,
        activo=usuario.activo,
        negocio_id=usuario.negocio_id
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def obtener_usuario_por_email(db: Session, email: str):
    return db.query(Usuario).filter(Usuario.email == email).first()
