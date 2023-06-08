"""
Semua sintaksis dasar bahasa pemrograman terdiri dari:
1. Sekuensial: Langkah berurutan
2. Percabangan: Langkah melompat jika kondisi terpenuhi
3. Perulangan: Mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""

# Sequential
print('Ibu berkata,"Pergi ke toko"')
print('Budi menjawab, "Baik, apa yang harus dibeli"')
print('Ibu menjawab, "Beli satu botol susu dan jika ada telur beli 6"')
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