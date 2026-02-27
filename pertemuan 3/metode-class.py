#Membuat sebuah metode dalam kelas
class Teknik:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Halooo, nama saya " + self.name)

p1 = Teknik("Hera")
p1.greet()

#Metode dengan Parameter
class Kalkulator:
  def tambah(self, a, b):
    return a + b

  def kali(self, a, b):
    return a * b

kalk = Kalkulator()
print(kalk.tambah(100, 80))
print(kalk.kali(10, 9))

#Metode mengakses Properti
class Teknik:
  def __init__(self, name, nim):
    self.name = name
    self.nim = nim

  def get_info(self):
    return f"{self.name} NIM {self.nim} Fakultas Teknik"

p1 = Teknik("Herawati Siregar", 25071206988)
print(p1.get_info())

#Metode memodifikasi sifat-sifat
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def celebrate_birthday(self):
    self.age += 1
    print(f"Happy birthday! You are now {self.age}")

p1 = Person("Hera", 20)
p1.celebrate_birthday()
p1.celebrate_birthday()

#Metode __str__
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} ({self.age})"    

p1 = Person("Yazid", 15)

print(p1)

#Berbagai Metode
class Teknik:
  def __init__(self, name, nim, major):
    self.name = name
    self.nim = nim
    self.major = major

  def printname(self):
    print(self.name)
    
  def printnim(self):
    print(self.nim)
    
  def printmajor(self):
    print(self.major)
    
  def perkenalan(self):
  	print(f"Perkenalkan nama saya {self.name}, dengan NIM {self.nim}, dari jurusan {self.major}")
    
p1 = Teknik("Hera", 25071206988, "Informatics engineering")
p2 = Teknik("Yazid", 2507110111, "Mechanical engineering")

p1.perkenalan()
p2.perkenalan()
