# 🤖 **Data Science & Machine Learning dengan Python**  

Python adalah **raja** dalam dunia **Data Science & Machine Learning** berkat banyaknya library powerful seperti **NumPy, Pandas, Matplotlib, Scikit-learn, dan TensorFlow**. Di sini, kita bakal bahas dasar-dasarnya!  

---

## 📊 **1. Data Science: Analisis & Visualisasi Data**  

### 🔹 **Install Library yang Dibutuhkan**  
```sh
pip install numpy pandas matplotlib seaborn
```

### 🔹 **1.1 Manipulasi Data dengan Pandas**  
```python
import pandas as pd

# Buat DataFrame
data = {"Nama": ["Adit", "Budi", "Citra"],
        "Umur": [25, 30, 22],
        "Gaji": [5000000, 7000000, 4500000]}

df = pd.DataFrame(data)

print(df)  # Tampilkan tabel
```

### 🔹 **1.2 Visualisasi Data dengan Matplotlib & Seaborn**  
```python
import matplotlib.pyplot as plt
import seaborn as sns

sns.barplot(x=df["Nama"], y=df["Gaji"])
plt.title("Gaji Karyawan")
plt.show()
```
📌 **Ini akan menampilkan grafik gaji tiap karyawan!**  

---

## 🤖 **2. Machine Learning dengan Scikit-Learn**  

📌 **Install Scikit-Learn**  
```sh
pip install scikit-learn
```

### 🔹 **2.1 Contoh Prediksi Sederhana (Linear Regression)**  
```python
import numpy as np
from sklearn.linear_model import LinearRegression

# Data (Jam Belajar vs Nilai)
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([50, 55, 60, 70, 75])

# Buat Model & Latih
model = LinearRegression()
model.fit(X, y)

# Prediksi nilai jika belajar 6 jam
prediksi = model.predict([[6]])
print(f"Prediksi Nilai: {prediksi[0]:.2f}")  # Output: Prediksi nilai sekitar 80
```
📌 **Dengan Linear Regression, kita bisa memprediksi nilai berdasarkan jam belajar!**  

---

## 🎯 **Kesimpulan**  
✅ **Pandas** → Untuk manipulasi dan analisis data  
✅ **Matplotlib & Seaborn** → Untuk visualisasi data  
✅ **Scikit-Learn** → Untuk model Machine Learning  

**Next: Artificial Intelligence & Deep Learning! 🚀**