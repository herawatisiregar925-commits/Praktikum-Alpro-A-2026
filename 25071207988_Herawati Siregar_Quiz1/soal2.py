Menu = [["Nasi Goreng", 15000], ["Es Teh", 5000], ["Mie Goreng", 15000], ["Mie Rebus", 10000], ["Es Jeruk", 5000]]
for i in range(len(Menu)):
    print(f"{i+1} {Menu[i][0]} harga = {Menu[i][1]}")

nomorMenu =(1, 2, 3, 4, 5)
daftarPesanan = []
i = 0
while True :
    pilihan = int(input("Masukkan nomor menu:"))
    if pilihan in nomorMenu :
        print(f"{"pilihan"} {Menu[pilihan -1][0]}) harga = {Menu[pilihan -1][1]}")
        daftarPesanan.append(f"[{Menu[pilihan -1][0]} harga = [{Menu[pilihan -1][1]}")
    else:
        print("ERROR" " " "nomor menu tidak valid")
