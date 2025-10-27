from sqlalchemy import create_engine, text

# 🔗 Koneksi ke PostgreSQL Railway kamu
DATABASE_URL = "postgresql://postgres:NhlSoKTjSkvZuARzWwizekSjdZeenyVP@switchback.proxy.rlwy.net:36266/railway"
engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    print("🚀 Menambahkan data contoh ke database...\n")

    # --- MENUS ---
    conn.execute(text("""
        INSERT INTO menus (name, price, category, description, image_url)
        VALUES
        ('Nasi Goreng Spesial', 25000, 'Makanan', 'Nasi goreng dengan ayam dan telur.', 'https://picsum.photos/200'),
        ('Mie Ayam Bakso', 22000, 'Makanan', 'Mie ayam dengan tambahan bakso sapi.', 'https://picsum.photos/200'),
        ('Es Teh Manis', 8000, 'Minuman', 'Teh manis dingin segar.', 'https://picsum.photos/200'),
        ('Cappuccino', 20000, 'Minuman', 'Kopi susu dengan foam lembut.', 'https://picsum.photos/200');
    """))

    # --- ORDERS ---
    conn.execute(text("""
        INSERT INTO orders (customer_name, total_price)
        VALUES
        ('Andrian', 55000),
        ('Budi', 30000);
    """))

    # --- ORDER ITEMS ---
    conn.execute(text("""
        INSERT INTO order_items (order_id, menu_id, quantity, subtotal)
        VALUES
        (1, 1, 1, 25000),
        (1, 3, 2, 16000),
        (2, 2, 1, 22000),
        (2, 4, 1, 20000);
    """))

    conn.commit()
    print("✅ Data contoh berhasil dimasukkan!\n")
    print("👉 Coba buka di browser:")
    print("   http://127.0.0.1:5000/api/menus")
    print("   http://127.0.0.1:5000/api/orders")
    print("   http://127.0.0.1:5000/api/order-items")
