"""
Semua sintaksis dasar bahasa pemrograman terdiri dari:
1. Sekuensial: Langkah berurutan
2. Percabangan: Langkah melompat jika kondisi terpenuhi
3. Perulangan: Mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""

# Sequential
print('Ibu berkata,"Pergi ke toko"')
print('Budi menjawab, "Baik, apa yang harus dibeli"')
print('Ibu menjawab, "Beli satu botol susu dan beli 6 jika ada telur"')
print("Maka Budi berangkat ke toko")
print("Dan mulai berbelanja")

# percabangan
jumlah_botol_susu = 6

if jumlah_botol_susu > 0:
    print("Budi mengecek harganya, dan ternyata uangnya cukup")
    print("Budi membeli 1 botol susu")
else:
    print("Budi tidak jadi membeli 1 botol susu")

print("Budi pulang ke rumah")
print("Menyerahkan hasilnya kepada ibu")

# percabangan2
jumlah_botol_susu = 60
jumlah_telur = 100
print(f"Jumlah Botol Susu {jumlah_botol_susu} botol")
print(f"Jumlah Telur {jumlah_telur} butir")

if jumlah_botol_susu > 0:
    print("Budi mengecek harganya, dan ternyata uangnya cukup")
    if jumlah_telur == 0:
        print("Budi membeli 1 botol susu")
    else:
        print("Budi membeli 1 botol susu & 6 butir telur")
else:
    print("Budi tidak jadi membeli 1 botol susu")

print("Budi pulang ke rumah")
print("Menyerahkan hasilnya kepada ibu")