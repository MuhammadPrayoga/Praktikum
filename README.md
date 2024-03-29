## Tugas Struktur Kondisi
## Latihan 1
*Buat program sederhada dengan input 2 buah bilangan, kemudian
tentukan bilangan terbesar dari kedua bilangan tersebut
menggunakan statement if.*

![gambar](gambar/g1.png)

#### Hasil program
![gambar](gambar/ss1.png)

### Latihan 2

*Buat program untuk mengurutkan data berdasarkan input sejumlah
 data (minimal 3 variable input atau lebih), kemudian tampilkan
 hasilnya secara berurutan mulai dari data terkecil.*

 ![gambar](gambar/g2.png)

 `list.sort` Syntax ini berfungsi untuk mengurutkan data

 #### Hasil program
 ![gambar](gambar/ss2.png)


 ## Tugas perulangan
### Latihan 1

*Buat program dengan perulangan bertingkat (nested) for yang 
menghasilkan output sebagai berikut:*

![gambar](gambar/g3.png)

1. Pendeklarasian variable
```python
baris = 10
kolom = baris
```
2. Untuk perulangan baris dan kolom menggunakan `for`
```python
for b in range(baris):
    for k in range(kolom):
        tab = b+k
``` 
3. Untuk menampikan hasil dari perulangan
     * Agar terlihat rapih menggunakan `format string` rata ke kanan sebanyak 5 karakter
     * Agar tidak membuat baris baru menggunakan `end=''` (baris)
```python
  print("{0:>5}".format(tab), end='')
print()    
```
#### Hasil program
![gambar](gambar/ss3.png)

### Latihan 2

*Tampilkan n bilangan acak yang lebih kecil dari 0.5.* 
*nilai n diisi pada saat runtime*
*anda bisa menggunakan kombinasi while dan for untuk
 menyelesaikannya.*

 ![gambar](gambar/g4.png)

 #### Hasil program
 ![gambar](gambar/ss4.png)

- `import random` Untuk membuat bilangan acak
- `n = int(input("Masukan nilai: "))` Menentukan jumlah input & di konversikan dalam bilangan bulat-dimasukan ke variable `n`
- `while i in range(n)` Pengulangan
- Menampilkan urutan sesuai inputan dengan hasil di bawah 0.5
```python
random_number = random.uniform(0,0.5)
    print("Bilangan ke :", i, " : ", random_number)
```

## Tugas Modul praktikum 2
### Latihan 1

*Buat program sederhana dengan input tiga buah bilangan, dari ketiga bilangan
 tersebut tampilkan bilangan terbesarnya. Gunakan statement if.*

 ![gambar](gambar/g5.png)

 - a,b,c sebagai inputan 
- `max = a` Dekralasi variable
- `if` jika b lebih besar dari a/max, maka max = a
- `if` jika c lebih besar dari a/max, maka max = c

### Flowchart
![gambar](gambar/flowchart.png)

#### Hasil program
![gambar](gambar/ss5.png)

