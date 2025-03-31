# 🧠 **Artificial Intelligence & Deep Learning dengan Python**  

AI & Deep Learning adalah cabang dari Machine Learning yang lebih kompleks, sering digunakan untuk **pengolahan gambar, suara, NLP (Natural Language Processing), dan lainnya**. Python punya banyak library powerful seperti **TensorFlow, PyTorch, dan OpenCV** buat ini!  

---

## ⚙️ **1. Install Library yang Dibutuhkan**  
```sh
pip install tensorflow keras torch torchvision opencv-python
```
📌 **`tensorflow` & `keras`** → Untuk deep learning  
📌 **`torch & torchvision`** → Untuk model AI berbasis PyTorch  
📌 **`opencv-python`** → Untuk pemrosesan gambar  

---

## 🏋️‍♂️ **2. Membuat Model Neural Network Sederhana**  

📌 **Contoh: Prediksi Angka Tulisan Tangan (MNIST) dengan TensorFlow**  
```python
import tensorflow as tf
from tensorflow import keras
import numpy as np

# Load dataset MNIST (angka tulisan tangan)
(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()

# Normalisasi data
X_train, X_test = X_train / 255.0, X_test / 255.0

# Buat model neural network
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),  # Ubah 2D jadi 1D
    keras.layers.Dense(128, activation="relu"),  # Hidden layer
    keras.layers.Dense(10, activation="softmax")  # Output layer (10 kelas angka 0-9)
])

# Compile & latih model
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
model.fit(X_train, y_train, epochs=5)  # Latih selama 5 epoch

# Evaluasi model
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"Akurasinya: {test_acc:.2f}")
```
📌 **Model ini bisa mengenali angka tulisan tangan dari dataset MNIST!** 🧠  

---

## 🖼️ **3. Computer Vision dengan OpenCV**  

📌 **Deteksi wajah pakai OpenCV**  
```python
import cv2

# Load model deteksi wajah
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Buka kamera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Ubah gambar ke grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Deteksi wajah
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Gambar kotak di wajah yang terdeteksi
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Tampilkan hasilnya
    cv2.imshow("Deteksi Wajah", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
```
📌 **Ini bakal mendeteksi wajah secara real-time dari kamera!** 🎥  

---

## 🎯 **Kesimpulan**  
✅ **TensorFlow/Keras** → Buat model AI & Deep Learning  
✅ **OpenCV** → Buat pemrosesan gambar & Computer Vision  
✅ **PyTorch** → Alternatif TensorFlow untuk AI yang lebih fleksibel  

**Next: Deployment Model AI ke Web & Mobile! 🚀**