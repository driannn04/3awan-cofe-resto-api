from sqlalchemy import create_engine, text

# URL database kamu
DATABASE_URL = "postgresql://postgres:NhlSoKTjSkvZuARzWwizekSjdZeenyVP@switchback.proxy.rlwy.net:36266/railway"

engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    print("🚀 Mengecek dan memperbaiki kolom 'orders.custumer_name'...")
    try:
        conn.execute(text("ALTER TABLE orders RENAME COLUMN custumer_name TO customer_name;"))
        conn.commit()
        print("✅ Kolom berhasil diubah menjadi 'customer_name'!")
    except Exception as e:
        print("⚠️ Tidak perlu diubah atau sudah benar:", e)
