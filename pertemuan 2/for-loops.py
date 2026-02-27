#For loops
movies = ["action", "music", "trailer"]
for x in movies:
  print(x) 

#Melakukan perulangan melalui sebuah string
for x in "hera":
  print(x) 

#Pernyataan Break
movies = ["music", "action", "trailer"]
for x in movies:
  print(x) 
  if x == "action":
    break
#Pernyataan Continue
movies = ["music", "action", "trailer"]
for x in movies:
  if x == "action":
    continue
  print(x) 

#Range
for x in range(3):
  print(x) 

for x in range(1, 4):
  print(x) 

for x in range(3, 50, 5):
  print(x) 

#Perulangan Bersarang (Nested loops)
adj = ["blue", "sweet", "nice"]
fruits = ["grapes", "melon", "lemon"]

for x in adj:
  for y in fruits:
    print(x, y)
