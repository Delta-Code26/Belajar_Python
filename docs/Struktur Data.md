# 🧠 **Struktur Data Python** (Level Intermediate)  

Struktur data di Python membantu kita menyimpan dan mengelola data dengan lebih efisien. Python punya 4 struktur data utama:  

1. **List** → Kumpulan data yang bisa diubah (mutable)  
2. **Tuple** → Mirip list, tapi tidak bisa diubah (immutable)  
3. **Set** → Kumpulan unik, tanpa duplikasi  
4. **Dictionary** → Kumpulan data dengan format `key-value`  

---

## 📌 **1. List (Daftar Elemen yang Bisa Diubah)**  

List digunakan untuk menyimpan beberapa item dalam satu variabel. Bisa berisi berbagai tipe data.  

### 🔹 **Membuat List**  
```python
angka = [1, 2, 3, 4, 5]
buah = ["apel", "mangga", "jeruk"]
campuran = [10, "Python", True]
```

### 🔹 **Operasi Dasar List**  
```python
print(angka[0])      # Mengakses elemen pertama -> 1
print(buah[-1])      # Mengakses elemen terakhir -> "jeruk"

buah.append("pisang")  # Menambah item
buah.remove("apel")    # Menghapus item
angka.insert(2, 99)    # Menyisipkan 99 di indeks ke-2
buah.pop()             # Menghapus item terakhir
buah.sort()            # Mengurutkan list
```

📌 **Contoh Penggunaan List**  
```python
# Looping List
for item in buah:
    print(item)
```

---

## 🔗 **2. Tuple (Mirip List, Tapi Tidak Bisa Diubah)**  

Tuple berguna kalau kita ingin data tetap **konstan** dan tidak berubah.  

### 🔹 **Membuat Tuple**  
```python
angka = (1, 2, 3, 4, 5)
warna = ("merah", "hijau", "biru")
```

### 🔹 **Operasi Tuple**  
```python
print(angka[0])  # 1
print(len(warna))  # 3

# Tuple tidak bisa diubah, tapi bisa diubah ke list dulu
warna_list = list(warna)
warna_list.append("kuning")
warna = tuple(warna_list)
print(warna)  # ('merah', 'hijau', 'biru', 'kuning')
```

---

## 🔥 **3. Set (Kumpulan Unik, Tanpa Duplikasi)**  

Set digunakan jika kita butuh **data unik** tanpa elemen duplikat.  

### 🔹 **Membuat Set**  
```python
angka = {1, 2, 3, 3, 4, 5, 5}
print(angka)  # {1, 2, 3, 4, 5} -> Duplikat dihapus
```

### 🔹 **Operasi Set**  
```python
angka.add(6)       # Menambahkan item
angka.remove(3)    # Menghapus item
print(angka)       # {1, 2, 4, 5, 6}

# Operasi Set
genap = {2, 4, 6, 8}
ganjil = {1, 3, 5, 7}

print(genap | ganjil)  # Gabungan (union)
print(genap & ganjil)  # Irisan (intersection)
print(genap - {2, 4})  # Selisih
```

---

## 🗂️ **4. Dictionary (Data Key-Value)**  

Dictionary (`dict`) menyimpan data dalam format `key-value`, seperti JSON.  

### 🔹 **Membuat Dictionary**  
```python
mahasiswa = {
    "nama": "Budi",
    "umur": 20,
    "jurusan": "Informatika"
}
```

### 🔹 **Operasi Dictionary**  
```python
print(mahasiswa["nama"])   # Mengakses nilai -> "Budi"

mahasiswa["umur"] = 21     # Mengubah nilai
mahasiswa["universitas"] = "ITB"  # Menambah key baru
del mahasiswa["jurusan"]   # Menghapus key

print(mahasiswa.keys())    # Melihat semua key
print(mahasiswa.values())  # Melihat semua nilai
print(mahasiswa.items())   # Melihat semua pasangan key-value
```

📌 **Looping Dictionary**  
```python
for key, value in mahasiswa.items():
    print(f"{key}: {value}")
```

---

## 🎯 **Kesimpulan**  
✅ **List** → Bisa diubah, cocok untuk menyimpan banyak item yang bisa diurutkan.  
✅ **Tuple** → Tidak bisa diubah, cocok untuk data konstan.  
✅ **Set** → Tidak ada duplikasi, cocok untuk data unik.  
✅ **Dictionary** → Data dengan pasangan `key-value`, mirip JSON.  

**Next: Manipulasi String & File Handling! 🚀**