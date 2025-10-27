from sqlalchemy import Column, Integer, Float, ForeignKey
from config.database import Base

class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id", ondelete="CASCADE"))
    menu_id = Column(Integer, ForeignKey("menus.id"))
    quantity = Column(Integer, nullable=False)
    subtotal = Column(Float)
