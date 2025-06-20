# app/main.py

from fastapi import FastAPI
from app.routes import negocio_router, sucursal_router, certificado_router
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Factureando API")

app.include_router(negocio_router)
app.include_router(sucursal_router)
app.include_router(certificado_router)

@app.get("/")
def root():
    return {"msg": "Factureando Backend funcionando correctamente."}
