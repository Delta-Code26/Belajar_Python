

---

# 🔐 Security dalam Python Web Development

---

## 😰 Kenapa Security Itu Penting?

Satu celah kecil = satu kerugian besar 💸  
Kalau aplikasi kamu bocor:
- Data user bisa dicuri 😱  
- Bisa kena deface / DDoS 😵  
- Bisa jadi zombie buat botnet 😐

> Pokoknya jangan jadi developer yang bikin website bocor kayak ember bolong 🪣

---

## 🚨 1. SQL Injection

**Masalah:** Query langsung dari input user  
**Solusi:** Gunakan parameterized query / ORM

**❌ Salah:**
```python
cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
```

**✅ Benar:**
```python
cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
```

ORM kayak SQLAlchemy atau Django ORM lebih aman by default.

---

## 💻 2. XSS (Cross Site Scripting)

**Masalah:** Input user ditampilkan mentah-mentah  
**Solusi:** Escape output, validasi input

Gunakan template engine (Jinja2, Django template) karena otomatis escape HTML.

```html
{{ user_input }}  <!-- aman, auto escape -->
```

---

## 🥸 3. CSRF (Cross Site Request Forgery)

**Masalah:** User login disuruh klik link jahat  
**Solusi:** Gunakan CSRF token

Contoh di Flask-WTF atau Django:
```html
<input type="hidden" name="csrf_token" value="{{ csrf_token() }}">
```

---

## 🔑 4. Authentication & Authorization

- Gunakan **JWT atau session** untuk autentikasi
- Jangan simpan password langsung!
- Gunakan **bcrypt**, **argon2**, atau **PBKDF2**

**Contoh hashing pakai bcrypt:**

```python
import bcrypt

hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
bcrypt.checkpw(password_attempt.encode(), hashed)
```

---

## 🔐 5. HTTPS Wajib!

- Jangan pernah deploy pakai HTTP doang
- Gunakan **Let's Encrypt** untuk sertifikat SSL gratis
- Akses API = selalu lewat HTTPS

---

## 🧯 6. Error Handling Aman

**❌ Salah:**
```python
return f"Error: {e}"
```

**✅ Benar:**
```python
logging.error(e)
return "Terjadi kesalahan. Coba lagi nanti."
```

> Jangan kasih clue internal ke attacker (nama tabel, trace, dll.)

---

## 🔒 7. Secure Header & CORS

Gunakan middleware atau library untuk:
- Menambahkan header seperti `X-Content-Type-Options`, `Content-Security-Policy`, dll.
- Mengatur CORS agar hanya domain tertentu yang boleh akses API

**Contoh di FastAPI:**

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## 🧪 8. Security Testing Tools

| Tool       | Fungsi                        |
|------------|-------------------------------|
| `bandit`   | Scan celah security di Python |
| `OWASP ZAP`| Uji keamanan web app          |
| `safety`   | Cek package yang rentan       |

```bash
pip install bandit
bandit -r src/
```

---

## ✅ Best Practices Security

- Jangan hardcode secrets (pakai `.env`!)
- Gunakan library yang selalu di-*maintain*
- Selalu update dependency (`pip list --outdated`)
- Logging error, tapi jangan bocorin info sensitif
- Pakai 2FA di admin panel (kalau ada)

---

## 📌 Kesimpulan

Security bukan fitur tambahan, **itu pondasi**.  
Lebih baik capek sedikit di awal, daripada nangis tengah malam karena server dibajak 🧠💻🔥

---

### Tambahan ke `mkdocs.yml`:

```yaml
  - Security dalam Python Web Dev: Security dalam Python Web Dev.md
```

---

Siap lanjut?  
Next bisa ke:
- ⚙️ Performance Tuning & Profiling  
- 🧑‍💻 Python untuk Automation & Scripting  
- 🤖 Python untuk Data Science  

Pilih topik selanjutnya, broh! 🐍🚀