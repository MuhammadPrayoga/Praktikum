#Masukan inputan
bilangan_1 = int(input("Bilangan ke-1: "))
bilangan_2 = int(input("Bilangan ke-2: "))
bilangan_3 = int(input("Bilangan ke-3: "))

#Buat variable data
data = [bilangan_1, bilangan_2, bilangan_3]

#Menampilkan data
print("Data sebelum di urutkan :", data)
list.sort(data)
print("Data setelah di urutkan :", data)