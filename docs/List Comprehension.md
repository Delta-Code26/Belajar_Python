# 🧠 **Pythonic Thinking: Menulis Kode Python Seperti Pro**  

Pythonic Thinking adalah cara menulis kode yang **bersih, efisien, dan sesuai standar Python**. Di sini, kita bahas **list comprehension, lambda, map/filter/reduce, serta generator & iterator**.  

---

## 🚀 **1. List Comprehension: Cara Elegan Buat List**  

List comprehension adalah cara **singkat & cepat** buat bikin list baru dari list lama.  

### 🔹 **Tanpa List Comprehension (Cara Biasa)**  
```python
angka = [1, 2, 3, 4, 5]
kuadrat = []
for i in angka:
    kuadrat.append(i ** 2)

print(kuadrat)  # Output: [1, 4, 9, 16, 25]
```

### 🔹 **Dengan List Comprehension (Pythonic 🚀)**  
```python
kuadrat = [i ** 2 for i in angka]
print(kuadrat)  # Output: [1, 4, 9, 16, 25]
```
📌 **Bisa ditambah kondisi (if statement)!**  
```python
genap = [i for i in angka if i % 2 == 0]
print(genap)  # Output: [2, 4]
```

---

## ⚡ **2. Lambda, Map, Filter, Reduce: Pemrograman Fungsional di Python**  

### 🔹 **Lambda (Fungsi Anonim)**  
Fungsi kecil & cepat yang bisa ditulis dalam satu baris.  

```python
tambah = lambda a, b: a + b
print(tambah(3, 4))  # Output: 7
```

### 🔹 **Map (Transformasi List)**  
`map(fungsi, iterable)` → Terapkan fungsi ke setiap elemen dalam list.  

```python
angka = [1, 2, 3, 4]
hasil = list(map(lambda x: x * 2, angka))
print(hasil)  # Output: [2, 4, 6, 8]
```

### 🔹 **Filter (Pilih Elemen yang Sesuai Kondisi)**  
`filter(fungsi, iterable)` → Pilih elemen yang memenuhi kondisi tertentu.  

```python
genap = list(filter(lambda x: x % 2 == 0, angka))
print(genap)  # Output: [2, 4]
```

### 🔹 **Reduce (Kombinasi Semua Elemen)**  
Gunakan `functools.reduce()` buat **mengakumulasi nilai dalam list**.  

```python
from functools import reduce

total = reduce(lambda a, b: a + b, angka)
print(total)  # Output: 10 (1+2+3+4)
```

---

## 🔄 **3. Generator & Iterator: Menghemat Memori dengan Lazy Evaluation**  

### 🔹 **Iterator: Struktur Data yang Bisa Diiterasi**  
List, Tuple, Set, Dictionary semuanya adalah iterator.  

```python
angka = iter([1, 2, 3])  # Ubah list jadi iterator

print(next(angka))  # Output: 1
print(next(angka))  # Output: 2
print(next(angka))  # Output: 3
```
📌 **Kalau `next()` dipanggil terus & elemen habis, bakal error `StopIteration`!**  

---

### 🔹 **Generator: Iterasi Tanpa Boros Memori**  
Generator **mirip function**, tapi pakai `yield` buat menyimpan state terakhir.  

```python
def angka_generator():
    for i in range(1, 4):
        yield i  # Simpan state tiap kali dipanggil

gen = angka_generator()

print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
```

📌 **Keuntungan Generator:**  
✅ **Lebih hemat memori** dibandingkan list besar.  
✅ **Cocok buat data streaming atau perhitungan besar.**  

---

## 🎯 **Kesimpulan**  
✅ **List Comprehension** → Cara cepat bikin list.  
✅ **Lambda, Map, Filter, Reduce** → Teknik pemrograman fungsional.  
✅ **Generator & Iterator** → Menghemat memori dengan lazy evaluation.  

**Next: Multi-threading & Async Programming! 🚀**