"""
Program perulangan membaca buku dengan while
"""
buku = 10
Jumlah_baca = 0
Jumlah_dipahami = 0

while Jumlah_baca < buku * 2:
    Jumlah_baca = Jumlah_baca + 1
    if Jumlah_dipahami == 9:
        print(f"Buku ke {Jumlah_dipahami +1} belum paham")
    else:
        Jumlah_dipahami = Jumlah_dipahami + 1
        print(f"Buku ke {Jumlah_dipahami} sudah paham")
    

print(f"Jumlah Buku yang sudah di baca {Jumlah_dipahami} buah")
#while digunakan perulangan yang tidak tertentu sampai kondisi true