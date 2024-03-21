#Tugas 1
# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) +1):
#         if num % i == 0:
#             return False
#     return True
# num = int(input("Masukkan sebuah bilangan bulat positif: "))

# if is_prime(num):
#     print(num, "adalah bilangan prima.")
# else:
#     print(num, "bukan bilangan prima.")
    
    

# Tugas 2
# num1 = float(input("Masukkan bilangan kedua: "))
# num2 = float(input("Masukkan bilangan kedua: "))
# operator = input("Masukkan operator (+, -, *, /): ")

# if operator == '+':
#     print("Hasil:", num1 + num2)
# elif operator == '-':
#     print("Hasil:", num1 - num2)
# elif operator == '*':
#     print("Hasil:", num1 * num2)
# elif operator == '/':
#     if num2 != 0:
#         print("Hasil:", num1 / num2)
#     else:
#         print("Error: Pembagian Nol.")
# else:
#     print("operator tidak valid")
    
 
 #tugas3   
# num = int(input("Masukkan sebuah bilangan bulat: "))
# print("Digit-digit dari bilangan", num, "adalah:")
# while num > 0:
#     digit = num %  10
#     print(digit)
#     num = num // 10



#tugas 4
# def fibonacci(n):
#     fib_series = [0, 1]
#     for i in range(2, n):
#         fib_series.append(fib_series[i-1] + fib_series[i-2])
#     return fib_series

# n = int(input("Masukkan jumlah bilangan dalam deret Fibonacci: "))
# fib_series = fibonacci(n)
# print("Deret Fibonacci hingga", n, "Bilangan pertama adalah:", ",". join(map(str, fib_series)))