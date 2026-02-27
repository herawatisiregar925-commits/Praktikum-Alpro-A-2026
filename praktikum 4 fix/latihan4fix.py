#Soal Algoritma Pemrograman 1
angka_list = [10, 20, 30]

try :
    idx = int(input("Masukkan index (0-2) : "))
    print(f"Nilai = {angka_list[idx]}")
except ValueError :
    print("Harus berupa bilangan bulat, Jangan pakai huruf yaa!")
except IndexError :
    print("Index di luar jangkauan nih!")
finally :
    print("Selesai!!!")

#Soal Algoritma Pemrograman 2
try :
    pembilang = float(input("Masukkan angka pembilang : "))
    penyebut = float(input("Masukkan angka penyebut : "))
    hasil = pembilang / penyebut
except ValueError : 
    print("Harus berupa bilangan real ya!")
except ZeroDivisionError :
    print("Nggak bisa membagi angka dengan nol!")
except Exception as e :
    print(f"Error tidak terduga: {e}")
else:
    print(f"Hasil pembagian: {hasil}")
finally :
    print("Program berhasil yeayy!")