backend/
├── app/
│ ├── **init**.py
│ ├── main.py # Punto de entrada si luego separamos desde main.py raíz
│ ├── config.py # Configuración del entorno
│ ├── database.py # Configuración de SQLAlchemy
│ ├── models/ # Modelos SQLAlchemy
│ ├── schemas/ # Pydantic para validación
│ ├── crud/ # Lógica de acceso a datos
│ ├── services/ # Servicios (negocio, autenticación, etc.)
│ ├── routes/ # Rutas (endpoints)
│ └── utils/ # Utilidades como seguridad, hashing, etc.
├── .env # Variables de entorno
├── requirements.txt # Dependencias
└── alembic/ # Migraciones opcionales
