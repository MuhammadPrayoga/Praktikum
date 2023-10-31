baris = 10
kolom = baris

for b in range(baris):
    for k in range(kolom):
        tab = b+k
        print("{0:>5}".format(tab), end='')
    print()