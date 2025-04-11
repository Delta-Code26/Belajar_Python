

---

### 📄 **Unit Testing dan TDD (Test-Driven Development)**

---

## 🧪 Apa Itu Unit Testing?

**Unit testing** adalah proses menguji bagian terkecil dari kode (biasanya fungsi atau metode) secara terpisah untuk memastikan mereka bekerja sesuai harapan.

> “Ngetes fungsi kayak nyicipin masakan sebelum disajikan ke bos 😎”

---

## 🛠️ Kenapa Unit Testing Penting?

- Menangkap bug lebih awal (sebelum jadi drama produksi)
- Bikin refactor lebih aman
- Jadi dokumentasi hidup
- Nambah kepercayaan diri sebelum deploy 🚀

---

## 🔧 Dasar Unit Testing dengan `unittest`

Python punya modul built-in bernama `unittest`. Contoh dasar:

```python
import unittest

def tambah(a, b):
    return a + b

class TestTambah(unittest.TestCase):
    def test_tambah_positif(self):
        self.assertEqual(tambah(1, 2), 3)

if __name__ == '__main__':
    unittest.main()
```

Jalankan:

```bash
python test_namafile.py
```

---

## 🧨 Apa Itu TDD?

**Test-Driven Development (TDD)** adalah gaya ngoding di mana kita nulis test **sebelum** nulis kode.

### 🔁 Siklus TDD:
1. 🔴 **Red** – Tulis test yang gagal
2. 🟢 **Green** – Tulis kode minimal agar test lulus
3. 🛠️ **Refactor** – Rapikan kode tanpa bikin test gagal

### 🧪 Contoh Sederhana TDD:

```python
# Step 1: Test dulu
def test_faktor_dari_angka():
    assert faktor(6) == [1, 2, 3, 6]  # Gagal dulu

# Step 2: Implementasi
def faktor(n):
    return [i for i in range(1, n+1) if n % i == 0]
```

---

## 🪄 Mocking: Palsukan Hal yang Ribet

Gunakan `unittest.mock` buat nge-mock API atau database:

```python
from unittest.mock import Mock

api = Mock()
api.get_data.return_value = {"data": 123}

assert api.get_data()["data"] == 123
```

---

## 🔥 Alternatif: Pytest (Simple Banget)

Lebih clean daripada `unittest`, banyak dipakai developer modern.

```python
def tambah(a, b):
    return a + b

def test_tambah():
    assert tambah(3, 4) == 7
```

Jalankan:

```bash
pytest
```

---

## 📊 Cek Seberapa Banyak Kode Yang Dites (Coverage)

```bash
pip install coverage
coverage run -m pytest
coverage report
```

---

## ✅ Best Practices

- Gunakan nama test yang deskriptif: `test_login_dengan_password_salah()`
- Pisahkan file test dari file utama (`test_*.py`)
- Test logic penting, bukan semua baris
- Gunakan CI/CD untuk otomatisasi test
- Jangan takut nulis test sebelum coding (TDD FTW!)

---

## 📌 Kesimpulan

Unit testing dan TDD bukan cuma buat perusahaan gede, tapi buat semua developer yang ingin ngoding tanpa drama di akhir sprint. Tambahin testing di habit coding kamu, kayak sarapan pagi — biar sehat dan kuat 💪🐍

---

Kalau kamu mau, aku bisa langsung buatin juga file markdown-nya dalam bentuk file `.md` biar tinggal kamu taruh di `docs/`. Mau dibuatkan file-nya juga atau kamu copy manual?