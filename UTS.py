def input_data_barang():
    # Tanyakan kepada Andi berapa banyak barang yang ingin diinput
    num_items = int(input("Masukkan jumlah barang yang ingin dibeli: "))

    # Buat kamus kosong untuk menyimpan data barang
    data_barang = {}

    # Loop melalui jumlah barang
    for i in range(num_items):
        # Tanyakan nama, harga beli, dan harga jual untuk setiap barang
        nama_barang = input(f"Masukkan nama barang ke-{i+1}: ")
        harga_beli = int(input(f"Masukkan harga beli {nama_barang}: "))
        harga_jual = int(input(f"Masukkan harga jual {nama_barang}: "))

        # Simpan data dalam kamus
        data_barang[nama_barang] = {
            "Harga Beli": harga_beli,
            "Harga Jual": harga_jual
        }

    # Cetak data untuk konfirmasi
    print("\nData barang yang dimasukkan:")
    for barang, detail in data_barang.items():
        print(f"- {barang}: Harga Beli {detail['Harga Beli']}, Harga Jual {detail['Harga Jual']}")

    return data_barang

def beli_barang(data_barang):
    total_harga = 0
    while True:
        nama_barang = input("Masukkan nama barang yang ingin dibeli (atau ketik 'selesai' untuk selesai): ")
        if nama_barang.lower() == 'selesai':
            break
        if nama_barang not in data_barang:
            print(f"Barang '{nama_barang}' tidak tersedia.")
            continue
        jumlah_barang = int(input(f"Masukkan jumlah {nama_barang} yang ingin dibeli: "))
        total_harga += jumlah_barang * data_barang[nama_barang]['Harga Jual']
        print(f"{jumlah_barang} {nama_barang} berhasil dibeli.")
    print(f"\nTotal harga belanja: {total_harga}")

# Panggil fungsi
data_barang = input_data_barang()
beli_barang(data_barang)


# def main():

#   num_bad_words = int(input("Masukan Jumlah Kata kasar yang ingin dimasukan: "))

#   bad_words = []
#   for i in range(num_bad_words):
#     word = input("Masukan Kata Kasar Ke-{}: ".format(i + 1))
#     bad_words.append(word)

#   sentence = input("Masukan Pesan (Tidak Terbatas Karakter): ")

#   found_bad_words = []
#   for word in bad_words:
#     if word.lower() in bad_words:
#       found_bad_words.append(word)

#   if len(found_bad_words) > 0:
#     print("\nJumlah Kosa Kata Kasar Sebanyak: {}".format(len(found_bad_words)))
#     print("Kata - Kata kasar Yang Digunakan:")
#     for i, bad_word in enumerate(found_bad_words, start=1):
#       print("{}. {} ".format(i, bad_word))
#   else:
#     print("Tidak ada Kata Kasar dalam Kalimat.")

# if __name__ == "__main__":
#   main()
