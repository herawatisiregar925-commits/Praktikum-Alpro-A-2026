#Pernyataan If
a = 20
b = 180
if b > a:
  print("b lebih besar dari a")   #Indentasi

#Menggunakan Variabel dalam Kondisi
is_password = True
if is_password:
  print("your password is correct")

#elif
nilai = 97

if nilai >= 95:
  print("Nilai: A")
elif nilai >= 85:
  print("Nilai: B")
elif nilai >= 75:
  print("Nilai: C")
elif nilai >= 65:
  print("Nilai: D")

#else
suhu = 12

if suhu > 30:
  print("Panas sekali!")
elif suhu > 20:
  print("Hangat sekali!")
elif suhu > 10:
  print("Sejuk sekali!")
else:
  print("Dingin sekali!")

#Short Hand If
a = 40
b = 70

besar = a if a > b else b
print("Besar dari", besar)      #Menetapkan nilai dengan if else

x = 90
y = 95
nilai_max = x if x > y else y
print("Nilai maksimum:", nilai_max)   #Mencari nilai maksimum dari dua bilangan

#Operator Logika
x = 7
print(x > 0 and x < 10)     #Menguji angka apakah lebih besar dari 0 dan kurang dari 10

x = 7
print(x < 7 or x > 10)      #Menguji angka apakah kurang dari 7 atau lebih besar dari 10

x = 7
print(not(x > 4 and x < 10))    #Membalikkan hasil dengan NOT

#Nested If
x = 75

if x > 50:
  print("Lebih dari 50,")
  if x > 70:
    print("dan lebih dari 70!")
  else:
    print("tetapi tidak lebih dari 70.")    #If bersarang

umur = 20
punya_sim = True

if umur >= 18:
  if punya_sim:
    print("Kamu bisa berkendara yaa!!")
  else:
    print("Kamu harus punya sim")
else:
  print("Kamu masih belum cukup umur")    #Kondisi penestingan

#Pass Statements
nilai = 95

if nilai > 90:
  pass  # Lulus ujian
print("Nilai diproses")