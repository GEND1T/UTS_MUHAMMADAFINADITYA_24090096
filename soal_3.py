import locale

# Set locale ke Indonesia
locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')

jumlah_barang = int(input("Masukan Jumlah Barang : "))

total_belanja = 0
for x in  range(1,jumlah_barang+1):
    nilai = int(input(f'Masukan Harga Barang Ke-{x} : '))
    total_belanja+=nilai
    
print()
print(f'Jumlah Belanjaan : {locale.currency(total_belanja, grouping=True, symbol="Rp.  ")}')
print()
