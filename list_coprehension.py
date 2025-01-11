daftar_buku = ['atlas','kamus','buku_catatan']
print("\nPerintah del dengan list comprehension")
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nPerintah del dengan list comperhension strat")
daftar_buku = ['atlas','kamus','buku_catatan']
del daftar_buku[0:1]#START:END
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
    
print("\nPerintah del dengan list comperhension strat")
daftar_buku = ['atlas','kamus','buku_catatan']
del daftar_buku[0::2]#START:END:STEP
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nMembuat list baru dengan comprehension : ganjil")
daftar_film = ['ajal','dilan','warkop_dki']
daftar_film_terbaru = daftar_film [:]#TANDA [:] MENGCOPY SEMUA ISI VARIABEL YANG SEBELAH KIRI KEKANAN
for i in range(0, len(daftar_film_terbaru)):
    print(daftar_film_terbaru[i])