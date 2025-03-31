# 🏗️ **Pemrograman Modular di Python**  

Pemrograman modular adalah teknik **membagi kode ke dalam bagian-bagian kecil** yang bisa digunakan kembali. Ini bikin kode lebih **rapi, mudah dikelola, dan scalable**.  

---

## 📌 **1. Import & Modul**  

### 🔹 **Apa Itu Modul?**  
Modul adalah **file Python** yang berisi fungsi, variabel, atau kelas yang bisa digunakan di file lain.  

📌 **Contoh Modul Bawaan Python:**  
- `math` → Operasi matematika  
- `random` → Angka acak  
- `datetime` → Waktu & tanggal  
- `os` → Operasi sistem  

### 🔹 **Cara Import Modul**  
```python
import math  # Mengimpor seluruh modul
print(math.sqrt(16))  # Output: 4.0

from math import sqrt  # Mengimpor fungsi tertentu
print(sqrt(25))  # Output: 5.0

import random as rnd  # Mengubah nama modul (alias)
print(rnd.randint(1, 10))  # Angka acak antara 1-10
```

📌 **Tips:**  
- Pakai `import modul` untuk mengimpor semuanya.  
- Pakai `from modul import fungsi` kalau cuma butuh fungsi tertentu.  
- Pakai `import modul as alias` kalau mau nama lebih singkat.  

---

## 🛠️ **2. Membuat Modul Sendiri**  

Kita bisa bikin modul sendiri dengan **menyimpan kode Python ke file `.py`** dan mengimpornya ke program utama.  

### 🔹 **1. Buat File `modulku.py`**  
```python
# modulku.py
def sapa(nama):
    return f"Halo, {nama}! Selamat datang di Python."
```

### 🔹 **2. Gunakan di Program Utama (`main.py`)**  
```python
import modulku

print(modulku.sapa("Adit"))  # Output: Halo, Adit! Selamat datang di Python.
```

### 🔹 **3. Cara Lain: Import Fungsi Tertentu**  
```python
from modulku import sapa

print(sapa("Budi"))  # Output: Halo, Budi! Selamat datang di Python.
```

📌 **Keuntungan Modul:**  
✅ Bisa digunakan ulang tanpa harus menulis ulang kode.  
✅ Kode lebih rapi dan modular.  

---

## 🤯 **3. `__name__ == "__main__"` itu Apa?**  

Ini digunakan untuk menentukan **apakah file Python sedang dijalankan langsung atau diimpor sebagai modul**.  

### 🔹 **Contoh Sederhana**  
```python
# file: contoh.py
def salam():
    print("Halo dari contoh.py!")

if __name__ == "__main__":
    print("File ini dijalankan langsung.")
    salam()
```

### 🔹 **Uji Coba di Program Utama**  
```python
import contoh  # Mengimpor file contoh.py

print("Program utama berjalan.")
```

📌 **Hasilnya:**  
Jika kita **menjalankan `contoh.py` langsung**, outputnya:  
```
File ini dijalankan langsung.
Halo dari contoh.py!
```
Jika kita **mengimpor `contoh.py` dari file lain**, outputnya:  
```
Program utama berjalan.
```

💡 **Intinya:**  
- `if __name__ == "__main__":` memastikan kode hanya berjalan jika file dieksekusi langsung.  
- Berguna buat testing modul tanpa mengganggu program lain.  

---

## 🎯 **Kesimpulan**  
✅ **Modul** bikin kode lebih rapi & bisa digunakan ulang.  
✅ **Python punya banyak modul bawaan (math, random, os, dll.).**  
✅ **Bisa bikin modul sendiri** dengan menyimpannya sebagai file `.py`.  
✅ **`__name__ == "__main__"`** digunakan untuk membedakan apakah file dijalankan langsung atau diimpor.  

**Next: Exception Handling (Menangani Error)! 🚀**