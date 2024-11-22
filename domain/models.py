from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from infrastructure.database import Base

class Product(Base):
    __tablename__ = "producto02"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    local_kw = Column(String, index=True)
    id_t_producto = Column(Integer, ForeignKey('Tipo_Producto02.id'))
    imagen_url = Column(String, index=True)  # Nuevo campo

    tipo_producto = relationship("Tipo_Producto")

class Tipo_Producto(Base):
    __tablename__ = "Tipo_Producto02"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)