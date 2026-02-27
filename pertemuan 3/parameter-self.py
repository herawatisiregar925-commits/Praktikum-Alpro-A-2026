#Parameter self
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
    
p1 = Teknik("Hera", 25071206988, "Informatics engineering")
p2 = Teknik("Yazid", 2507110111, "Mechanical engineering")

p1.printname()
p1.printnim()
p1.printmajor()
p2.printname()
p2.printnim()
p2.printmajor()