🍽️ 3awan Cafe & Resto API

Backend REST API untuk aplikasi 3awan Cafe & Resto — dibangun dengan Python (Flask) dan PostgreSQL, serta dihosting di Railway.

⚙️ Deskripsi

API ini berfungsi sebagai server utama yang mengelola data menu restoran dan pesanan dari aplikasi Flutter.
Semua data disimpan di database PostgreSQL dan dapat diakses secara publik melalui endpoint Railway.

🧱 Struktur Tabel
menus
Kolom	Tipe Data	Keterangan
id	Integer (Primary Key)	ID menu
name	Varchar	Nama menu
price	Integer	Harga menu
category	Varchar	Kategori (Coffee / Non Coffee / Makanan)
image_url	Text	Link gambar menu
🔗 API Endpoint
Metode	Endpoint	Deskripsi
GET	/api/menus	Ambil semua menu
GET	/api/menus/{id}	Ambil menu berdasarkan ID
POST	/api/menus	Tambah menu baru
PUT	/api/menus/{id}	Update menu
DELETE	/api/menus/{id}	Hapus menu

Contoh:

GET https://3awan-caferesto-api.up.railway.app/api/menus

🧰 Teknologi yang Digunakan

Python 3.x

Flask (REST API)

PostgreSQL

Railway Hosting

CORS + JSON Response

🛠️ Instalasi Lokal

1️⃣ Clone repository

git clone https://github.com/AndrianSaputra/3awan-caferesto-api.git
cd 3awan-caferesto-api


2️⃣ Install dependencies

pip install -r requirements.txt


3️⃣ Konfigurasi database PostgreSQL
Edit file .env atau konfigurasi langsung di Railway:

DATABASE_URL=postgresql://user:password@host:port/database


4️⃣ Jalankan server

python app.py


Server akan berjalan di:

http://127.0.0.1:5000

☁️ Hosting di Railway

1️⃣ Login ke Railway.app

2️⃣ Deploy project Python ini
3️⃣ Hubungkan dengan database PostgreSQL
4️⃣ Pastikan endpoint API bisa diakses publik, contoh:

https://3awan-caferesto-api.up.railway.app/api/menus

📁 Struktur Folder
3awan-caferesto-api/
├── app.py
├── controllers/
│   └── menu_controller.py
├── models/
│   └── menu_model.py
├── requirements.txt
└── README.md

🧑‍💻 Developer

👨‍💻 Andrian Saputra
📚 Mobile Programming Semester 5
🏫 Universitas [Unib.BinaNiaga]

🏁 Lisensi

Proyek ini dibuat untuk kebutuhan akademik dan pengembangan pembelajaran.