#While Loops
i = 1
while i < 10:     #Perhitungan hanya kurang dari angka 10
  print(i)
  i += 1

#The break Statement
i = 1
while i < 10:
  print(i)
  if (i == 7):      #Perhitungan hanya sampai angka 7
    break
  i += 1

#The continue Statement
i = 1
while i < 7:
  i += 1
  if i == 4:		#angka 4 hilang dalam hasilnya
    continue
  print(i)

#The else Statement
i = 1
while i < 7:
  print(i)
  i += 1
else:
  print("i tidak kurang dari 7")