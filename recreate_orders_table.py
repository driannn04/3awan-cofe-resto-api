from sqlalchemy import create_engine, text

# 🔗 URL database dari Railway kamu
DATABASE_URL = "postgresql://postgres:NhlSoKTjSkvZuARzWwizekSjdZeenyVP@switchback.proxy.rlwy.net:36266/railway"
engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    print("⚙️ Membuat ulang tabel 'orders'...\n")

    # Hapus dulu jika masih ada sisa
    conn.execute(text("DROP TABLE IF EXISTS orders CASCADE;"))

    # Buat ulang tabel orders sesuai model di Python
    conn.execute(text("""
        CREATE TABLE orders (
            id SERIAL PRIMARY KEY,
            customer_name TEXT,
            total_price REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """))

    conn.commit()
    print("✅ Tabel 'orders' berhasil dibuat ulang!\n")
    print("Kolom:")
    print(" - id (serial, primary key)")
    print(" - customer_name (text)")
    print(" - total_price (real)")
    print(" - created_at (timestamp)\n")
    print("Sekarang kamu bisa jalankan 'python seed_data.py' untuk isi data contoh.")
