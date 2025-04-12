# 🔄 **Logika Pemrograman di Python**  

Sekarang kita masuk ke **logika pemrograman**! Dengan logika pemrograman, kita bisa bikin program yang bisa **mengambil keputusan** dan **mengulang tugas secara otomatis**. Let's gooo! 🚀  

---

## ⚡ **1. If-Else 😎**  

If-Else memungkinkan program buat **mengambil keputusan** berdasarkan kondisi tertentu.  

### 🔹 **Sintaks Dasar**  
```python
if kondisi:
    # kode jika kondisi True
elif kondisi_lain:
    # kode jika kondisi lain True
else:
    # kode jika semua kondisi False
```

### 🔥 **Contoh 1: Cek Bilangan Positif atau Negatif**  
```python
angka = int(input("Masukkan angka: "))

if angka > 0:
    print("Angka ini positif!")
elif angka < 0:
    print("Angka ini negatif!")
else:
    print("Angka ini nol!")
```

### 🔥 **Contoh 2: Cek Login User**  
```python
password = input("Masukkan password: ")

if password == "python123":
    print("Login berhasil! 🎉")
else:
    print("Password salah, coba lagi! ❌")
```

📌 **Tips:**  
- `elif` bisa lebih dari satu.  
- `else` opsional, tapi berguna buat menangani semua kemungkinan lain.  

---

## 🔁 **2. Looping (For & While)**  

Looping digunakan buat **mengulang eksekusi kode** tanpa harus ngetik berkali-kali.  

---

### 🔹 **A. Looping dengan `for`**  
Gunakan `for` buat mengulang suatu kode **dalam jumlah tertentu**.  

#### **1. Looping Menggunakan `range()`**  
```python
for i in range(5):  # 0 sampai 4
    print(f"Loop ke-{i}")
```
📌 `range(n)` menghasilkan angka dari `0` sampai `n-1`.  

#### **2. Looping List atau String**  
```python
hobi = ["ngoding", "gaming", "makan"]

for h in hobi:
    print("Saya suka", h)
```

```python
for huruf in "Python":
    print(huruf, end=" ")  # Output: P y t h o n
```

---

### 🔹 **B. Looping dengan `while`**  
Gunakan `while` kalau kita nggak tahu pasti berapa kali loop akan berjalan.  

#### **1. Looping sampai kondisi terpenuhi**  
```python
angka = 1

while angka <= 5:
    print(f"Angka sekarang: {angka}")
    angka += 1  # Jangan lupa update biar nggak loop selamanya!
```

#### **2. Program Sederhana: Tebak Angka**  
```python
import random

angka_rahasia = random.randint(1, 10)
tebakan = 0

while tebakan != angka_rahasia:
    tebakan = int(input("Tebak angka (1-10): "))
    
    if tebakan < angka_rahasia:
        print("Terlalu kecil! ⬆️")
    elif tebakan > angka_rahasia:
        print("Terlalu besar! ⬇️")
    else:
        print("Benar! 🎉")
```

📌 **Tips:**  
- `while` cocok buat **program yang harus berjalan terus sampai kondisi tertentu terpenuhi**.  
- Jangan lupa **update kondisi dalam loop** biar gak stuck di **infinite loop**.  

---

## 🔄 **3. Break, Continue, dan Pass**  

Terkadang kita butuh **menghentikan atau melewati sebagian kode dalam loop**.  

### 🔹 **A. `break` → Hentikan loop langsung**  
```python
for angka in range(1, 10):
    if angka == 5:
        print("Angka 5 ketemu, loop berhenti!")
        break
    print("Angka:", angka)
```
📌 Kalau `break` ketemu, loop langsung berhenti!  

---

### 🔹 **B. `continue` → Lewati iterasi & lanjut ke berikutnya**  
```python
for angka in range(1, 6):
    if angka == 3:
        print("Lewati angka 3")
        continue
    print("Angka:", angka)
```
📌 Kalau `continue` ketemu, kode setelahnya dalam loop **dilewati**, tapi loop tetap lanjut.  

---

### 🔹 **C. `pass` → Placeholder (nggak ngapa-ngapain)**  
Kadang kita butuh **struktur kode**, tapi belum mau diisi logikanya. Gunakan `pass`!  

```python
for angka in range(1, 6):
    if angka == 3:
        pass  # Nanti bisa diisi logika lain
    print("Angka:", angka)
```
📌 `pass` berguna kalau kita mau **tunda penulisan kode** tanpa kena error.  

---

## 🚀 **Kesimpulan**  
✅ **If-Else** → Mengambil keputusan berdasarkan kondisi.  
✅ **For Loop** → Mengulang berdasarkan jumlah tertentu atau koleksi data.  
✅ **While Loop** → Mengulang sampai kondisi tertentu terpenuhi.  
✅ **Break, Continue, Pass** → Mengontrol jalannya loop.  

**Next: Fungsi di Python! 🔥**