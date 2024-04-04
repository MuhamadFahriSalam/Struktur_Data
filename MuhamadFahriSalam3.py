# TUGAS 1
def hitung_kemunculan(array, target):
    hitung = 0
    for subarray in array:
        for elemen in subarray:
            if elemen == target:
                hitung += 1
    return hitung

array = [[1, 2, 3], 
         [4, 2, 1], 
         [2, 3, 2]]

target = int(input("Masukkan angka yang ingin dicari: "))

kemunculan = hitung_kemunculan(array, target)
print(f"Jumlah Kemunculan: {kemunculan}")



# TUGAS 2
def cari_minuman(array, nama_minuman):
    for sub_array in array:
        for minuman in sub_array:
            if minuman.lower() == nama_minuman.lower():
                return minuman
    return None

array = [['Kopi', 'Susu', 'Teh'],
         ['Jus Apel', 'Jus Melon', 'Jus Jeruk'],
         ['Es Kopi', 'Es Campur', 'Es Teler']]

nama_minuman = input("Masukkan nama minuman: ")
minuman = cari_minuman(array, nama_minuman)

if minuman:
    print("Minuman ditemukan:", minuman)
else:
    print("Minuman tidak ditemukan.")
