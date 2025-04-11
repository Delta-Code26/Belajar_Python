

---

# 🎨 Design Patterns di Python

---

## 🧠 Apa Itu Design Pattern?

Design Pattern = solusi generik untuk masalah umum dalam pemrograman.

Bukan aturan saklek, tapi lebih kayak *template pemikiran*:
> "Kalau nemu masalah X, bisa pakai pola Y"

---

## 📚 Tiga Kategori Utama

| Kategori         | Fokusnya                                |
|------------------|------------------------------------------|
| **Creational**   | Cara membuat objek                       |
| **Structural**   | Cara nyusun objek & class                |
| **Behavioral**   | Cara objek berkomunikasi                 |

---

## 🛠️ 1. Singleton Pattern

🧃 *"Satu class, satu objek. Titik."*

**Gunanya:** Pastikan hanya ada satu instance dari sebuah class.  
**Contoh:** Koneksi DB, konfigurasi global

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
```

---

## 🏭 2. Factory Pattern

🏭 *"Client gak tau class mana yang dipakai. Cuma request, langsung jadi."*

**Gunanya:** Buat objek tanpa tahu class-nya secara eksplisit

```python
class Animal:
    def speak(self): pass

class Cat(Animal):
    def speak(self): return "Meow"

class Dog(Animal):
    def speak(self): return "Woof"

def animal_factory(type):
    return Cat() if type == "cat" else Dog()
```

---

## 🧱 3. Builder Pattern

🧩 *"Bangun objek step-by-step, bukan sekaligus."*

**Gunanya:** Untuk objek kompleks yang punya banyak bagian atau konfigurasi

```python
class BurgerBuilder:
    def __init__(self):
        self.ingredients = []

    def add_cheese(self):
        self.ingredients.append("cheese")
        return self

    def add_lettuce(self):
        self.ingredients.append("lettuce")
        return self

    def build(self):
        return f"Burger with {' & '.join(self.ingredients)}"

burger = BurgerBuilder().add_cheese().add_lettuce().build()
```

---

## 🪢 4. Adapter Pattern

🔌 *"Jembatan antara dua sistem yang gak kompatibel."*

**Gunanya:** Bikin dua class beda struktur bisa kerja bareng

```python
class OldPrinter:
    def print_text(self):
        return "Mencetak..."

class NewPrinter:
    def print(self):
        return "Printing..."

class PrinterAdapter:
    def __init__(self, printer):
        self.printer = printer

    def print(self):
        return self.printer.print_text()

printer = PrinterAdapter(OldPrinter())
printer.print()
```

---

## 👁️ 5. Observer Pattern

🔔 *"Kalau satu objek berubah, semua follower dikabarin."*

**Gunanya:** Cocok buat event-driven programming

```python
class Publisher:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, sub):
        self.subscribers.append(sub)

    def notify(self, message):
        for sub in self.subscribers:
            sub.update(message)

class Subscriber:
    def update(self, msg):
        print(f"Notif: {msg}")

pub = Publisher()
sub1 = Subscriber()
pub.subscribe(sub1)
pub.notify("Ada update baru!")
```

---

## 🚦 6. Strategy Pattern

🎭 *"Ganti-ganti algoritma di runtime, tanpa ubah class utama."*

**Gunanya:** Misalnya sorting yang bisa diganti-ganti

```python
class BubbleSort:
    def sort(self, data): return "Bubble Sorted"

class QuickSort:
    def sort(self, data): return "Quick Sorted"

class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def sort_data(self, data):
        return self.strategy.sort(data)

ctx = Context(QuickSort())
ctx.sort_data([5, 2, 1])
```

---

## 🧠 Best Practices

- Pakai pattern **kalau memang butuh**  
- Jangan terlalu memaksakan (anti "Over-Engineering")
- Pelajari pattern dari **problem-nya**, bukan dari teorinya doang
- Bisa dikombinasikan sesuai kebutuhan

---

## 📌 Kesimpulan

Design Pattern bikin kodenya:
- Lebih **rapi**
- Lebih **terstruktur**
- Lebih **siap berkembang**

> "Pattern itu kayak jurus ninja — keliatan keren, tapi yang penting efektif!" 🥷🐍

---

### Tambahan ke `mkdocs.yml`:

```yaml
  - Design Patterns di Python: Design Patterns di Python.md
```

---

Lanjut yuk ke topik berikutnya?  
Mau bahas:
- ⚙️ Performance Tuning & Profiling  
- 🧑‍💻 Automation & Scripting  
- 🤯 Python Async & Concurrency  
Atau kamu mau request topik di luar list? Gue siapin juga! 💪