#TUGAS 1
def input_nilai():
    # Inisialisasi list kosong untuk menyimpan nama dan nilai
    nama = []
    nilai = []
    # Memasukkan data untuk 5 siswa
    for i in range(5):
        nama_siswa = input("Masukkan nama siswa {}: ".format(i+1))
        nilai_siswa = float(input("Masukkan nilai siswa {}: ".format(i+1)))
        nama.append(nama_siswa)
        nilai.append(nilai_siswa)
    # Menghitung total nilai dan rata-rata nilai
    total_nilai = sum(nilai)
    rata_rata_nilai = total_nilai / len(nilai)
    # Mencari nilai tertinggi dan terendah
    nilai_tertinggi = max(nilai)
    nilai_terendah = min(nilai)
    indeks_nilai_tertinggi = nilai.index(nilai_tertinggi)
    indeks_nilai_terendah = nilai.index(nilai_terendah)
    # Mencetak output
    print("")
    print("No\tNama\tNilai")
    for i in range(5):
     print("{}\t{}\t{}".format(i+1, nama[i], nilai[i]))
    print("")
    print("Jumlah Mahasiswa =", len(nama))
    print("Rata-rata nilai =", rata_rata_nilai)
    print("Nilai tertinggi =", nilai_tertinggi, "(", nama[indeks_nilai_tertinggi], ")")
    print("Nilai terendah =", nilai_terendah, "(", nama[indeks_nilai_terendah], ")")
input_nilai()



# TUGAS 2
def niai_rata_rata():
    # Input jumlah mahasiswa
    jumlah_mahasiswa = int(input("Masukkan jumlah nilai mahasiswa: "))
    # Inisialisasi variabel untuk total nilai dan jumlah mahasiswa
    total_nilai = 0
    # Perulangan untuk input nilai mahasiswa dan menghitung total nilai
    for i in range(1, jumlah_mahasiswa + 1):
      nilai_mahasiswa = float(input(f"Masukkan nilai mahasiswa ke-{i}: "))
      total_nilai += nilai_mahasiswa
    # Hitung rata-rata nilai
    rata_rata_nilai = total_nilai / jumlah_mahasiswa
    # Output rata-rata nilai
    print(f"Rata-rata nilai mahasiswa adalah: {rata_rata_nilai}")
niai_rata_rata()
 