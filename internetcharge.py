#data usage variabel n
#charge variabel ch

n = float(input("Masukkan jumlah data berlanggan    :"))
if(n > 0 and n <= 1.0):
    ch = 250
elif(n > 1.0 and n <= 2.0):
    ch = 500
elif( n > 2.0 and n <= 5.0):
    ch = 1000
elif (n > 5.0 and n <= 10.0):
    ch = 1500
else :
    ch = 2000

print(f"Harga yang anda harus bayar untuk berlanggan data {n} Gbs adalah {ch}")