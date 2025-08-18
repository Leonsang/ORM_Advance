from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# URL de conexión a la base de datos.
# Para este ejemplo, usaremos una base de datos SQLite en un archivo.
# Para usar en memoria: "sqlite:///:memory:"
# Para PostgreSQL: "postgresql://user:password@host/dbname"
DATABASE_URL = "sqlite:///orm_avanzado.db"

# El motor de la base de datos
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Creación de la sesión
# La sesión es el punto de entrada para todas las conversaciones con la base de datos.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos declarativos
# Nuestras clases de modelo heredarán de esta clase.
Base = declarative_base()

def get_db():
    """
    Función para obtener una sesión de base de datos.
    Se asegura de que la sesión se cierre correctamente después de su uso.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_database():
    """
    Crea todas las tablas en la base de datos.
    """
    Base.metadata.create_all(bind=engine)
