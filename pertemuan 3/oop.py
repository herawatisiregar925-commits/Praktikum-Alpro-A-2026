#Membuat class dan object
class Teknik:				#Class bernama Teknik
  x = 95					  #Properti/Atribut

p1 = Teknik()				#Object dari class Teknik
print(p1.x)					#Mengakses data objek


#Membuat beberapa objek dari kelas yang sama
class Teknik:				
  x = 95					

p1 = Teknik()
p2 = Teknik()
p3 = Teknik()

print(p1.x)					
print(p2.x)	
print(p3.x)	