import random
print("Bilangan acak yang lebih kecil dari 0,5 ")

n = int( input("Masukan nilai: "))
i = 0
while i in range(n):
    i += 1
    random_number = random.uniform(0,0.5)
    print("Bilangan ke :", i, " : ", random_number)