from config.database import engine, Base
from models.order_model import Order
from models.order_item_model import OrderItem

print("⚠️ Menghapus tabel lama...")
try:
    OrderItem.__table__.drop(engine, checkfirst=True)
    Order.__table__.drop(engine, checkfirst=True)
    print("✅ Tabel orders & order_items berhasil dihapus.")
except Exception as e:
    print(f"❌ Gagal menghapus tabel: {e}")

print("🧱 Membuat ulang tabel baru...")
try:
    Base.metadata.create_all(bind=engine)
    print("✅ Tabel baru berhasil dibuat ulang sesuai model Python.")
except Exception as e:
    print(f"❌ Gagal membuat tabel baru: {e}")
