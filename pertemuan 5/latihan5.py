A = [[5, 3, 1],
[2, 8, 4],
[6, 0, 7]]

B = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]

#Menjumlahkan Matriks A dan B
print("Menjumlahkan Matriks A dan B")
def tambah_matriks(A, B): 
    if len(A) != len(B) or len(A[0]) != len(B[0]): 
        print('Error: ukuran matriks tidak sama') 
        return None 
    baris, kolom = len(A), len(A[0]) 
    hasil = [[A[i][j] + B[i][j] for j in range(kolom)] for i in 
range(baris)] 
    return hasil

C_tambah = tambah_matriks(A, B) 
for baris in C_tambah: 
    print(baris) 

print('\n\n')

#Mengurangi Matriks A dan B
print("Mengurangi Matriks A dan B")
def kurang_matriks(A, B): 
    baris, kolom = len(A), len(A[0]) 
    hasil = [[A[i][j] - B[i][j] for j in range(kolom)] for i in 
range(baris)] 
    return hasil 
 
C_kurang = kurang_matriks(A, B) 
for baris in C_kurang: 
    print(baris) 

print('\n\n')

#Mengalikan dengan Skalar 4
print("Mengalikan dengan skalar 4")
def kali_skalar(matriks, k): 
    C_skalar = [] 
    for baris in matriks: 
        baris_baru = [elemen * k for elemen in baris] 
        C_skalar.append(baris_baru) 
    return C_skalar 

C_skalar = kali_skalar(A, 4) 
for baris in C_skalar: 
    print(baris) 

print('\n\n')

#Menampilkan ketiga hasil dengan format rapi baris per baris
