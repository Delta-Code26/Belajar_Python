# 🗄️ **Database & ORM: Python & Penyimpanan Data**  

Python bisa terhubung dengan berbagai database seperti **MySQL, PostgreSQL, SQLite**, dan lainnya. Kita bisa mengakses database pakai **SQL langsung** atau pakai **ORM (Object-Relational Mapping)** biar lebih fleksibel dan Pythonic.  

---

## 📌 **1. Menggunakan Database dengan Python (Tanpa ORM)**  

Python punya modul bawaan `sqlite3` buat mengakses database SQLite tanpa install tambahan.  

### 🔹 **Contoh: SQLite dengan Python**  
```python
import sqlite3

# Buat & koneksi ke database
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Buat tabel
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama TEXT,
    umur INTEGER
)
""")

# Insert data
cursor.execute("INSERT INTO users (nama, umur) VALUES (?, ?)", ("Adit", 25))
conn.commit()  # Simpan perubahan

# Ambil data
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())  # Output: [(1, 'Adit', 25)]

conn.close()  # Tutup koneksi
```
📌 **Kelebihan:**  
✅ Langsung akses SQL tanpa library tambahan  
📌 **Kekurangan:**  
❌ Harus tulis query SQL manual  

---

## 🚀 **2. ORM (Object-Relational Mapping) dengan SQLAlchemy**  

ORM bikin kita bisa **interaksi dengan database pakai Python OOP** tanpa nulis SQL langsung. Salah satu ORM terbaik adalah **SQLAlchemy**.  

📌 **Install SQLAlchemy dulu**  
```sh
pip install sqlalchemy
```

### 🔹 **Contoh: SQLAlchemy ORM dengan SQLite**  
```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Koneksi ke database
engine = create_engine("sqlite:///database.db")
Base = declarative_base()

# Definisi Model (Tabel Users)
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    nama = Column(String)
    umur = Column(Integer)

# Buat tabel di database
Base.metadata.create_all(engine)

# Insert Data ke Database
Session = sessionmaker(bind=engine)
session = Session()

user_baru = User(nama="Budi", umur=30)
session.add(user_baru)
session.commit()

# Ambil Data
users = session.query(User).all()
for user in users:
    print(user.id, user.nama, user.umur)

session.close()
```

📌 **Keuntungan ORM:**  
✅ **Gak perlu nulis SQL manual**  
✅ **Struktur database lebih rapi pakai class Python**  
✅ **Lebih mudah pindah ke database lain (MySQL, PostgreSQL, dll.)**  

---

## 🎯 **Kesimpulan**  
✅ **SQL Biasa** → Cocok kalau butuh kontrol penuh dengan query manual.  
✅ **SQLAlchemy (ORM)** → Cocok buat proyek besar & clean code.  

**Next: API & Web Development! 🚀**