# 🍽️ 3awan Cafe Resto API

API backend untuk aplikasi restoran sederhana, dikembangkan menggunakan **Flask + SQLAlchemy** dan database **PostgreSQL (Railway)**.

---

## 🚀 Fitur Utama
- Manajemen Menu (CRUD lengkap)
- Pemesanan (Order) dan Item Pesanan
- Integrasi dengan Flutter (State Management: Provider)
- Otomatis membuat tabel saat pertama dijalankan

---

## 🧱 Struktur Proyek
3awan-cofe-resto-api/
│
├── app.py # Entry point Flask
├── config/
│ └── database.py # Koneksi database + session
├── models/
│ ├── menu_model.py
│ ├── order_model.py
│ └── order_item_model.py
├── controllers/
│ ├── MenuController.py
│ ├── OrderController.py
│ └── OrderItemController.py
├── routes/
│ └── web.py # Semua routing API
├── fix_all_id_autoincrement.py
├── seed_data.py
├── Procfile
└── requirements.txt


---

## 📡 Endpoint API

### 🧾 Menu
| Method | Endpoint | Deskripsi |
|--------|-----------|-----------|
| GET | `/api/menus` | Ambil semua menu |
| GET | `/api/menus/:id` | Ambil satu menu |
| POST | `/api/menus` | Tambah menu |
| PUT | `/api/menus/:id` | Update menu |
| DELETE | `/api/menus/:id` | Hapus menu |

### 🛒 Order
| Method | Endpoint | Deskripsi |
|--------|-----------|-----------|
| GET | `/api/orders` | Ambil semua pesanan |
| POST | `/api/orders` | Tambah pesanan baru |

### 🍴 Order Item
| Method | Endpoint | Deskripsi |
|--------|-----------|-----------|
| GET | `/api/order-items` | Ambil semua item pesanan |
| POST | `/api/order-items` | Tambah item pesanan |

---

## ⚙️ Jalankan Proyek di Lokal

```bash
# Install dependencies
pip install -r requirements.txt

# Jalankan server Flask
python app.py


http://127.0.0.1:5000/api/menus
