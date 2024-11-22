from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:SKLYjqmQgbHpHWWxGHIEukBxFpPLipLQ@junction.proxy.rlwy.net:22062/railway"
engine = create_engine(DATABASE_URL)
metadata = MetaData()

Base = declarative_base()

class Tipo_Producto(Base):
    __tablename__ = 'Tipo_Producto02'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class Product(Base):
    __tablename__ = 'producto02'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    local_kw = Column(String, index=True)
    id_t_producto = Column(Integer, ForeignKey('Tipo_Producto02.id'))
    imagen_url = Column(String, index=True)  # Nuevo campo

# Crear las tablas
Base.metadata.create_all(engine)

# Crear una sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

# Insertar datos en Tipo_Producto01
tipo_producto1 = Tipo_Producto(name="Electrónica")
tipo_producto2 = Tipo_Producto(name="Ropa")
db.add(tipo_producto1)
db.add(tipo_producto2)
db.commit()

# Insertar datos en producto01
producto1 = Product(name="Televisor", local_kw="KW1", id_t_producto=tipo_producto1.id, imagen_url="https://drive.google.com/uc?export=view&id=1eVcFr3V4lBgYbu57VBkyHF1OuNpPKyXO")
producto2 = Product(name="Camiseta", local_kw="KW2", id_t_producto=tipo_producto2.id, imagen_url="https://drive.google.com/uc?export=view&id=1MNLUxdPLeTUmdXOs4ciXsO8DFEYML-Mc")
db.add(producto1)
db.add(producto2)
db.commit()

# Cerrar la sesión
db.close()