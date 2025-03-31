# 📊 **Python untuk Data Science**  

Python adalah **bahasa utama dalam Data Science** karena memiliki pustaka yang kuat untuk **analisis data, visualisasi, dan machine learning** seperti Pandas, NumPy, Matplotlib, dan Seaborn.  

---

## 🔧 **1. Instalasi & Setup Data Science di Python**  

📌 **Install pustaka yang dibutuhkan**  
```sh
pip install numpy pandas matplotlib seaborn
```
✅ **Sekarang kita siap menganalisis data!**  

---

## 📂 **2. Baca & Manipulasi Data dengan Pandas**  

📌 **Baca dataset CSV dan tampilkan informasi dasar**  
```python
import pandas as pd

# Load dataset
df = pd.read_csv("data.csv")

# Tampilkan 5 baris pertama
print(df.head())

# Cek info dataset
print(df.info())
print(df.describe())
```
✅ **Gunakan Pandas untuk mengolah data dengan mudah!**  

📌 **Menghapus kolom atau baris yang memiliki nilai kosong**  
```python
df.dropna(inplace=True)  # Hapus baris dengan nilai kosong
df.drop(columns=["KolomTidakPenting"], inplace=True)  # Hapus kolom tertentu
```
✅ **Bersihkan data sebelum dianalisis!**  

---

## 📈 **3. Visualisasi Data dengan Matplotlib & Seaborn**  

📌 **Buat grafik sederhana untuk memahami data**  
```python
import matplotlib.pyplot as plt

# Buat grafik batang
df["Kategori"].value_counts().plot(kind="bar", color="skyblue")
plt.title("Distribusi Kategori")
plt.xlabel("Kategori")
plt.ylabel("Jumlah")
plt.show()
```
✅ **Bisa memahami tren data dengan cepat!**  

📌 **Gunakan Seaborn untuk visualisasi yang lebih menarik**  
```python
import seaborn as sns

# Scatter plot hubungan antara dua variabel
sns.scatterplot(x="Pendapatan", y="Pengeluaran", data=df)
plt.title("Hubungan Pendapatan vs Pengeluaran")
plt.show()
```
✅ **Bisa melihat pola dalam dataset dengan lebih jelas!**  

---

## 📊 **4. Analisis Statistik Data**  

📌 **Hitung korelasi antar variabel untuk menemukan hubungan dalam data**  
```python
print(df.corr())  # Hitung korelasi antar kolom
```

📌 **Visualisasi korelasi dengan heatmap**  
```python
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Heatmap Korelasi")
plt.show()
```
✅ **Mengetahui hubungan antar variabel sebelum analisis lebih lanjut!**  

---

## 🎯 **Kesimpulan**  
✅ **Baca & Bersihkan Data** → Gunakan Pandas  
✅ **Visualisasi Data** → Pakai Matplotlib & Seaborn  
✅ **Analisis Statistik** → Lihat korelasi antar variabel  
✅ **Data Science Siap Dipakai!**  

**Next: Python untuk Cybersecurity! 🔐**