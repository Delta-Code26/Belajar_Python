# 🏗️ **Pemrograman Berbasis Objek (OOP) di Python**  

OOP (Object-Oriented Programming) adalah gaya pemrograman yang berfokus pada **objek**. Konsep ini mempermudah **pengelolaan kode**, terutama dalam proyek besar.  

---

## 🎭 **1. Kelas & Objek**  

### 🔹 **Apa Itu Kelas & Objek?**  
- **Kelas (Class)** → Blueprint atau cetakan untuk membuat objek.  
- **Objek** → Hasil nyata yang dibuat dari kelas.  

### 🔹 **Membuat Kelas & Objek**  
```python
# Membuat kelas
class Mobil:
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna

    def info(self):
        return f"Mobil {self.merk} berwarna {self.warna}"

# Membuat objek dari kelas
mobil1 = Mobil("Toyota", "Merah")
mobil2 = Mobil("Honda", "Hitam")

print(mobil1.info())  # Output: Mobil Toyota berwarna Merah
print(mobil2.info())  # Output: Mobil Honda berwarna Hitam
```
📌 **`__init__`** → Constructor, dipanggil saat objek dibuat.  
📌 **`self`** → Mengacu pada instance objek itu sendiri.  

---

## 🔧 **2. Atribut & Method**  

### 🔹 **Atribut (Variabel dalam Kelas)**  
Atribut bisa bersifat **instance** (berbeda tiap objek) atau **class** (sama untuk semua objek).  
```python
class Kucing:
    spesies = "Mamalia"  # Atribut kelas (sama untuk semua objek)

    def __init__(self, nama, umur):
        self.nama = nama  # Atribut instance
        self.umur = umur

kucing1 = Kucing("Milo", 3)
kucing2 = Kucing("Luna", 2)

print(kucing1.spesies)  # Output: Mamalia
print(kucing2.nama)  # Output: Luna
```

### 🔹 **Method (Fungsi dalam Kelas)**  
```python
class Laptop:
    def __init__(self, merk, harga):
        self.merk = merk
        self.harga = harga

    def diskon(self, persen):
        self.harga -= self.harga * (persen / 100)
        return f"Harga setelah diskon: {self.harga}"

laptop1 = Laptop("Asus", 10000000)
print(laptop1.diskon(10))  # Output: Harga setelah diskon: 9000000
```

---

## 🔄 **3. Inheritance (Pewarisan)**  

Pewarisan memungkinkan **satu kelas mewarisi atribut & method dari kelas lain**.  

```python
# Kelas Induk
class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def suara(self):
        return "Suara hewan"

# Kelas Anak (Turunan dari Hewan)
class Kucing(Hewan):
    def suara(self):
        return "Meong!"

kucing1 = Kucing("Kitty")
print(kucing1.nama)  # Output: Kitty
print(kucing1.suara())  # Output: Meong!
```
📌 **Kelas `Kucing` mewarisi `Hewan`**, tapi bisa **mengubah (override)** method `suara()`.

---

## 🎭 **4. Polymorphism (Satu Method, Banyak Bentuk)**  

Polymorphism memungkinkan **method yang sama bekerja berbeda pada kelas yang berbeda**.  

```python
class Anjing:
    def suara(self):
        return "Guk guk!"

class Kucing:
    def suara(self):
        return "Meong!"

# Contoh Polymorphism
hewan_list = [Anjing(), Kucing()]

for hewan in hewan_list:
    print(hewan.suara())  

# Output:
# Guk guk!
# Meong!
```

---

## 🔒 **5. Encapsulation (Membatasi Akses Data)**  

Encapsulation digunakan untuk **menyembunyikan data** agar tidak bisa diakses langsung.  

```python
class BankAccount:
    def __init__(self, saldo):
        self.__saldo = saldo  # Atribut private

    def lihat_saldo(self):
        return f"Saldo: {self.__saldo}"

    def tarik_uang(self, jumlah):
        if jumlah <= self.__saldo:
            self.__saldo -= jumlah
            return f"Berhasil menarik {jumlah}, sisa saldo: {self.__saldo}"
        else:
            return "Saldo tidak cukup!"

rekening = BankAccount(1000000)
print(rekening.lihat_saldo())  # Output: Saldo: 1000000
print(rekening.tarik_uang(500000))  # Output: Berhasil menarik 500000, sisa saldo: 500000

# print(rekening.__saldo)  # ERROR: Tidak bisa diakses langsung!
```
📌 Gunakan **dua underscore (`__`)** untuk atribut private.  
📌 Data bisa diakses lewat **method khusus** (getter & setter).  

---

## 🎯 **Kesimpulan**  
✅ **Kelas & Objek** → Dasar dari OOP.  
✅ **Atribut & Method** → Variabel & fungsi dalam kelas.  
✅ **Inheritance** → Pewarisan sifat dari kelas induk.  
✅ **Polymorphism** → Method yang sama, hasil berbeda.  
✅ **Encapsulation** → Membatasi akses ke data.  

**Next: Exception Handling (Menangani Error)! 🚀**