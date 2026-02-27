class Film:
    def __init__(self, genre, musik, tahun):
          self.genre = genre
          self.musik = musik
          self.tahun = tahun
    
    def Film_ini(self):
     print(f"film {self.genre}, tahun {self.tahun}")


    def ubah_tahun(self, tahun):
        self.tahun = tahun
        
p1 = Film("Horor", "Seram", "2025")
p2 = Film("Romcom", "Riang", "2027")
p3 = Film("Perjuangan", "Tegang", "2028")
    
print(p1.genre)
print(p2.genre)
p1.genre = "SEDIH"
p1.ubah_tahun(1980)
print(p1.tahun)