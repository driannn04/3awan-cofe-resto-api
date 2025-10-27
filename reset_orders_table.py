from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql://postgres:NhlSoKTjSkvZuARzWwizekSjdZeenyVP@switchback.proxy.rlwy.net:36266/railway"
engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    print("⚙️ Menghapus tabel 'orders' lama...")
    conn.execute(text("DROP TABLE IF EXISTS orders CASCADE;"))
    conn.commit()
    print("✅ Tabel orders berhasil dihapus.")
