"""
Program perulangan membaca buku dengan while
"""
buku = 10
Jumlah_baca = 0
Jumlah_dipahami = 0

while Jumlah_baca < buku * 1:
    Jumlah_baca = Jumlah_baca + 1
    if Jumlah_dipahami == 10:
        print(f"Buku ke {Jumlah_dipahami +1} belum paham")
    else:
        Jumlah_dipahami = Jumlah_dipahami + 1
        print(f"Buku ke {Jumlah_dipahami} sudah paham")
    

print(f"Jumlah Buku yang sudah di pahami {Jumlah_dipahami}")
if Jumlah_dipahami == buku:
    print("semua buku sudah dipahami")
else:
    print(f"tidak semua dipahami.budi hanya memahamu {Jumlah_dipahami}")
#while digunakan perulangan yang tidak tertentu sampai kondisi true