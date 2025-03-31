# 🌍 **Python untuk Internet of Things (IoT)**  

Python sering digunakan dalam **IoT (Internet of Things)** untuk mengontrol sensor, perangkat pintar, dan mengolah data dari hardware seperti **Raspberry Pi, Arduino, dan ESP8266**.  

---

## 📡 **1. Membaca Data Sensor dengan Raspberry Pi**  

📌 **Gunakan `gpiozero` untuk membaca sensor suhu**  
```sh
pip install gpiozero
```

```python
from gpiozero import MCP3008
import time

sensor = MCP3008(channel=0)  # Menghubungkan sensor ke channel 0

while True:
    suhu = sensor.value * 100  # Konversi ke suhu
    print(f"Suhu: {suhu:.2f}°C")
    time.sleep(1)
```
✅ **Bisa digunakan untuk proyek Smart Home!**  

---

## 📶 **2. Mengontrol LED dengan Raspberry Pi & Python**  

📌 **Gunakan `RPi.GPIO` untuk menyalakan/mematikan LED**  
```python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

# Nyalakan & Matikan LED setiap 1 detik
while True:
    GPIO.output(18, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(18, GPIO.LOW)
    time.sleep(1)
```
✅ **Bisa dikembangkan menjadi sistem IoT otomatis!**  

---

## 🌐 **3. Mengirim Data Sensor ke Cloud (MQTT Protocol)**  

📌 **Gunakan MQTT (`paho-mqtt`) untuk komunikasi IoT ke Cloud**  
```sh
pip install paho-mqtt
```

```python
import paho.mqtt.client as mqtt

broker = "mqtt.eclipseprojects.io"
topic = "sensor/suhu"

client = mqtt.Client()
client.connect(broker, 1883, 60)

# Kirim data suhu ke MQTT Broker
client.publish(topic, "Suhu sekarang: 30°C")
print("Data dikirim!")
```
✅ **Bisa digunakan untuk menghubungkan IoT dengan aplikasi berbasis cloud!**  

---

## 📲 **4. Mengontrol Perangkat IoT dari HP dengan Flask API**  

📌 **Gunakan Flask untuk membuat API sederhana yang bisa dikontrol dari HP**  
```sh
pip install flask
```

```python
from flask import Flask

app = Flask(__name__)

@app.route("/led/on")
def led_on():
    return "LED menyala!"

@app.route("/led/off")
def led_off():
    return "LED mati!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```
✅ **Bisa diakses dari HP untuk mengontrol perangkat IoT!**  

---

## 🎯 **Kesimpulan**  
✅ **Baca Data Sensor** → Gunakan `gpiozero` untuk membaca sensor suhu  
✅ **Kontrol Perangkat IoT** → Gunakan `RPi.GPIO` untuk menyalakan LED  
✅ **Kirim Data ke Cloud** → Gunakan MQTT untuk komunikasi IoT  
✅ **Buat API IoT** → Gunakan Flask untuk kontrol dari HP  

**Next: Python untuk Game Development! 🎮**