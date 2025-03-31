# ⚡ **Multi-threading & Async Programming: Python Super Cepat!**  

Python mendukung **multi-threading dan asynchronous programming** buat eksekusi yang lebih cepat & efisien. Ini berguna buat **program yang butuh banyak proses berjalan bersamaan**, seperti:  
✅ **Scraping data** dari banyak situs sekaligus  
✅ **Proses background** (misalnya logging atau notifikasi)  
✅ **Aplikasi real-time** seperti chat atau server web  

---

## 🔄 **1. Multi-threading: Menjalankan Banyak Tugas Bersamaan**  

Python punya modul `threading` buat menjalankan beberapa tugas **di thread berbeda**.  

### 🔹 **Contoh Tanpa Multi-threading (Lambat 😴)**  
```python
import time

def tugas(nama):
    print(f"{nama} mulai...")
    time.sleep(2)  # Simulasi tugas berat
    print(f"{nama} selesai!")

tugas("Tugas 1")
tugas("Tugas 2")
```
📌 **Outputnya berurutan** karena tiap tugas harus selesai dulu sebelum lanjut ke yang lain.

---

### 🔹 **Dengan Multi-threading (Lebih Cepat! 🚀)**  
```python
import threading
import time

def tugas(nama):
    print(f"{nama} mulai...")
    time.sleep(2)
    print(f"{nama} selesai!")

# Buat thread
t1 = threading.Thread(target=tugas, args=("Tugas 1",))
t2 = threading.Thread(target=tugas, args=("Tugas 2",))

# Jalankan thread secara paralel
t1.start()
t2.start()

# Tunggu semua thread selesai
t1.join()
t2.join()

print("Semua tugas selesai!")
```
📌 **Bedanya?**  
✅ **Lebih cepat** karena tugas dijalankan secara paralel  
✅ **Cocok buat tugas I/O-bound** seperti scraping atau download file  

---

## ⏳ **2. Asyncio: Pemrograman Asynchronous di Python**  

Kalau `threading` bagus buat **banyak tugas bersamaan**, **`asyncio` lebih optimal** buat program yang butuh **respons cepat & efisien** seperti API, chatbot, atau server web.  

### 🔹 **Contoh Async dengan `async` dan `await`**  
```python
import asyncio

async def tugas(nama):
    print(f"{nama} mulai...")
    await asyncio.sleep(2)  # Tunggu tanpa menghambat tugas lain
    print(f"{nama} selesai!")

async def main():
    # Jalankan semua tugas secara async
    await asyncio.gather(tugas("Tugas 1"), tugas("Tugas 2"))

asyncio.run(main())
```
📌 **Keuntungan Asyncio:**  
✅ **Lebih ringan** dibandingkan thread biasa  
✅ **Cocok buat tugas yang butuh banyak I/O (baca/tulis file, HTTP request, dsb.)**  

---

## 🎯 **Kesimpulan**  
✅ **Multi-threading** → Jalankan beberapa tugas bersamaan (cocok buat CPU-bound tasks).  
✅ **Asyncio** → Eksekusi non-blokir yang lebih efisien (cocok buat I/O-bound tasks).  

**Next: Database & ORM! 🚀**