# 🔥 **Fungsi di Python**  

Fungsi adalah **blok kode yang bisa dipanggil kapan saja**, sehingga kode kita lebih **rapi, efisien, dan bisa digunakan ulang**.  

---

## 🎯 **1. Definisi & Pemanggilan Fungsi**  

Kita bisa **mendefinisikan** fungsi sendiri menggunakan `def`.  

### 🔹 **Sintaks Dasar**
```python
def nama_fungsi():
    # kode di dalam fungsi
    print("Halo dari dalam fungsi!")

# Pemanggilan fungsi
nama_fungsi()
```
📌 **Tanpa pemanggilan**, fungsi nggak akan jalan!  

---

### 🔥 **Contoh: Fungsi Sederhana**
```python
def sapa():
    print("Halo! Selamat datang di Python 🚀")

sapa()
```
📝 **Output:**  
```
Halo! Selamat datang di Python 🚀
```

---

## 🔄 **2. Parameter & Return Value**  

Fungsi bisa menerima **parameter (input)** dan mengembalikan **nilai (return value)**.  

### 🔹 **A. Parameter (Input ke Fungsi)**  
```python
def sapa_nama(nama):
    print(f"Halo, {nama}! Selamat belajar Python.")

sapa_nama("Adit")
sapa_nama("Budi")
```
📝 **Output:**  
```
Halo, Adit! Selamat belajar Python.  
Halo, Budi! Selamat belajar Python.  
```

📌 **Parameter bisa lebih dari satu**!  
```python
def tambah(a, b):
    print(f"Hasil: {a + b}")

tambah(5, 3)  # Output: Hasil: 8
```

---

### 🔹 **B. Return Value (Mengembalikan Hasil)**  
Gunakan `return` kalau mau **mengembalikan nilai** dari fungsi.  

```python
def luas_persegi(sisi):
    return sisi * sisi

hasil = luas_persegi(4)
print(f"Luas persegi: {hasil}")  # Output: Luas persegi: 16
```

📌 **Keuntungan `return`** → Bisa menyimpan hasil fungsi ke variabel lain.

---

### 🔹 **C. Default Parameter (Nilai Bawaan)**  
```python
def salam(nama="User"):
    print(f"Halo, {nama}!")

salam()         # Output: Halo, User!
salam("Rina")   # Output: Halo, Rina!
```
📌 Jika parameter **tidak diberikan**, Python pakai **nilai default**.  

---

## ⚡ **3. Fungsi Bawaan Python (Built-in Functions)**  

Python punya banyak fungsi bawaan yang langsung bisa dipakai!  

| **Fungsi**  | **Deskripsi**  | **Contoh**  |
|-------------|---------------|------------|
| `print()`   | Menampilkan teks | `print("Hello!")` |
| `input()`   | Menerima input user | `nama = input("Masukkan nama: ")` |
| `len()`     | Menghitung panjang data | `len("Python")  # 6` |
| `type()`    | Mengecek tipe data | `type(123)  # <class 'int'>` |
| `int()`     | Konversi ke integer | `int("10")  # 10` |
| `float()`   | Konversi ke float | `float("3.14")  # 3.14` |
| `str()`     | Konversi ke string | `str(123)  # "123"` |
| `abs()`     | Nilai mutlak | `abs(-5)  # 5` |
| `round()`   | Pembulatan angka | `round(3.6)  # 4` |
| `max()`     | Nilai terbesar | `max([1, 2, 3])  # 3` |
| `min()`     | Nilai terkecil | `min([1, 2, 3])  # 1` |
| `sum()`     | Menjumlahkan elemen | `sum([1, 2, 3])  # 6` |

📌 **Contoh Penggunaan**  
```python
angka = [4, 8, 2, 9, 5]

print(max(angka))  # 9
print(min(angka))  # 2
print(sum(angka))  # 28
print(len(angka))  # 5
```

---

## 🚀 **Kesimpulan**  
✅ **Fungsi** membantu membuat kode lebih rapi & reusable.  
✅ **Parameter** → Bisa menerima input.  
✅ **Return** → Bisa mengembalikan nilai ke variabel lain.  
✅ **Python punya banyak fungsi bawaan** buat mempermudah coding!  

Next: **Struktur Data Python (List, Tuple, Dictionary, Set)! 🔥**