

---

### 📄 **Environment Management.md**

Berikut isi lengkapnya dalam format Markdown buat kamu taruh di `docs/`:

---

# 🧪 Environment Management di Python

---

## 🤔 Kenapa Perlu Environment?

Kamu gak mau project A pake Python 3.11, tapi project B malah error karena masih stuck di 3.7 kan?  
Environment management bikin tiap project punya *dapur sendiri*, jadi gak tabrakan versi atau dependency.

---

## 1️⃣ `venv` – Built-in Virtual Environment

`venv` udah bawaan Python, simple dan cukup kuat.

### 📦 Cara Buat Virtual Env:

```bash
python -m venv env
```

> Ini bikin folder `env/` yang isinya Python environment terpisah.

### ▶️ Aktifkan Env:
- **Windows**:
  ```bash
  .\env\Scripts\activate
  ```
- **Linux/Mac**:
  ```bash
  source env/bin/activate
  ```

Kalau aktif, prompt terminal kamu akan berubah (ada `(env)`).

### ⛔ Nonaktifkan:
```bash
deactivate
```

---

## 2️⃣ `pip freeze` & `requirements.txt`

Setelah install banyak paket:

```bash
pip freeze > requirements.txt
```

Lalu bisa di-install ulang di tempat lain:

```bash
pip install -r requirements.txt
```

---

## 3️⃣ `pipenv` – Lebih Rapih & Otomatis

```bash
pip install pipenv
```

### 🚀 Mulai Project:
```bash
pipenv install requests
```

> Pipenv bakal otomatis bikin `Pipfile` dan `Pipfile.lock`  
(semacam `package.json`-nya Python)

### 🧙 Aktifkan Shell Pipenv:
```bash
pipenv shell
```

---

## 4️⃣ `poetry` – Solusi Modern & Kece Abis

```bash
pip install poetry
```

### 🔨 Buat Project:
```bash
poetry new nama_project
```

### 📦 Tambah Dependency:
```bash
poetry add numpy
```

### 🔁 Install Semua:
```bash
poetry install
```

> Poetry juga punya virtual env sendiri. Profesional banget vibes-nya.

---

## 📦 VS Code + Virtual Env

- Buka Command Palette > **Python: Select Interpreter**
- Pilih interpreter dari folder `env` atau yang dibuat Pipenv/Poetry

---

## ✅ Best Practice

- **Satu project, satu environment**
- Simpan `requirements.txt` atau `Pipfile`
- Jangan commit folder `env/`
- Gunakan tools seperti `pre-commit`, `black`, `flake8` di dalam env

---

## 💡 Tips Tambahan

| Tools     | Cocok Untuk                     |
|-----------|---------------------------------|
| `venv`    | Proyek ringan, built-in         |
| `pipenv`  | Dev yang suka simpel + locking  |
| `poetry`  | Proyek serius, publish ke PyPI  |

---

## 📌 Kesimpulan

Environment management bukan hal ribet, tapi **nyelamatin hidup** waktu dependency project mulai aneh-aneh.  
Bikin environment, commit `requirements.txt`, hidup tenang 😌🐍

---

Kalau kamu setuju, kita lanjut ke topik berikutnya. Tapi sebelumnya mau aku buatin juga `nav:`-nya?

Contoh penambahan di `mkdocs.yml`:

```yaml
  - Environment Management: Environment Management.md
```

Gas? Mau lanjut langsung ke topik berikutnya juga?