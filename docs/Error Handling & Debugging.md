# 🚨 **Error Handling & Debugging di Python**  

Error pasti terjadi dalam coding, tapi jangan panik! Python punya mekanisme **error handling** biar program gak langsung crash. Kita juga bakal belajar **debugging** buat jadi detektif kode yang handal. 🔍🕵️‍♂️  

---

## ⚠️ **1. Try-Except-Finally (Menangani Error dengan Elegan)**  

**`try-except`** digunakan untuk menangkap error tanpa bikin program berhenti.  

### 🔹 **Contoh Sederhana**  
```python
try:
    angka = int(input("Masukkan angka: "))
    hasil = 10 / angka
    print(f"Hasil: {hasil}")

except ZeroDivisionError:
    print("Error! Tidak bisa membagi dengan nol.")

except ValueError:
    print("Error! Masukkan angka yang benar.")

except Exception as e:
    print(f"Terjadi error: {e}")

finally:
    print("Program selesai.")
```
📌 **`finally`** akan selalu dijalankan, entah ada error atau tidak.  
📌 **`Exception as e`** menangkap semua jenis error.  

**Contoh Output:**  
```
Masukkan angka: 0
Error! Tidak bisa membagi dengan nol.
Program selesai.
```

---

## 🚀 **2. Raise & Custom Exception**  

Kita juga bisa **membuat error sendiri** dengan `raise`.  

### 🔹 **Raise Exception Manual**  
```python
def cek_umur(umur):
    if umur < 18:
        raise ValueError("Umur harus minimal 18 tahun!")
    return "Akses diberikan."

try:
    print(cek_umur(16))
except ValueError as e:
    print(f"Error: {e}")
```
📌 **Hasilnya:**  
```
Error: Umur harus minimal 18 tahun!
```

### 🔹 **Membuat Exception Sendiri**  
```python
class CustomError(Exception):
    pass  # Bisa ditambah fitur sendiri

try:
    raise CustomError("Ini error khusus!")
except CustomError as e:
    print(f"Custom Error: {e}")
```

---

## 🕵️‍♂️ **3. Debugging Kayak Detektif**  

Debugging adalah proses **mencari & memperbaiki bug** dalam kode. Python punya beberapa tools keren buat ini!  

### 🔹 **1. Gunakan Print Statement 📢**  
Kadang, **print()** bisa bantu cari bug.  
```python
def bagi(a, b):
    print(f"DEBUG: a={a}, b={b}")  # Debugging pakai print
    return a / b

print(bagi(10, 2))
```

### 🔹 **2. Gunakan `assert` Buat Validasi**  
```python
def cek_nilai(n):
    assert n > 0, "Nilai harus lebih besar dari 0!"
    return f"Nilai valid: {n}"

print(cek_nilai(5))  # Berhasil
print(cek_nilai(-3))  # AssertionError
```

### 🔹 **3. Debugging Pakai `pdb` (Python Debugger) 🕵️‍♂️**  
Ketik `import pdb; pdb.set_trace()` di mana saja buat masuk mode debugging interaktif.  
```python
import pdb

def hitung(a, b):
    pdb.set_trace()  # Debugging mulai di sini
    return a + b

hitung(10, 5)
```
📌 **Command Debugging di pdb:**  
- `n` (next) → Jalankan kode baris demi baris  
- `c` (continue) → Lanjutkan eksekusi normal  
- `p variabel` → Cetak nilai variabel  

---

## 🎯 **Kesimpulan**  
✅ **Try-Except-Finally** → Tangkap error tanpa bikin program crash.  
✅ **Raise & Custom Exception** → Bisa bikin error sendiri sesuai kebutuhan.  
✅ **Debugging** → Bisa pakai print, assert, atau Python Debugger (`pdb`).  

**Next: Manipulasi File (Baca & Tulis File)! 🚀**