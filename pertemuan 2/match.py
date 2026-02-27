#The Python Match Statement
profesi = 1
match profesi:
  case 1:
    print("Engineer")
  case 2:
    print("Dosen")
  case 3:
    print("PNS")
  case _:                       #Nilai " _ " penting untuk menjadi kasus terakhir agar berfungsi sebagai kasus default
    print("Tidak valid")

#If Statements as Guards
 #Mengecek jumlah roda kendaraan untuk menentukan bahan bakar yang sesuai
roda = 4
bahan_bakar = "Pertamax"
match roda:
  case 1 | 2 | 3 | 4 | 5 if roda == 4:
    print("Pertamax")
  case 1 | 2 | 3 | 4 | 5 if roda == 2:
    print("Pertalite")
  case _:
    print("Tidak valid")       
roda = 2
bahan_bakar = "Pertamax"
match roda:
  case 1 | 2 | 3 | 4 | 5 if roda == 4:
    print("Pertamax")
  case 1 | 2 | 3 | 4 | 5 if roda == 2:
    print("Pertalite")
  case _:
    print("Tidak valid")
