from config.database import engine, Base
from models.order_model import Order
from models.order_item_model import OrderItem

print("🧹 Menghapus tabel lama orders & order_items jika ada...")
Base.metadata.drop_all(bind=engine)

print("🧱 Membuat ulang tabel orders & order_items...")
Base.metadata.create_all(bind=engine)

print("✅ Struktur database berhasil diperbarui!")
