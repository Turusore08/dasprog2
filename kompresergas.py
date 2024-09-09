#silinder variabel sil
# warna variabel col
#gas variabel gas

sil = input("Masukkan inisial warna tabung gas  :")

if(sil == "o" or sil == "O"):
    col = "Orange"
    gas = "amonia"
    print(f"Tabung gas silinder {col} berisi gas {gas}")
elif(sil == "c" or sil == "C"):
    col = "Coklat"
    gas = "Karbon Monoksida"
    print(f"Tabung gas silinder {col} berisi gas {gas}")
elif(sil == "k" or sil == "K"):
    col = "Kuning"
    gas = "Hidrogen"
    print(f"Tabung gas silinder {col} berisi gas {gas}")
elif(sil == "h" or sil== "H"):
    col = "Hijau"
    gas = "Oksigen"
    print(f"Tabung gas silinder {col} berisi gas {gas}")
else:
    print("tidak diketahui")



