import os
def tampilkanMenu():
    print("============================")
    print("PYTHON FILE MANAGER v1.0")
    print("============================")
    
    print("[1] Read file")
    print("[2] Write file")
    print("[3] Delete file")
    print("[0] Exit")
    print("------------------------------")

    pilih = int(input("Pilih Menu: "))
    return pilih

def tampilkanFile():
    print("File tersedia: ")
    print("[1] catatan.txt")
    print("[2] tugas.txt")
    print("[3] jadwal.txt")

def selectFile():
    print("File tersedia: ")
    print("[1] catatan.txt")
    print("[2] tugas.txt")
    print("[3] jadwal.txt")

    pilih = int(input("Pilih file (nomor): "))
    return pilih

def pilihFileWr():
    print('------------------------------')
    print('File tersedia:')
    print('[1] catatan.txt')
    print('[2] tugas.txt')
    print('[3] jadwal.txt')
    print('Ketik [0] untuk membuat file baru!')


    pilih = int(input('Pilih file (nomor): '))
    return pilih

def creatFile(file):
    with open(file, 'x') as f:
        f.write(input(f'Masukkan isi file baru kamu: '))

def writeFile(file):
    with open(file, "a") as f:
        f.write(input(f"Masukkan catatan kamu: "))

def deleteFile(file):
    if os.path.exists(file):
        confirm = input("Kamu beneran mau hapus? (y/n) ")
        if confirm == "y":
            os.remove(file)
    else:
        print("file tidak ada")

def readFile(file):
    print("---isi {file}---")
    with open(file) as f:
        print(f.read())


def main():
    while True :
        pilihMenu = tampilkanMenu()
        match pilihMenu :
            case 1 :
                pilihanFileRead =  selectFile()

                match pilihanFileRead :
                    case 1 :
                        readFile('catatan.txt')
                    case 2 : 
                        readFile('tugas.txt')
                    case 3 :
                        readFile('jadwal.txt')

            case 2 :
                pilihanFileWrite =  selectFile()
           
                match pilihanFileWrite :
                    case 1 :
                        writeFile('catatan.txt')
                    case 2 : 
                        writeFile('tugas.txt')
                    case 3 :
                        writeFile('jadwal.txt')
                    case 0:
                        namaFile = input("Masukkan file baru kamu: ")
                        creatFile(namaFile)
        
            case 3 :
                pilihanFileDelete =  selectFile()

                match pilihanFileDelete : 
                
                    case 1 :
                        deleteFile('catatan.txt')
                    case 2 : 
                        deleteFile('tugas.txt')
                    case 3 :
                        deleteFile('jadwal.txt')
            case 0 :
                break
        print('------------------------------')


main()