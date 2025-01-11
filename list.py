daftar_buku = ['atlas','kamus','buku_catatan']
print(daftar_buku)

print('\nProses semua dengan for in')
for buku in daftar_buku:
    print(buku)

print('\nTampilkan isi dalam index tertentu')
print(daftar_buku[0])
print(daftar_buku[2])

print('\nTampikan dengan for range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])


#variabel list nilainya bisa sembarangan   
daftar_buku_baru = [1, 'mario wibowo 2', -313, 3.14]
print('\nTampilkan dengan for in range dengan tipe data berbeda')
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

#slicing
#menambah isi dalam list paling ujung

daftar_buku.append('sidu')
print(daftar_buku)
