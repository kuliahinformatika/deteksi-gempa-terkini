"""
Program perulangan membaca buku dengan while
"""
Jumlah_buku = 10
total_jumlah_baca = 0
Jumlah_buku_sudah_dibaca_dan_dipahami = 0

while total_jumlah_baca < Jumlah_buku * 1:
    total_jumlah_baca = total_jumlah_baca + 1
    if Jumlah_buku_sudah_dibaca_dan_dipahami == 9:
        print(f"Buku ke {Jumlah_buku_sudah_dibaca_dan_dipahami +1} belum paham")
    else:
        Jumlah_buku_sudah_dibaca_dan_dipahami = Jumlah_buku_sudah_dibaca_dan_dipahami + 1
        print(f"Buku ke {Jumlah_buku_sudah_dibaca_dan_dipahami} sudah paham")
    

print(f"Jumlah Buku yang sudah di baca {Jumlah_buku_sudah_dibaca_dan_dipahami} buah")
#while digunakan perulangan yang tidak tertentu sampai kondisi true