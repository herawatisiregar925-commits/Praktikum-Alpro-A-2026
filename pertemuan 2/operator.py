#Operator Python
print(12 + 8)

sum1 = 100 + 100      # 200 (100 + 100)
sum2 = sum1 + 200    # 400 (200 + 200)
sum3 = sum2 + sum2   # 800 (400 + 400)

print(sum1)
print(sum2)
print(sum3)

#Operator Aritmatika
x = 20
y = 5

print(x + y)    #Menjumlah variabel (x) dan (y)
print(x - y)    #Mengurang variabel (x) dan (y)
print(x * y)    #Mengali variabel (x) dan (y)
print(x / y)    #Membagi variabel (x) dan (y)
print(x % y)    #Menampilkan sisa hasil bagi variabel (x) dan (y)
print(x ** y)   #Menghitung hasil perpangkatan dari (x) pangkat (y)
print(x // y)   #Membulatkan hasil bagi variabel (x) dan (y)

#Operator Assignments
x = 100
print(x)        #Memasukkan nilai (x = 100)

x = 8
x += 16
print(x)        #Menambahkan nilai (x += 16)

x = 10
x -= 5
print(x)        #Mengurangi nilai (x -= 5)

x = 5
x *= 10
print(x)        #Mengalikan nilai (x *= 10)

x = 100
x /= 5
print(x)        #Membagi nilai (x /= 5)

x = 20
x %= 5
print(x)        #Sisa pembagian nilai (x %= 5)

x = 18
x //= 3
print(x)        #Membulatkan hasil bagi (x //= 3)

x = 5
x **= 5
print(x)        #Perpangkatan (x **= 5)

x = 5
x &= 4
print(x)    #Ambil yang sama

x = 6
x |= 3
print(x)    #Ambil semua

x = 7
x ^= 3
print(x)    #Ambil yang beda

print(x := 9)       #Memberi nilai langsung ke variabel (x = 9)

#Operator perbandingan
x = 10
y = 5

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

x = 3
print(1 < x < 7)
print(1 < x and x < 7) #Penggabungan Operator Perbandingan

#Operator Logika
x = 7
print(x > 0 and x < 10)     #Menguji angka apakah lebih besar dari 0 dan kurang dari 10

x = 7
print(x < 7 or x > 10)      #Menguji angka apakah kurang dari 7 atau lebih besar dari 10

x = 7
print(not(x > 4 and x < 10))    #Membalikkan hasil dengan NOT

#Operator Identitas
x = ["movie", "trailer"]
y = ["movie", "trailer"]
z = x

print(x is z)
print(x is not y)
print(x == y)

#Operator Keanggotaan
fruits = ["movie", "music", "bioskop"]

print("bioskop" in fruits)
print("maps" not in fruits)
print("Movie" in fruits)

#Operator Bitwise
print(7 & 3)
print(7 | 3)
print(7 ^ 3)
print(~3)

#Operator Prioritas
#1 () Tanda Kurung
#2. ** Perpangkatan
#3. +x -x ~x Plus unary, minus unary, dan NOT bitwise
#4. * / // % Perkalian, pembagian, pembagian lantai, dan modulus
#5. + - Penjumlahan dan pengurangan
#6. << >> Pergeseran bitwise kiri dan kanan
#7. & AND bitwise
#8. ^ XOR bitwise
#9. | OR bitwise
#10. == != > >= < <= adalah adalah bukan di bukan di Operator perbandingan, identitas, dan keanggotaan
#11. not NOT Logis
#12. dan AND
#13. atau OR