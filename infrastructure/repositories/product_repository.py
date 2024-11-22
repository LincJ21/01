from sqlalchemy.orm import Session
from domain.models import ProductoDB

def get_all_products(db: Session):
    return db.query(ProductoDB).all()