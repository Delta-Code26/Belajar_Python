import os

# Ambil semua file dalam folder saat ini
files = [f for f in os.listdir('.') if os.path.isfile(f)]  

# Simpan ke dalam file list.txt
with open("list.txt", "w", encoding="utf-8") as f:
    for file in files:
        f.write(file + "\n")

print("Daftar file berhasil disimpan dalam list.txt 🚀")
