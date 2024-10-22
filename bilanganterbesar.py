# Input tiga bilangan A, B, C
A = float(input("Masukkan bilangan A: "))
B = float(input("Masukkan bilangan B: "))
C = float(input("Masukkan bilangan C: "))

# Membandingkan nilai A, B, dan C untuk menentukan yang terbesar
if A > B and A > C:
    print("A adalah bilangan terbesar:", A)
elif B > C:
    print("B adalah bilangan terbesar:", B)
else:
    print("C adalah bilangan terbesar:", C)
