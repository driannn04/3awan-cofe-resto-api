from sqlalchemy import Column, Integer, String, Float, Text
from config.database import Base

class Menu(Base):
    __tablename__ = "menus"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, nullable=False)
    price = Column(Float, nullable=False)
    category = Column(Text, nullable=False)
    description = Column(Text)
    image_url = Column(Text)
