# def print_star_pattern():
#     for i in range(5):
#         print(' ' * (4 - i) + '*' * (2 * i + 1))
# print_star_pattern()


# def print_word():
#     for i in range(1, 6):
#         if i == 4:
#          print(f"{i}saya suka, pemrograman")
#         else:
#          print(f"{i}saya suka pemrograman")       
# print_word()


def print_h_pattern():
    for i in range(6):
        if i == 0 or i == 5:
            print('------') # Awal dan Akhir
        elif i == 1 or i == 3 or i == 4:
            print('**  *')
        else:
            print('*****')
print_h_pattern()
