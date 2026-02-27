#Python fuction
#Memanggil fungsi
def hello_world():
  print("Halo Dunia!")

hello_world() #Manggil fungsinya

def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))   #Dengan fungsi, kode dapat digunakan kembali

#Nilai kembalian
def halo_dunia():
  return "Hello world!!"

pesan = halo_dunia()
print(pesan)

#Gunakan pass
def halo_dunia():
  pass     #fungsi tidak boleh kosong, jika perlu membuat placeholder fungsi tanpa kode apa pun gunakan pernyataan "pass"

#Python Arrguments
def my_function(name): # name adalah parameter
  print("Hello", name)

my_function("Herawati") # "Herawati" adalah argumen

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Herawati", "Siregar")   #Memiliki dua argumen

#Nilai Parameter Default
def my_function(kota = "Panam"):
  print("Saya dari kota", kota)

my_function("Marpoyan")
my_function("Perawang")
my_function()
my_function("Rumbai")

#Argumen Kata Kunci
def my_function(hewan, nama):
  print("Saya punya seekor", hewan)
  print("Nama", hewan + "nya adalah", nama)

my_function(hewan = "singa", nama = "Leon")

#Argumen Posisional
def my_function(hewan, nama):
  print("Saya punya seekor", hewan)
  print("Nama", hewan + "nya adalah", nama)

my_function(hewan = "singa", nama = "Leon")

#Mencampur Argumen Posisi dan Argumen Kata Kunci
def my_function(hewan, nama, umur):
  print("Saya punya seekor", hewan, "bernama", nama, "berumur", umur, "tahun")

my_function("kuda", nama = "rudy", umur = 14)

#Meneruskan Berbagai Tipe Data
def my_function(buah):
  for buah in buah:
    print(buah)

my_buah = ["nanas", "mangga", "apel"]
my_function(my_buah)

#Nilai Kembalian
def my_function(x, y):
  return x + y

result = my_function(10, 2)
print(result)

#Mengembalikan Tipe Data yang Berbeda
#Fungsi yang mengembalikan sebuah list:
def my_function():
  return ["mangga", "jeruk", "anggur"]

buah = my_function()
print(buah[0])
print(buah[1])
print(buah[2])

#Fungsi yang mengembalikan tuple:
def my_function():
  return (12, 8)

x, y = my_function()
print("x:", x)
print("y:", y)

#Argumen Khusus Kata Kunci
def my_function(*, nama):
  print("Halo", nama)

my_function(nama = "Hera")

#Menggabungkan Pencarian Berdasarkan Posisi Saja dan Pencarian Berdasarkan Kata Kunci Saja
def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)
