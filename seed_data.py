from sqlalchemy import create_engine, Column, Integer, String, Float, Text, ForeignKey, DateTime, func
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# 🔑 Koneksi ke Railway PostgreSQL baru
DATABASE_URL = "postgresql://postgres:eEVgAaMBSqAqnIAkcHuLUAKuxSRKHiNN@mainline.proxy.rlwy.net:57119/railway"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# ==========================
# MODEL DATABASE
# ==========================
class Menu(Base):
    __tablename__ = "menus"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, nullable=False)
    price = Column(Float, nullable=False)
    category = Column(Text, nullable=False)
    description = Column(Text)
    image_url = Column(Text)

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String(100))
    total_price = Column(Float, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")

class OrderItem(Base):
    __tablename__ = "order_items"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id", ondelete="CASCADE"))
    menu_id = Column(Integer, ForeignKey("menus.id"))
    quantity = Column(Integer, default=1)
    price = Column(Float, nullable=False)
    subtotal = Column(Float, nullable=False)
    
    order = relationship("Order", back_populates="items")

# ==========================
# CREATE TABLES
# ==========================
def create_tables():
    Base.metadata.create_all(engine)
    print("✅ Tables created successfully!")

# ==========================
# SEED DATA
# ==========================
def seed_data():
    session = SessionLocal()
    
    # Hapus data lama kalau ada
    session.query(OrderItem).delete()
    session.query(Order).delete()
    session.query(Menu).delete()
    session.commit()
    
    # Categories: "Semua", "Coffee", "Makanan", "Non Coffee"
    menu_items = [
        {"name": "Espresso", "price": 20000, "category": "Coffee", "description": "Espresso murni", "image_url": "https://example.com/espresso.jpg"},
        {"name": "Cappuccino", "price": 25000, "category": "Coffee", "description": "Cappuccino spesial", "image_url": "https://example.com/cappuccino.jpg"},
        {"name": "Nasi Goreng", "price": 15000, "category": "Makanan", "description": "Nasi goreng dengan telur", "image_url": "https://example.com/nasigoreng.jpg"},
        {"name": "Mie Ayam", "price": 12000, "category": "Makanan", "description": "Mie ayam lengkap", "image_url": "https://example.com/mieayam.jpg"},
        {"name": "Es Teh Manis", "price": 5000, "category": "Non Coffee", "description": "Teh manis dingin segar", "image_url": "https://example.com/estehmanis.jpg"},
        {"name": "Lemonade", "price": 8000, "category": "Non Coffee", "description": "Minuman segar lemon", "image_url": "https://example.com/lemonade.jpg"},
    ]
    
    for item in menu_items:
        menu = Menu(**item)
        session.add(menu)
    
    session.commit()
    
    # Contoh order
    order1 = Order(customer_name="Andrian Saputra", total_price=45000)
    session.add(order1)
    session.commit()
    
    # Ambil menu untuk order
    espresso = session.query(Menu).filter_by(name="Espresso").first()
    nasi_goreng = session.query(Menu).filter_by(name="Nasi Goreng").first()
    
    item1 = OrderItem(order_id=order1.id, menu_id=espresso.id, quantity=1, price=espresso.price, subtotal=espresso.price*1)
    item2 = OrderItem(order_id=order1.id, menu_id=nasi_goreng.id, quantity=2, price=nasi_goreng.price, subtotal=nasi_goreng.price*2)
    
    session.add_all([item1, item2])
    session.commit()
    
    print("✅ Seed data inserted successfully!")
    session.close()

# ==========================
# MAIN
# ==========================
if __name__ == "__main__":
    create_tables()
    seed_data()
