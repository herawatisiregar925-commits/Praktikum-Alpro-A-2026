#Metode __init__ Python
class Teknik:
  def __init__(self, name, age, studyProgram, major):
    self.name = name
    self.age = age
    self.studyProgram = studyProgram
    self.major = major

p1 = Teknik("Hera", 19, "Informatika", "Elektro")

print(p1.name)
print(p1.age)
print(p1.studyProgram)
print(p1.major)

#Tanpa menggunakan __init__
class Teknik:
  pass

p1 = Teknik()
p1.name = "Hera"
p1.age = 19

print(p1.name)
print(p1.age)
