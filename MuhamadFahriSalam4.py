from tabulate import tabulate

def input_nilai():
    jumlah_siswa = int(input("Masukkan jumlah siswa: ")) # Meminta pengguna memasukkan jumlah siswa
    nama = [] # Inisialisasi list kosong untuk menyimpan nama dan nilai
    nilai = []
    for i in range(jumlah_siswa): # Memasukkan data untuk setiap siswa
        nama_siswa = input("Masukkan nama siswa {}: ".format(i+1))
        nilai_siswa = float(input("Masukkan nilai siswa {}: ".format(i+1)))
        nama.append(nama_siswa)
        nilai.append(nilai_siswa)
    total_nilai = sum(nilai) # Menghitung total nilai dan rata-rata nilai
    rata_rata_nilai = total_nilai / len(nilai)
    nilai_tertinggi = max(nilai) # Mencari nilai tertinggi dan terendah
    nilai_terendah = min(nilai)
    indeks_nilai_tertinggi = nilai.index(nilai_tertinggi)
    indeks_nilai_terendah = nilai.index(nilai_terendah)
    data = [] # Menyusun data dalam bentuk tabel
    for i in range(jumlah_siswa):
        data.append([i+1, nama[i], nilai[i]])
    print(tabulate(data, headers=["No", "Nama", "Nilai"], tablefmt="grid")) # Mencetak tabel menggunakan tabulate
    print("") # Mencetak output tambahan
    print("Jumlah Mahasiswa =", jumlah_siswa)
    print("Rata-rata nilai =", rata_rata_nilai)
    print("Nilai tertinggi =", nilai_tertinggi, "(", nama[indeks_nilai_tertinggi], ")")
    print("Nilai terendah =", nilai_terendah, "(", nama[indeks_nilai_terendah], ")")
input_nilai()


# TUGAS 2
def niai_rata_rata():
    jumlah_mahasiswa = int(input("Masukkan jumlah nilai mahasiswa: ")) # Input jumlah mahasiswa
    total_nilai = 0 # Inisialisasi variabel untuk total nilai dan jumlah mahasiswa
    for i in range(1, jumlah_mahasiswa + 1): # Perulangan untuk input nilai mahasiswa dan menghitung total nilai
      nilai_mahasiswa = float(input(f"Masukkan nilai mahasiswa ke-{i}: "))
      total_nilai += nilai_mahasiswa
    rata_rata_nilai = total_nilai / jumlah_mahasiswa # Hitung rata-rata nilai
    print(f"Rata-rata nilai mahasiswa adalah: {rata_rata_nilai}") # Output rata-rata nilai
niai_rata_rata()
 