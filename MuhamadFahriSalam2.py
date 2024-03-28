merk = input('Masukkan merk: ')
lengan = input('Masukkan panjang lengan: ')

if merk.lower() == 'a':
    if lengan.lower() == 'lengan pendek':
        print('Harga: Rp 80.000')
    elif lengan.lower() == 'lengan panjang':
        print('Harga: Rp 87.000')
    else:
        print('Barang tidak ditemukan')
        
elif merk.lower() == 'b':
    if lengan.lower() == 'lengan pendek':
        print('Harga: Rp 75.000')
    elif lengan.lower() == 'lengan panjang':
        print('Harga: Rp 80.000')
    else:
        print('Barang tidak ditemukan')
else:
    print('Barang tidak ditemukan')
    
    
    
    
    