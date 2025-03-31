# 🚀 **Deployment Model AI ke Web & Mobile**  

Setelah bikin model AI, langkah selanjutnya adalah **deploy** supaya bisa digunakan oleh aplikasi web atau mobile. Python bisa integrasi dengan **Flask, FastAPI, TensorFlow Serving, dan Firebase** buat menyebarkan model AI ke dunia nyata!  

---

## 🌐 **1. Deploy Model AI ke Web dengan Flask**  

📌 **Contoh: Buat API AI dengan Flask untuk Prediksi Angka Tulisan Tangan (MNIST)**  

```python
import tensorflow as tf
from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

# Load model yang sudah dilatih
model = tf.keras.models.load_model("model_mnist.h5")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["image"]  # Terima data gambar dalam bentuk array
    img = np.array(data).reshape(1, 28, 28) / 255.0  # Normalisasi
    prediction = model.predict(img)
    return jsonify({"prediction": int(np.argmax(prediction))})

if __name__ == "__main__":
    app.run(debug=True)
```

📌 **Cara Pakai:**  
1. **Jalankan Flask Server**:  
   ```sh
   python app.py
   ```
2. **Kirim data gambar via API (pakai Postman atau Python Requests)**  

---

## 📱 **2. Deploy ke Mobile (Android) dengan Firebase ML Kit**  

📌 **Langkah-Langkah:**  
1. **Convert Model AI ke TensorFlow Lite (TFLite)**  
   ```python
   import tensorflow as tf

   model = tf.keras.models.load_model("model_mnist.h5")
   converter = tf.lite.TFLiteConverter.from_keras_model(model)
   tflite_model = converter.convert()

   # Simpan model
   with open("model.tflite", "wb") as f:
       f.write(tflite_model)
   ```
2. **Upload Model ke Firebase ML Kit**  
3. **Gunakan di Android Studio dengan TensorFlow Lite Interpreter**  

📌 **Keuntungannya:**  
✅ Model bisa dijalankan langsung di HP (tanpa internet)  
✅ **Lebih cepat & hemat kuota**  

---

## 🎯 **Kesimpulan**  
✅ **Flask API** → Bagus buat deploy model AI ke server web  
✅ **Firebase ML Kit** → Bagus buat deploy AI ke mobile apps  
✅ **TensorFlow Serving** → Cocok buat skala besar (enterprise-level)  

**Next: Best Practices dalam Python Programming! 🚀**