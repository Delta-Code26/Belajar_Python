# 🔗 **Python untuk Blockchain & Cryptocurrency**  

Python banyak digunakan dalam dunia **Blockchain dan Cryptocurrency** untuk **membuat smart contract, mining, dan transaksi crypto**.  

---

## ⛏ **1. Membuat Blockchain Sederhana dengan Python**  

📌 **Gunakan `hashlib` untuk membuat sistem blockchain dasar**  
```python
import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

# Membuat blockchain
blockchain = [Block(0, "0", "Genesis Block")]

# Menambahkan blok baru
def add_block(data):
    prev_block = blockchain[-1]
    new_block = Block(len(blockchain), prev_block.hash, data)
    blockchain.append(new_block)

# Tambahkan beberapa blok
add_block("Transaksi A ke B: 5 BTC")
add_block("Transaksi B ke C: 2 BTC")

# Cetak blockchain
for block in blockchain:
    print(f"Index: {block.index}, Hash: {block.hash}, Data: {block.data}")
```
✅ **Ini adalah dasar dari teknologi blockchain yang digunakan Bitcoin!**  

---

## 💰 **2. Menggunakan API untuk Cek Harga Crypto**  

📌 **Gunakan API CoinGecko untuk mengambil harga crypto secara real-time**  
```sh
pip install requests
```

```python
import requests

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
response = requests.get(url).json()

print(f"Bitcoin: ${response['bitcoin']['usd']}")
print(f"Ethereum: ${response['ethereum']['usd']}")
```
✅ **Dapatkan harga terbaru BTC & ETH langsung dari API!**  

---

## 🔐 **3. Membuat Private & Public Key dengan Python**  

📌 **Gunakan `ecdsa` untuk membuat sistem kriptografi kunci publik**  
```sh
pip install ecdsa
```

```python
from ecdsa import SigningKey, SECP256k1

# Generate private key
private_key = SigningKey.generate(curve=SECP256k1)
public_key = private_key.get_verifying_key()

print("Private Key:", private_key.to_string().hex())
print("Public Key:", public_key.to_string().hex())
```
✅ **Dasar dari wallet cryptocurrency seperti Bitcoin & Ethereum!**  

---

## 📜 **4. Membuat Transaksi Crypto Sederhana**  

📌 **Format transaksi dengan hashing (tanpa jaringan blockchain)**  
```python
import hashlib

def create_transaction(sender, receiver, amount):
    tx_data = f"{sender}->{receiver}:{amount}"
    tx_hash = hashlib.sha256(tx_data.encode()).hexdigest()
    return {"transaction": tx_data, "hash": tx_hash}

tx = create_transaction("Alice", "Bob", 1.5)
print(tx)
```
✅ **Simulasi transaksi sederhana tanpa blockchain!**  

---

## 🎯 **Kesimpulan**  
✅ **Blockchain Dasar** → Memahami cara kerja blok & hash  
✅ **Cek Harga Crypto** → Menggunakan API CoinGecko  
✅ **Public & Private Key** → Dasar dari wallet crypto  
✅ **Simulasi Transaksi** → Cara kerja transaksi digital  

**Next: Python untuk Internet of Things (IoT)! 🌍**