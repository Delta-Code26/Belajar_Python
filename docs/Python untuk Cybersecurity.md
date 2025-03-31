# 🔒 **Python untuk Cybersecurity**  

Python sering digunakan dalam dunia **Cybersecurity** untuk **penetration testing, enkripsi data, analisis malware, dan otomatisasi keamanan**.  

---

## 🕵 **1. Membuat Password Generator Otomatis**  

📌 **Gunakan `random` dan `string` untuk membuat password yang kuat**  
```python
import random
import string

def generate_password(length=12):
    karakter = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(karakter) for _ in range(length))
    return password

print("Password baru:", generate_password())
```
✅ **Hasil: Password acak yang sulit ditebak!**  

---

## 🔑 **2. Enkripsi & Dekripsi dengan Python (Fernet - Symmetric Encryption)**  

📌 **Gunakan `cryptography` untuk mengenkripsi data**  
```sh
pip install cryptography
```

```python
from cryptography.fernet import Fernet

# Buat kunci enkripsi
key = Fernet.generate_key()
cipher = Fernet(key)

# Enkripsi pesan
pesan = "Ini adalah data rahasia."
pesan_terenkripsi = cipher.encrypt(pesan.encode())
print("Terenkripsi:", pesan_terenkripsi)

# Dekripsi pesan
pesan_dekripsi = cipher.decrypt(pesan_terenkripsi).decode()
print("Didekripsi:", pesan_dekripsi)
```
✅ **Cocok buat menyimpan data sensitif dengan aman!**  

---

## 🕵 **3. Scan Port Terbuka dengan Python (Port Scanner)**  

📌 **Gunakan `socket` untuk mengecek apakah suatu port terbuka atau tertutup**  
```python
import socket

def scan_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((ip, port))
    s.close()
    return result == 0

target = "192.168.1.1"
ports = [21, 22, 80, 443, 3306]  # Port umum

for port in ports:
    if scan_port(target, port):
        print(f"Port {port} terbuka!")
    else:
        print(f"Port {port} tertutup.")
```
✅ **Digunakan untuk mengecek keamanan jaringan!**  

---

## 🎭 **4. Web Scraping Aman dengan Requests & BeautifulSoup**  

📌 **Gunakan `requests` & `BeautifulSoup` untuk mengambil data dari web dengan aman**  
```sh
pip install requests beautifulsoup4
```

```python
import requests
from bs4 import BeautifulSoup

url = "https://example.com"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

print("Judul Halaman:", soup.title.text)
```
✅ **Pastikan tidak scraping website tanpa izin!** 🚨  

---

## 🎯 **Kesimpulan**  
✅ **Password Generator** → Buat password yang kuat  
✅ **Enkripsi & Dekripsi** → Lindungi data penting  
✅ **Port Scanner** → Cek keamanan jaringan  
✅ **Web Scraping Aman** → Ambil data dari web dengan etika  

**Next: Python untuk Blockchain & Crypto! 🚀**

# Versi 2

# 🔐 **Python untuk Cybersecurity**  

Python banyak digunakan dalam **Cybersecurity** untuk analisis malware, pemindaian jaringan, eksploitasi keamanan, hingga forensik digital.  

---

## 🛠 **1. Instalasi & Setup Alat Cybersecurity**  

📌 **Install pustaka yang sering digunakan dalam Cybersecurity**  
```sh
pip install scapy cryptography requests
```
✅ **Siap digunakan untuk ethical hacking dan analisis keamanan!**  

---

## 🌐 **2. Pemindaian Jaringan dengan Scapy**  

📌 **Gunakan Scapy untuk melihat perangkat yang terhubung ke jaringan**  
```python
from scapy.all import ARP, Ether, srp

# Buat paket ARP Request
target_ip = "192.168.1.1/24"  
arp = ARP(pdst=target_ip)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = ether / arp

# Kirim paket dan dapatkan respons
result = srp(packet, timeout=3, verbose=0)[0]

# Tampilkan hasil
devices = []
for sent, received in result:
    devices.append({"IP": received.psrc, "MAC": received.hwsrc})

# Cetak daftar perangkat yang ditemukan
for device in devices:
    print(f"IP: {device['IP']}, MAC: {device['MAC']}")
```
✅ **Bisa digunakan untuk mendeteksi perangkat dalam satu jaringan!**  

---

## 🔑 **3. Enkripsi & Dekripsi Data dengan Python**  

📌 **Gunakan pustaka `cryptography` untuk mengamankan data**  
```python
from cryptography.fernet import Fernet

# Buat kunci enkripsi
key = Fernet.generate_key()
cipher = Fernet(key)

# Enkripsi pesan
pesan = "Ini adalah data rahasia"
encrypted_pesan = cipher.encrypt(pesan.encode())
print(f"Pesan terenkripsi: {encrypted_pesan}")

# Dekripsi pesan
decrypted_pesan = cipher.decrypt(encrypted_pesan).decode()
print(f"Pesan asli: {decrypted_pesan}")
```
✅ **Bisa digunakan untuk menyimpan data sensitif dengan aman!**  

---

## 🕵️ **4. Cek Kelemahan Website dengan Python**  

📌 **Gunakan `requests` untuk mendeteksi celah keamanan sederhana**  
```python
import requests

# Target URL
url = "http://example.com/login.php"

# Uji SQL Injection sederhana
payload = {"username": "admin' --", "password": "password"}
response = requests.post(url, data=payload)

# Jika berhasil login tanpa password, berarti ada celah SQL Injection
if "Welcome" in response.text:
    print("Website rentan terhadap SQL Injection!")
else:
    print("Website aman dari SQL Injection.")
```
✅ **Bisa digunakan untuk menguji keamanan website secara etis!**  

---

## 🎯 **Kesimpulan**  
✅ **Pemindaian Jaringan** → Gunakan Scapy untuk mendeteksi perangkat  
✅ **Enkripsi Data** → Gunakan `cryptography` untuk keamanan data  
✅ **Cek Keamanan Website** → Gunakan `requests` untuk uji celah keamanan  
✅ **Python sangat cocok untuk Cybersecurity!**  

**Next: Python untuk Blockchain & Cryptocurrency! ⛓️**