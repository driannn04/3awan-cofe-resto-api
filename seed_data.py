from sqlalchemy import create_engine, text

# 🔗 URL database Railway kamu
DATABASE_URL = "postgresql://postgres:NhlSoKTjSkvZuARzWwizekSjdZeenyVP@switchback.proxy.rlwy.net:36266/railway"
engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    print("🔍 Mengecek tabel 'menus'...")
    
    # Bersihkan data lama
    conn.execute(text("DELETE FROM menus;"))
    conn.commit()
    print("🧹 Menghapus data lama...")

    print("🍽️ Menambahkan data baru...")

    menus = [
        {
            "name": "Kopi Hitam",
            "price": 12000,
            "category": "Coffee",
            "description": "Kopi hitam panas khas 3awan Cafe",
            "image_url": "https://picsum.photos/200?coffee1"
        },
        {
            "name": "Cappuccino",
            "price": 18000,
            "category": "Coffee",
            "description": "Cappuccino creamy dengan foam lembut",
            "image_url": "https://picsum.photos/200?coffee2"
        },
        {
            "name": "Nasi Goreng Spesial",
            "price": 25000,
            "category": "Makanan",
            "description": "Nasi goreng ayam telur spesial dengan topping sayur segar",
            "image_url": "https://picsum.photos/200?food1"
        },
        {
            "name": "Mie Goreng Jawa",
            "price": 22000,
            "category": "Makanan",
            "description": "Mie goreng khas Jawa dengan rasa autentik",
            "image_url": "https://picsum.photos/200?food2"
        },
        {
            "name": "Es Teh Manis",
            "price": 8000,
            "category": "Non Coffee",
            "description": "Teh manis dingin penyegar tenggorokan",
            "image_url": "https://picsum.photos/200?drink1"
        },
        {
            "name": "Lemon Tea",
            "price": 10000,
            "category": "Non Coffee",
            "description": "Teh lemon segar cocok untuk hari panas",
            "image_url": "https://picsum.photos/200?drink2"
        },
    ]

    for menu in menus:
        conn.execute(text("""
            INSERT INTO menus (name, price, category, description, image_url)
            VALUES (:name, :price, :category, :description, :image_url)
        """), menu)

    conn.commit()
    print("✅ Data menu berhasil dimasukkan ke tabel 'menus'!")
