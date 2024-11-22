from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    local_kw: str
    imagen_url: str  # Nuevo campo

class ProductCreate(ProductBase):
    id_t_producto: int

class Product(ProductBase):
    id: int
    id_t_producto: int

    class Config:
        orm_mode = True