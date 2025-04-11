

---

# 📋 Logging & Monitoring dalam Python

---

## 🧠 Kenapa Harus Logging?

Tanpa logging, ngedebug app itu kayak nyari kunci di hutan malam-malam.  
Dengan logging, kamu bisa:
- Tau error terjadi di mana & kapan
- Lacak perilaku pengguna atau sistem
- Monitor performa & bottleneck

> Debugging tanpa logging = Gacha 😩

---

## 🔥 Logging vs Print

```python
print("Error dong!")  # ❌
logging.error("Terjadi error")  # ✅
```

### ➕ Kelebihan `logging`:
- Bisa diatur levelnya (info, error, dsb.)
- Bisa ditulis ke file, bukan cuma terminal
- Bisa terstruktur rapi & format custom

---

## ⚙️ Dasar Logging di Python

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

logging.debug("Ini debug info (jarang tampil)")
logging.info("Aplikasi jalan")
logging.warning("Cie warning")
logging.error("Ups, ada error")
logging.critical("🔥 Server meledak!")
```

---

## 📁 Logging ke File

```python
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
```

> File `app.log` bakal nyimpen semua log kamu secara otomatis

---

## 🔀 Level-Level Logging

| Level      | Kegunaan                            |
|------------|-------------------------------------|
| DEBUG      | Info super detail (dev mode)        |
| INFO       | Info biasa (misal: server jalan)    |
| WARNING    | Sesuatu gak normal tapi gak fatal   |
| ERROR      | Terjadi error, tapi app masih jalan |
| CRITICAL   | Error fatal, app bisa mati          |

---

## 🧠 Logging Modular: Gunakan Logger Per File

```python
# di file modul.py
logger = logging.getLogger(__name__)
logger.warning("Log dari modul")
```

---

## 📡 Monitoring (Level Lanjutan)

Untuk **real-time monitoring**, kamu bisa integrasi Python dengan:

### 🔧 Tools Populer:

| Tool              | Fungsi                          |
|-------------------|---------------------------------|
| **Sentry**        | Error tracking, stack trace, dll |
| **Prometheus + Grafana** | Metrics dan visualisasi       |
| **Logstash + Kibana (ELK)** | Analisis log skala gede     |
| **New Relic / Datadog** | APM dan observability menyeluruh |

### 📦 Contoh Integrasi dengan Sentry

```bash
pip install sentry-sdk
```

```python
import sentry_sdk

sentry_sdk.init(
    dsn="https://publickey@o0.ingest.sentry.io/0",
    traces_sample_rate=1.0
)
```

> Semua error uncaught akan otomatis dikirim ke dashboard Sentry

---

## ✅ Best Practices Logging

- Jangan pakai `print()` di production!
- Simpan log penting di file atau layanan logging
- Gunakan format standar + timestamp
- Jangan log data sensitif (password, token, dll)
- Level log = sesuaikan sama kebutuhan (debug di dev, warning/error di prod)

---

## 📌 Kesimpulan

**Logging itu seperti CCTV buat aplikasi kamu**  
Tanpa logging? Blind spot everywhere 😵‍💫  
Dengan logging? Semua kejadian terekam, kamu tinggal playback dan fix 💪

---

### Tambahan ke `mkdocs.yml`:

```yaml
  - Logging & Monitoring: Logging & Monitoring.md
```

---

Kalau udah sip, kita bisa lanjut ke next topic! Pilihan selanjutnya:
- 🔐 Security dalam Python Web Dev
- 🧪 Python untuk Automation & Scripting
- ⚡ Performance Tuning & Profiling  
Kamu pilih yang mana, sensei Python? 🐍✨