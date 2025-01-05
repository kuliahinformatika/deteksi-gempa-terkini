"""
ini adalah demo project pertama dengan python
"""

# print("Hello World")
# print("My name is Hakim")
# print ("5 januari 2025")
# print("Python RWID")

"""
Semua sintaks dasar bahasa pemograan terdiri dari :
1. Sekuensial : langkah berurutan
2. Percabangan : langkah melompat jika kondisi terpenuhi
3. Perulangan : mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi 
"""
#squensial

print('ibu berkata "Pergi ke toko"')
print('budi menajawab,"ok ma, apa yang saya lakukan ditoko?"')
print('ibu berkata "belikan telur"')
print("oke ma", 'budi pergi ke toko')

#pecabangan
Jumlah_susu = 234
Jumlah_telur = 6

print(f"Jumlah botol susu adalah {Jumlah_susu} botol")
print(f"Jumlah telur adalah {Jumlah_telur} botol")

if Jumlah_susu > 0:
    print("Budi mengecek harganya, uangnya cukup")
    print("Budi membawa 1 botol susu")
    if Jumlah_telur > 0:
        print("Budi membeli 6 butir telur")
    else:
        print("Budi membeli 1 butir telur")

else:
    print("Budi tidak membeli susu")

print ("Budi pulang ke rumah")
print ("Budi menyerahkan hasil ke ibunya")
