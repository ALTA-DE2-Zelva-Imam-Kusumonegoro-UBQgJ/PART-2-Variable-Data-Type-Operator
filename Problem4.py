# Meminta input harga awal dan diskon
harga_awal = float(input("Harga awal: "))
diskon = float(input("diskon (dalam %): "))

# Menghitung harga diskon
harga_diskon = (diskon / 100) * harga_awal

# Menghitung harga akhir setelah diskon
harga_akhir = harga_awal - harga_diskon

# Menampilkan harga akhir setelah diskon
print("Harga yang harus dibayar adalah Rp. {:,.2f}".format(harga_akhir))
