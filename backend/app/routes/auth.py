# app/routes/auth.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.usuario import UsuarioCreate, UsuarioLogin
from app.schemas.token import TokenOut
from app.crud.usuario import crear_usuario, obtener_usuario_por_email
from app.utils.security import verify_password, create_access_token
from app.database import get_db

router = APIRouter(prefix="/auth", tags=["Autenticación"])

@router.post("/register", response_model=TokenOut)
def register(user: UsuarioCreate, db: Session = Depends(get_db)):
    if obtener_usuario_por_email(db, user.email):
        raise HTTPException(status_code=400, detail="El correo ya está registrado")
    nuevo_usuario = crear_usuario(db, user)
    token = create_access_token(data={"sub": str(nuevo_usuario.id)})
    return {"access_token": token, "token_type": "bearer"}

@router.post("/login", response_model=TokenOut)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = obtener_usuario_por_email(db, form_data.username)
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    token = create_access_token(data={"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}
