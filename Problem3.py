# Mendefinisi constant, pi sebagai 3.14
pi = 3.14

# Meminta input dari pengguna untuk radius (r) dan tinggi (T)
height = float(input("Masukkan tinggi tabung (T): "))
radius = float(input("Masukkan jari-jari tabung (r): "))

# Menghitung luas permukaan tabung
luas_permukaan_tabung = 2 * pi * radius * (radius + height)


# Menampilkan hasil
print(f"Luas permukaan tabung adalah {luas_permukaan_tabung}.")
