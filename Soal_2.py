tahun = int(input('Masukan Tahun : '))

kabisat = tahun%4

if kabisat==0:
    print (f'Tahun {tahun} merupakan TAHUN KABISAT')
else:
    print (f'Tahun {tahun} bukan TAHUN KABISAT')
    
