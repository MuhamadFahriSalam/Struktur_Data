def mahasiswa():
    mahasiswa = []
    jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa/i: "))
    for i in range(jumlah_mahasiswa):
        nama = input(f"Masukkan nama mahasiswa/i ke-{i+1}: ").capitalize()
        umur = int(input(f"Masukkan umur mahasiswa/i ke-{i+1}: "))
        mahasiswa.append({"nama": nama, "umur": umur})
    umur_target = int(input("Masukkan umur yang ingin dicari: "))
    mahasiswa_ditemukan = [mhs for mhs in mahasiswa if mhs["umur"] == umur_target]
    if mahasiswa_ditemukan:
        print("Mahasiswa/i berumur {} ditemukan:".format(umur_target))
        for mhs in mahasiswa_ditemukan:
            print("Nama: {}\nUmur: {}".format(mhs["nama"], mhs["umur"]))
    else:
        print("Tidak ditemukan mahasiswa/i dengan umur {}".format(umur_target))
mahasiswa()

