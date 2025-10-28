from sqlalchemy import Column, Integer, String, Float, DateTime, func
from config.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String(100))
    total_price = Column(Float, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
