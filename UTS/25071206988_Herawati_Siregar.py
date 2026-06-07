DAFTAR_ANGKA = [23, 67, 4, 89, 15, 42, 73, 31, 58, 9] 
# === BAGIAN A : Fungsi Inti Game ===
def tebak_angka(angka_rahasia, maks_percobaan):
    """Meminta input tebakan dari pemain secara berulang menggunakan loop."""
    angka_rahasia == DAFTAR_ANGKA
    maks_percobaan == 7
    for i in range(7):
        tebak_angka = (int(input("Masukkan angka: ")))
        if tebak_angka > DAFTAR_ANGKA:
            return "Terlalu Besar"
        elif tebak_angka < DAFTAR_ANGKA:
            return "Terlalu Kecil"
        elif tebak_angka == DAFTAR_ANGKA:
            return "Benar!"
    
    if maks_percobaan > 7:
        return "Percobaan habis"

def  hitung_skor(berhasil, sisa_percobaan):
    """"Jika pemain berhasil (berhasil = True), nilai dikembalikan sisa_percobaan * 10 
sebagai skor. Jika tidak berhasil, nilai dikembalikan  0. """

    if berhasil == True:
        skor = (sisa_percobaan * 10)
        return skor
    else:
        return 0

def main_satu_ronde(nama, nomor_ronde):
    """""Mengambil dari Daftar_angka dan menjalankan tebak_angka dan hitung_diskon dan mengembalikan dalam list"""
    nama = []
    DAFTAR_ANGKA[nomor_ronde % len(DAFTAR_ANGKA)]
    list = [nama, skor]
    skor = hitung_skor
    tebak_angka()
    hitung_skor()
    main_satu_ronde()

# === BAGIAN B : Riwayat Skor dengan Matrix 2D ===
def tampilkan_riwayat(riwayat):
    """Menampilkan data mahasiswa dalam format tabel yang rapi."""
    riwayat = []
    if not riwayat:
        print("\n[!] Belum ada riwayat!!!")
        return

    print("\n" + "="*45)
    print(f"{'Nomor':<15} | {'Nama':<10} | {'Skor':<10}")
    print("-" * 45)
    
    #Matrix 2D
    for baris in riwayat:
        nomor = baris[0]
        nama = baris[1]
        skor = baris[2]
        print(f"{nomor:<15} | {nama:<10} | {skor:<10}")
    print("="*45)


# === BAGIAN C : Leaderboard dengan Selection Sort ===
def selection_sort_riwayat(riwayat):
    riwayat = []
