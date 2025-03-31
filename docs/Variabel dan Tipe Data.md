# 🐍 **Sintaks Dasar Python**  

Setelah berhasil install Python dan menjalankan **Hello World**, sekarang kita masuk ke **dasar-dasar coding** di Python. Ini penting biar nanti lo bisa ngoding dengan lancar. 🚀  

---

## 🎯 **1. Variabel & Tipe Data**  

**Variabel** = tempat buat nyimpen data. Python nggak perlu deklarasi tipe data secara eksplisit, karena dia **dynamic typing** (langsung tau tipe datanya dari nilai yang dikasih).  

🔹 **Contoh Variabel & Tipe Data**  

```python
# String (teks)
nama = "Python"

# Integer (angka bulat)
umur = 25

# Float (angka desimal)
berat = 65.5

# Boolean (True/False)
is_python_easy = True

# List (daftar, bisa diubah)
hobi = ["ngoding", "main game", "nonton anime"]

# Tuple (mirip list, tapi gak bisa diubah)
koordinat = (10, 20)

# Dictionary (mirip JSON, key-value pair)
data_mahasiswa = {
    "nama": "Budi",
    "umur": 20,
    "jurusan": "Informatika"
}

# Set (kumpulan unik, gak ada duplikat)
angka_unik = {1, 2, 3, 4, 4, 5}  # {1, 2, 3, 4, 5}

print(nama, umur, berat, is_python_easy)
```

📌 **Catatan:**  
- String pakai kutip `""` atau `''`.  
- List `[ ]` bisa diubah, sedangkan Tuple `( )` nggak bisa diubah.  
- Dictionary `{}` punya pasangan key-value.  

---

## ➕ **2. Operator (Aritmatika, Perbandingan, Logika)**  

### 🔢 **A. Operator Aritmatika**  

| Operator | Fungsi | Contoh |
|----------|--------|---------|
| `+` | Penjumlahan | `5 + 3  # Hasil: 8` |
| `-` | Pengurangan | `10 - 4  # Hasil: 6` |
| `*` | Perkalian | `6 * 7  # Hasil: 42` |
| `/` | Pembagian | `10 / 2  # Hasil: 5.0` |
| `//` | Pembagian Bulat | `10 // 3  # Hasil: 3` |
| `%` | Modulus (Sisa Bagi) | `10 % 3  # Hasil: 1` |
| `**` | Pangkat | `2 ** 3  # Hasil: 8` |

🔹 **Contoh Penggunaan**  

```python
a = 10
b = 3

print(a + b)  # 13
print(a - b)  # 7
print(a * b)  # 30
print(a / b)  # 3.3333
print(a // b) # 3
print(a % b)  # 1
print(a ** b) # 1000 (10^3)
```

---

### 🔍 **B. Operator Perbandingan**  

| Operator | Fungsi | Contoh |
|----------|--------|---------|
| `==` | Sama dengan | `5 == 5  # True` |
| `!=` | Tidak sama dengan | `5 != 3  # True` |
| `>` | Lebih besar | `7 > 5  # True` |
| `<` | Lebih kecil | `2 < 3  # True` |
| `>=` | Lebih besar atau sama | `5 >= 5  # True` |
| `<=` | Lebih kecil atau sama | `4 <= 6  # True` |

🔹 **Contoh Penggunaan**  

```python
x = 10
y = 5

print(x > y)  # True
print(x < y)  # False
print(x == 10)  # True
print(x != 5)  # True
```

---

### 🤯 **C. Operator Logika**  

| Operator | Fungsi | Contoh |
|----------|--------|---------|
| `and` | True jika kedua kondisi True | `(5 > 3) and (10 > 8)  # True` |
| `or` | True jika salah satu kondisi True | `(5 > 3) or (10 < 8)  # True` |
| `not` | Membalik kondisi | `not (5 > 3)  # False` |

🔹 **Contoh Penggunaan**  

```python
a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False
```

---

## 🗣️ **3. Input & Output (Ngobrol Sama User)**  

### 📥 **A. Input (Menerima Data dari User)**  
Gunakan `input()` buat menerima data dari user.  

```python
nama = input("Masukkan nama kamu: ")
umur = int(input("Masukkan umur kamu: "))  # Convert ke integer

print("Halo,", nama, "! Umur kamu", umur, "tahun.")
```

📌 **Catatan:**  
- `input()` selalu mengembalikan **string**. Kalau mau angka, harus dikonversi pakai `int()` atau `float()`.  

---

### 📤 **B. Output (Menampilkan Data)**  
Gunakan `print()` buat menampilkan teks atau hasil perhitungan.  

```python
nama = "Adit"
umur = 20

# Cara 1: Pakai Koma (,) -> Bisa berbagai tipe data
print("Nama:", nama, "Umur:", umur)

# Cara 2: Pakai f-string (Rekomendasi)
print(f"Nama: {nama}, Umur: {umur}")

# Cara 3: Pakai format()
print("Nama: {}, Umur: {}".format(nama, umur))
```

📌 **f-string (`f"..."`)** adalah cara paling simpel dan rapi buat format teks di Python.  

---

## 🎯 **Kesimpulan**  
✅ **Variabel & Tipe Data** – Python otomatis menentukan tipe data.  
✅ **Operator** – Aritmatika, Perbandingan, dan Logika buat manipulasi data.  
✅ **Input & Output** – `input()` buat menerima data, `print()` buat menampilkan data.  

**Udah siap lanjut ke kontrol alur program? 🔥**  
Next: **If-Else & Looping di Python! 🚀**