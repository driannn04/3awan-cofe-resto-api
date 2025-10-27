from sqlalchemy import Column, Integer, Float, Text, DateTime
from config.database import Base
from sqlalchemy.sql import func

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(Text)
    total_price = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
