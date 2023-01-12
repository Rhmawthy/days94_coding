''' pak guntur memiliki sebidang tanah berbentuk persegi panjang, di sekelilin tanah akan di tanami pohon dengan jarak antar pohon 2 meter yang di mulai dari salah satu sudutnya. jika ukuran persegi tanah merupakan inputan user dan harga setiap pohon Rp35.000.00 berapa biaya pembelian pohon seluruhnya '''

panjang = int(input("masukkan panjang tanah = "))
luas = int(input("masukkan luas tanah = "))

keliling = 2 * (panjang + luas)

''' banyak pohon yang di tanam jika jarak antar pohon 2 meter '''

banyak = keliling /2

''' biaya pembelian pohon '''

biaya = banyak * 35000

print("jumlah pembelian seluruh pohon =Rp",biaya)