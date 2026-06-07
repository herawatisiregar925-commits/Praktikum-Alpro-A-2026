# #Ga ada output

# f = open("contoh.txt")

# print(f.read())

# f.close()

# with open("contoh.txt", "r") as f:
#   print(f.read(5))

#   print(f.readline())
# f.close()


# import time
# with open("contoh.txt", "a") as f:
#   f.write("\n NIM: 25071206988")
  
# time.sleep(5)

# with open("contoh.txt", "w") as f:
#   f.write("Ke overwrite")

# with open("file_new.txt", "x") as f:
#   pass

import os


if os.path.exists("file_new.txt"):
    os.remove("file_new.txt")
else:
    print("file_new.txt tidak")
