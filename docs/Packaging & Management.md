

---

# 📦 Packaging & Distribution di Python

---

## 🎁 Apa Itu Packaging?

Packaging = proses nge-*bungkus* project Python kamu jadi bentuk yang bisa:
- Diinstall pake `pip`
- Diupload ke **PyPI** (Python Package Index)
- Dipake di mana aja, bukan cuma di laptop kamu

> Anggap aja kayak ngebungkus mi instan: udah lengkap, tinggal seduh 🍜

---

## 📁 Struktur Folder Project Ideal

```bash
nama_project/
├── src/
│   └── nama_package/
│       ├── __init__.py
│       └── modul.py
├── tests/
│   └── test_modul.py
├── pyproject.toml
├── README.md
├── LICENSE
└── setup.cfg / setup.py
```

---

## ⚙️ `pyproject.toml` (Format Modern & Recommended)

Ini file konfigurasi utama di Python modern.

### Contoh `pyproject.toml`:

```toml
[project]
name = "nama-paket-keren"
version = "0.1.0"
description = "Ini paket Python buatan saya"
authors = [
  { name="Marno", email="marno@example.com" }
]
readme = "README.md"
license = {text = "MIT"}
dependencies = ["requests"]

[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"
```

---

## 📦 Cara Build Package

### 1. Install alat build-nya:

```bash
pip install build
```

### 2. Build!

```bash
python -m build
```

> Ini akan membuat folder `dist/` berisi:
- `.tar.gz` (source archive)
- `.whl` (wheel)

---

## 🚀 Upload ke PyPI

### 1. Buat akun PyPI
> [https://pypi.org/account/register/](https://pypi.org/account/register/)

### 2. Install Twine:

```bash
pip install twine
```

### 3. Upload:

```bash
twine upload dist/*
```

💥 Sekarang semua orang bisa install package kamu dengan:

```bash
pip install nama-paket-keren
```

---

## 🧪 Test Upload ke Test PyPI Dulu

Kalau belum yakin, bisa coba di [https://test.pypi.org](https://test.pypi.org)

```bash
twine upload --repository testpypi dist/*
```

Install dari test PyPI:

```bash
pip install --index-url https://test.pypi.org/simple/ nama-paket-keren
```

---

## ✅ Tips Best Practice

- Tambahkan `__init__.py` di semua folder
- Sertakan `README.md`, `LICENSE`, `CHANGELOG.md` (biar pro)
- Gunakan folder `src/` agar import lebih aman
- Gunakan `poetry` kalau mau cara modern all-in-one
- Versi naik = ubah `version` di `pyproject.toml`!

---

## 📌 Kesimpulan

Packaging & distribusi Python gak sesulit yang kamu bayangin. Sekali ngerti alurnya, kamu bisa punya library sendiri di PyPI dalam waktu kurang dari 15 menit ⏱️🐍

> **"From localhost to PyPI, like a boss."** 💼🔥

---

### Tambahan ke `mkdocs.yml`:

```yaml
  - Packaging & Distribution: Packaging & Distribution.md
```

---

Kalau udah oke, kita lanjut ke topik selanjutnya:  
**Logging & Monitoring** atau **Security dalam Python Web Dev** — pilih yang mana dulu, chief? 🧠🔍