# 📂 **File Handling di Python**  

Python punya fitur powerful buat **membaca, menulis, dan mengelola file**. Ini penting banget buat menyimpan data atau membaca informasi dari file eksternal.  

---

## 📝 **1. Baca & Tulis File (TXT, CSV)**  

### 🔹 **Membaca File TXT**  
```python
file = open("data.txt", "r")  # "r" = read mode
isi = file.read()
print(isi)
file.close()  # Jangan lupa tutup file!
```
📌 **Mode dalam `open()`**  
- `"r"` → Read (baca)  
- `"w"` → Write (tulis, overwrite)  
- `"a"` → Append (tambah data tanpa hapus)  
- `"x"` → Create (buat file baru, error kalau sudah ada)  

### 🔹 **Menulis ke File TXT**  
```python
file = open("data.txt", "w")  # "w" akan overwrite isi file
file.write("Halo, ini data baru!\n")
file.close()
```
Kalau mau **nambah data tanpa hapus isi lama**, pakai `"a"` (append).  
```python
file = open("data.txt", "a")
file.write("Tambahan data.\n")
file.close()
```

---

### 📊 **Membaca File CSV**  
CSV (Comma-Separated Values) sering dipakai buat data tabular (seperti Excel).  

```python
import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```
📌 **Hasilnya bisa berupa list:**  
```
['Nama', 'Umur', 'Kota']
['Adit', '21', 'Jakarta']
['Budi', '25', 'Surabaya']
```

### 🔹 **Menulis ke File CSV**  
```python
import csv

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Nama", "Umur", "Kota"])
    writer.writerow(["Adit", 21, "Jakarta"])
    writer.writerow(["Budi", 25, "Surabaya"])
```

---

## 📁 **2. Path & Direktori**  

Python bisa juga **mengelola file & folder** pakai modul `os` dan `pathlib`.  

### 🔹 **Cek Apakah File Ada**  
```python
import os

if os.path.exists("data.txt"):
    print("File ditemukan!")
else:
    print("File tidak ada!")
```

### 🔹 **Cek Isi Folder**  
```python
import os

print(os.listdir("."))  # "." berarti folder saat ini
```

### 🔹 **Membuat & Menghapus Folder**  
```python
os.mkdir("folder_baru")  # Buat folder
os.rmdir("folder_baru")  # Hapus folder kosong
```

---

## 🔄 **3. Context Manager (`with`)**  

`with` memastikan file **tertutup otomatis** setelah digunakan.  

### 🔹 **Membaca File dengan `with`**  
```python
with open("data.txt", "r") as file:
    isi = file.read()
    print(isi)  # File otomatis tertutup setelah keluar blok `with`
```

### 🔹 **Menulis File dengan `with`**  
```python
with open("data.txt", "w") as file:
    file.write("Data baru dengan with statement!\n")
```

---

## 🎯 **Kesimpulan**  
✅ **Baca & Tulis File** → Bisa TXT atau CSV.  
✅ **Path & Direktori** → Bisa cek file, buat/hapus folder.  
✅ **Context Manager (`with`)** → Biar gak lupa tutup file otomatis.  

**Next: Library & Virtual Environment! 🚀**