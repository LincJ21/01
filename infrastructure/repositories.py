from sqlalchemy.orm import Session
from domain import models, schemas

def get_product_by_id(db: Session, local_kw: str):
    return db.query(models.Product).filter(models.Product.local_kw == local_kw).first()

def get_all_products(db: Session):
    return db.query(models.Product).all()

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(
        name=product.name,
        local_kw=product.local_kw,
        id_t_producto=product.id_t_producto,
        imagen_url=product.imagen_url  # Nuevo campo
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product