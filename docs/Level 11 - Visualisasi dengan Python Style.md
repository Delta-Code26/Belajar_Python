
---

## 🔥 **LEVEL 11: Visualisasi Data Panen (Python Style!)**  
> Karena data yang *cuma ditulis doang itu boring*. Tapi kalau dibikin **grafik & chart**? Langsung keliatan pola & insight-nya 📈💥

---

## 🎯 Goal:
- Buat grafik panen mingguan / bulanan
- Lihat tren produktivitas petani
- Bisa digunakan di GUI, Web Flask, atau laporan PDF

---

## 📦 Tools yang Dipakai:

| Library | Fungsi |
|--------|--------|
| `matplotlib` | Bikin grafik statik |
| `pandas` | Manipulasi data (biar gampang) |
| `seaborn` | Grafik yang lebih kece (opsional) |

---

## ⚙️ Install Dulu

```bash
pip install matplotlib pandas seaborn
```

---

## 🧪 Data Panen (Contoh)

```python
import pandas as pd

data = {
    "Tanggal": ["2024-03-01", "2024-03-02", "2024-03-03", "2024-03-04"],
    "Jumlah (kg)": [120, 150, 110, 130]
}

df = pd.DataFrame(data)
df["Tanggal"] = pd.to_datetime(df["Tanggal"])  # Biar bisa diplot sumbu X
```

---

## 📊 Basic Line Chart (Tren Panen)

```python
import matplotlib.pyplot as plt

plt.plot(df["Tanggal"], df["Jumlah (kg)"], marker='o')
plt.title("Tren Panen Sawit")
plt.xlabel("Tanggal")
plt.ylabel("Jumlah (kg)")
plt.grid(True)
plt.tight_layout()
plt.show()
```

---

## 📈 Bar Chart: Total Panen Per Petani

```python
data = {
    "Petani": ["Budi", "Tono", "Joko"],
    "Panen (kg)": [320, 280, 300]
}
df = pd.DataFrame(data)

plt.bar(df["Petani"], df["Panen (kg)"], color='green')
plt.title("Total Panen per Petani")
plt.ylabel("Jumlah (kg)")
plt.show()
```

---

## 🔥 Bonus: Pie Chart – Persentase Panen

```python
plt.pie(df["Panen (kg)"], labels=df["Petani"], autopct="%1.1f%%")
plt.title("Distribusi Panen Petani")
plt.show()
```

---

## 🧠 Simpan Grafik ke File

```python
plt.savefig("grafik_panen.png")
```

Ini bisa lo **embed di Flask web**, **masukin ke laporan**, atau bahkan **upload ke WhatsApp grup kebun** 😂

---

## 📊 Menarik Data Langsung dari MySQL

```python
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="panen_sawit"
)

query = "SELECT tanggal, jumlah_kg FROM data_panen"
df = pd.read_sql(query, db)

df["tanggal"] = pd.to_datetime(df["tanggal"])

# Plot grafik
plt.plot(df["tanggal"], df["jumlah_kg"], marker='o')
plt.title("Grafik Panen Harian")
plt.show()
```

---

## 🚀 Rangkuman Level 11

| Hal | Tools |
|-----|-------|
| Grafik statik | `matplotlib` |
| Data dari SQL | `pandas.read_sql()` |
| Line Chart | Tren dari waktu ke waktu |
| Bar Chart | Perbandingan antar petani |
| Pie Chart | Distribusi persentase |
| `.savefig()` | Simpan grafik ke file |

---

## 🤔 Bisa Digunakan Di Mana?

- GUI Tkinter (pakai canvas)
- Web Flask (embed gambar grafik)
- Export PDF
- Laporan mingguan/bulanan otomatis

---

## 🎁 Bonus Next Level (Kalau Mau):

- Embed grafik ke halaman HTML Flask (`<img src="...">`)
- Pakai **Chart.js** di browser (via Flask)
- Auto-generate laporan dengan grafik PDF (`matplotlib + fpdf`)

---
