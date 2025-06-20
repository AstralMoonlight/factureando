# app/main.py

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.security import OAuth2PasswordBearer

from app.routes import negocio_router, sucursal_router, certificado_router
from app.routes.auth import router as auth_router
from app.database import Base, engine

app = FastAPI(title="Factureando API", version="0.1.0")

# Routers
app.include_router(auth_router)
app.include_router(negocio_router)
app.include_router(sucursal_router)
app.include_router(certificado_router)

# DB
Base.metadata.create_all(bind=engine)

# Seguridad para Swagger UI
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Factureando API",
        version="0.1.0",
        description="Sistema de facturación e inventario con autenticación JWT.",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "OAuth2PasswordBearer": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"OAuth2PasswordBearer": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

# Ruta raíz
@app.get("/")
def root():
    return {"msg": "Factureando Backend funcionando correctamente."}
