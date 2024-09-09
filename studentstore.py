#total belanja kita ganti dengan variable tb ya ges ya
#pelajar kita ganti dengan pel
#discount kita ganti dengan disc
#pajak kita ganti dengan tax
#harga setelah discount kita hanti hdc
#harga yang harus dibayar kita ganti dengan hb

tb = float(input("Masukkan total belanja anda : "))

pel = input("Apakah anda seorang pelajar? (iya/tidak) :")

if (pel == "iya"):
    disc = tb * 20/100
else :
    disc = tb * 0/100
hdc = tb - disc

tax = hdc * 5/100

hb = hdc + tax


print("Total belanja            ", tb)
print("Diskon pelajar(20%)      ", disc)
print("Harga setelah diskon     ", hdc)
print("Pajak Penjualan          ", tax)
print(f"Harga yang harus dibayar {hb:,.2f}")