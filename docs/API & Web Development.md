# 🌐 **API & Web Development dengan Python**  

Python punya banyak framework powerful buat bikin **API** dan **website**, seperti **Flask** dan **Django**. Di sini, kita bakal bahas cara bikin **REST API** dan website sederhana dengan Python.  

---

## 🚀 **1. REST API dengan Flask**  

API (Application Programming Interface) memungkinkan aplikasi **berkomunikasi** satu sama lain. Kita bisa bikin API di Python pakai **Flask**.  

📌 **Install Flask dulu**  
```sh
pip install flask
```

### 🔹 **Contoh: REST API Sederhana dengan Flask**  
```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Data contoh
users = [
    {"id": 1, "nama": "Adit", "umur": 25},
    {"id": 2, "nama": "Budi", "umur": 30}
]

# Endpoint GET (Ambil Data)
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

# Endpoint POST (Tambah Data)
@app.route("/users", methods=["POST"])
def add_user():
    data = request.json
    users.append({"id": len(users) + 1, "nama": data["nama"], "umur": data["umur"]})
    return jsonify({"message": "User ditambahkan!"})

if __name__ == "__main__":
    app.run(debug=True)
```

📌 **Coba jalankan server:**  
```sh
python nama_file.py
```
Buka browser dan akses **`http://127.0.0.1:5000/users`** buat lihat data!  

---

## 🎨 **2. Web Development dengan Flask**  

Flask juga bisa dipakai buat bikin website **dengan HTML & CSS**.  

📌 **Buat struktur folder:**  
```
/project
  /templates
    index.html
  app.py
```

### 🔹 **File `app.py` (Kode Flask-nya)**  
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
```

### 🔹 **File `templates/index.html` (HTML-nya)**  
```html
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Website</title>
</head>
<body>
    <h1>Halo, Selamat Datang di Website Flask!</h1>
</body>
</html>
```
📌 **Jalankan Flask dan buka `http://127.0.0.1:5000/` buat lihat websitenya!** 🎉  

---

## 🏗 **3. Django: Framework Web yang Lebih Besar**  

Kalau butuh framework lebih lengkap (termasuk admin panel otomatis), pakai **Django**.  

📌 **Install Django:**  
```sh
pip install django
```

📌 **Buat proyek Django:**  
```sh
django-admin startproject myproject
cd myproject
python manage.py runserver
```
Buka **`http://127.0.0.1:8000/`**, Django siap jalan! 🚀  

---

## 🎯 **Kesimpulan**  
✅ **Flask** → Ringan & fleksibel buat API & website kecil.  
✅ **Django** → Cocok buat proyek besar dengan fitur lengkap.  

**Next: Data Science & Machine Learning! 🚀**