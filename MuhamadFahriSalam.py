def nilai():
    number = int(input("Masukkan Nilai: "))
    if number % 2 == 0:
        print("Adalah Bilangann Genap.")
    else:
        print("Adalah Bilangan Ganjil.")
nilai()
    



def print_loop():
    special_numbers = [1, 3, 6, 10]
    for i in range(1, 11):
        if i in special_numbers:
            print(str(i) + " yes!")
        else:
            print(i)
print_loop()




    
