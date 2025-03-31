# 🤖 **Python untuk Otomasi (Automation Scripting)**  

Python bisa digunakan untuk **mengotomatisasi tugas-tugas membosankan**, seperti mengelola file, mengisi formulir, atau bahkan mengendalikan browser! Ini sangat berguna untuk meningkatkan produktivitas.  

---

## 📂 **1. Mengelola File & Folder secara Otomatis**  

📌 **Pindahkan, Ubah Nama, atau Hapus File dengan `os` & `shutil`**  
```python
import os
import shutil

# Buat folder baru
os.mkdir("folder_baru")

# Pindahkan file ke dalam folder
shutil.move("dokumen.txt", "folder_baru/dokumen.txt")

# Hapus file
os.remove("folder_baru/dokumen.txt")

# Hapus folder
os.rmdir("folder_baru")
```
✅ **Berguna buat mengatur ribuan file secara otomatis!**  

---

## 📧 **2. Kirim Email Otomatis dengan Python**  

📌 **Gunakan `smtplib` untuk mengirim email**  
```python
import smtplib

email_pengirim = "emailkamu@gmail.com"
email_penerima = "target@gmail.com"
password = "password_kamu"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(email_pengirim, password)

pesan = "Halo, ini email otomatis dari Python!"
server.sendmail(email_pengirim, email_penerima, pesan)

server.quit()
print("Email terkirim!")
```
⚠ **Pastikan fitur "Less Secure Apps" aktif di Gmail sebelum mencoba!**  

---

## 🌐 **3. Mengotomatisasi Browser dengan Selenium**  

📌 **Instal Selenium & WebDriver**  
```sh
pip install selenium
```

📌 **Contoh: Login Otomatis ke Website**  
```python
from selenium import webdriver

# Buka browser
driver = webdriver.Chrome()
driver.get("https://www.website.com/login")

# Isi username & password
driver.find_element("name", "username").send_keys("user123")
driver.find_element("name", "password").send_keys("pass123")

# Klik tombol login
driver.find_element("id", "login-btn").click()
```
✅ **Cocok buat scraping data atau mengisi formulir otomatis!**  

---

## 📝 **4. Membaca & Menulis Excel secara Otomatis**  

📌 **Gunakan `openpyxl` untuk membaca/mengedit file Excel**  
```python
import openpyxl

# Buka file Excel
wb = openpyxl.load_workbook("data.xlsx")
sheet = wb.active

# Ambil data dari sel
print(sheet["A1"].value)

# Tulis data ke Excel
sheet["B2"] = "Python Automation"
wb.save("data.xlsx")
```
✅ **Berguna buat otomatisasi laporan & data entry!**  

---

## 🎯 **Kesimpulan**  
✅ **`os & shutil`** → Buat mengelola file & folder  
✅ **`smtplib`** → Buat kirim email otomatis  
✅ **`selenium`** → Buat mengontrol browser otomatis  
✅ **`openpyxl`** → Buat baca/tulis file Excel otomatis  

**Next: Python untuk Cybersecurity! 🔒**