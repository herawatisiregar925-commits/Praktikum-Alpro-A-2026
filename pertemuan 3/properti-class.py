#Membuat properti kelas python
class Teknik:
  def __init__(self, name, nim):
    self.name = name
    self.nim = nim

teknik1 = Teknik("Hera", 25071206988)

print(teknik1.name)
print(teknik1.nim)

#Memodifikasi nilai properti pada objek
class Teknik:
  def __init__(self, name, nim):
    self.name = name
    self.nim = nim

teknik1 = Teknik("Hera", 25071206988)

teknik1.nim = 2507110111
print(teknik1.nim)

#Menghapus nilai properti pada objek
class Teknik:
  def __init__(self, name, nim):
    self.name = name
    self.nim = nim

teknik1 = Teknik("Hera", 25071206988)

del teknik1.nim

print(teknik1.name)
print(teknik1.nim)		#nim akan error karna properti nim telah di delete

#Properti Kelas dan/atau Properti Objek
class Teknik:
  fakultas = "Teknik"  #Class property

  def __init__(self, name):
    self.name = name  #Instance property

p1 = Teknik("Hera")
p2 = Teknik("Yazid")

print(p1.name)
print(p2.name)
print(p1.fakultas)
print(p2.fakultas)
