# 🤖 **Python untuk Machine Learning**  

Python adalah bahasa utama dalam **Machine Learning (ML)** karena memiliki banyak pustaka canggih seperti **NumPy, Pandas, Scikit-Learn, TensorFlow, dan PyTorch**.  

---

## 📊 **1. Instalasi & Setup ML di Python**  

📌 **Install pustaka yang dibutuhkan**  
```sh
pip install numpy pandas scikit-learn matplotlib seaborn
```
✅ **Sekarang siap untuk mulai belajar ML!**  

---

## 📉 **2. Membuat Model Prediksi Sederhana**  

📌 **Gunakan Scikit-Learn untuk prediksi harga rumah berdasarkan luasnya**  
```python
import numpy as np
from sklearn.linear_model import LinearRegression

# Data: Luas rumah (m²) & Harga (juta)
X = np.array([[30], [50], [70], [100], [120]])  # Luas rumah
y = np.array([300, 500, 700, 1000, 1200])  # Harga rumah

# Model ML
model = LinearRegression()
model.fit(X, y)

# Prediksi harga rumah dengan luas 90m²
prediksi = model.predict([[90]])
print(f"Prediksi harga rumah 90m²: {prediksi[0]:.2f} juta")
```
✅ **Cocok untuk memahami dasar ML!**  

---

## 📊 **3. Menggunakan Dataset dengan Pandas**  

📌 **Load dataset dan analisis data dengan Pandas**  
```python
import pandas as pd

# Load dataset
df = pd.read_csv("dataset.csv")
print(df.head())  # Lihat 5 baris pertama
print(df.describe())  # Statistik data
```
✅ **Gunakan Pandas untuk manipulasi dan eksplorasi data!**  

---

## 🧠 **4. Klasifikasi Gambar dengan TensorFlow**  

📌 **Gunakan TensorFlow untuk mengenali gambar (contoh: angka 0-9)**  
```sh
pip install tensorflow keras
```

```python
import tensorflow as tf
from tensorflow import keras

# Load dataset MNIST (angka tulisan tangan)
(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()

# Normalisasi data
X_train, X_test = X_train / 255.0, X_test / 255.0

# Buat model Neural Network
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),  
    keras.layers.Dense(128, activation="relu"),  
    keras.layers.Dense(10, activation="softmax")  
])

# Compile & train model
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
model.fit(X_train, y_train, epochs=5)

# Evaluasi model
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"Akurasi model: {test_acc:.2f}")
```
✅ **Bisa mengenali tulisan tangan angka 0-9 dengan AI!**  

---

## 🎯 **Kesimpulan**  
✅ **Buat Model Prediksi** → Gunakan Linear Regression  
✅ **Eksplorasi Data** → Pakai Pandas untuk analisis dataset  
✅ **Klasifikasi Gambar** → Gunakan TensorFlow untuk AI Vision  
✅ **Deep Learning** → Buat Neural Network dengan Keras  

**Next: Python untuk Data Science! 📊**