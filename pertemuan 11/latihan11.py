print("Soal 1")
def linearSearch(arr, targetVal):
  for i in range(len(arr)):
    if arr[i].lower() == targetVal:
      return i
  return -1 

pasien = [
"Budi Santoso", "Siti Rahayu", "Ahmad Fauzi", "Dewi Lestari",
"Eko Prasetyo", "Fitri Handayani", "Gilang Ramadan", "Hana Pertiwi",
"Irfan Maulana", "Joko Susilo"
]


Nama_Pasien = input("Masukkan nama pasien yang dicari: ")

result = linearSearch (pasien, Nama_Pasien.lower())

if result != -1:
  print(Nama_Pasien, "Ditemukan di urutan ke- ", result + 1)
else:
  print(Nama_Pasien, " tidak ada dalam daftar hari ini.")


print('\n\n')
print("Soal 2")
def binarySearch(arr, targetVal):
  left = 0
  right = len(arr) - 1
  perbandingan = 0

  while left <= right:
    mid = (left + right) // 2

    perbandingan += 1

    if arr[mid] == targetVal:
      return [mid, perbandingan]
    if arr[mid] < targetVal:
      left = mid + 1
    else:
      right = mid - 1

  return [-1, perbandingan ]

id_karyawan = [1021, 1045, 1089, 1102, 1157, 1203, 1245, 1312, 1378, 1401, 1456, 1502, 1567, 1634, 1700]

IdKaryawan = int(input("Masukkan ID karyawan yang dicari: "))

result_id = binarySearch(id_karyawan, IdKaryawan)

if result_id[0] != -1:
  print(f"Proses perbandingan: {result_id[1]} kali")
  print(f"ID {IdKaryawan} ditemukan! Posisi ke {result_id[0]+1} dalam daftar.")
else:
  print(f"ID {IdKaryawan} tidak terdaftar sebagai karyawan.")


print('\n\n')
print("Soal 3")
rak_a = ["BK-045", "BK-012", "BK-078", "BK-033", "BK-091",
"BK-027", "BK-056"]
rak_b = ["BK-011", "BK-023", "BK-035", "BK-047", "BK-059",
"BK-071", "BK-083", "BK-095"]

codeBuku = input("Masukkan kode buku yang dicari: ")


print("Mencari di Rak A (Linear Search)...")
result_linear = linearSearch(rak_b, codeBuku)
if result_linear != -1:
  print(codeBuku," ditemukan di urutan ke- ", result_linear+1)
else:
  print(codeBuku, "tidak ditemukan di Rak A.")



print("Mencari di Rak B (Binary Search)...")
result_binary = binarySearch(rak_b, codeBuku)
if result_binary[0] != -1:
  print(f"{codeBuku} ditemukan di rak B! Posisi ke {result_binary[0]+1} di rak B")
  print(f"Proses perbandingan: {result_binary[1]} kali")
else:
  print(f" {codeBuku} tidak ditemukan di Rak B.")


# --- JAWABAN ---
# a) Mengapa binary search tidak bisa langsung digunakan di Rak A?
#    Jawab: Karena Rak A tidak terurut (unsorted). Binary search memerlukan data 
#    yang sudah terurut agar logika "bagi dua" (membandingkan nilai tengah) bisa bekerja.

# b) Jika Rak B memiliki 1.000 buku, berapa maksimal langkah binary search?
#    Jawab: Maksimal langkah ditentukan dengan logaritma basis 2 dari jumlah data.
#    log2(1000) ≈ 9.96, dibulatkan ke atas menjadi 10 langkah.

# c) Jika Rak A memiliki 1.000 buku, berapa maksimal langkah linear search?
#    Jawab: Maksimal langkah pada linear search adalah sebanyak jumlah data itu sendiri
#    (Worst Case), yaitu 1.000 langkah jika buku ada di urutan terakhir atau tidak ada.