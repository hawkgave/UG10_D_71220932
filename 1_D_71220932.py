print("\(^o^) Selamat datang di Kalkulator Sederhana (^o^)/")

print("Ketik 1 untuk menghitung penjumlahan.")
print("Ketik 2 untuk menghitung pengurangan.")
print("Ketik 3 untuk menghitung perkalian.")
print("Ketik 4 untuk menghitung pembagian.")
print("Ketik 5 untuk menghitung sisa hasil bagi(modulus).")
print("Ketik 6 untuk menghitung pemmangkatan.")

pil=int(input("Masukkan pilihan anda: "))
x= int(input("Masukkan bilangan Pertama : "))
y= int(input("Masukkan bilangan Kedua : "))

if (pil == 1):
   hasil = x+y
   print("hasil dari", x, "ditambahkan dengan", y, "adalah", hasil)
elif (pil == 2):
   hasil = x-y
   print("hasil dari", x, "dikurangnkan dengan", y, "adalah", hasil)
elif (pil == 3):
   hasil = x*y
   print("hasil dari", x, "dikalikan dengan", y, "adalah", hasil)
elif (pil == 4):
   hasil = x/y
   print("hasil dari", x, "dibagikan dengan", y, "adalah", hasil)
elif (pil == 5)
    hasil = x%y
    print("hasil dari", x, "dimodulus dengan", y, "adalah", hasil)
elif (pil == 6)
    hasil = x**y
    print("hasil dari", x, "dipangkatkan dengan", y, "adalah", hasil)

print("\nHasil : %d" %hasil)