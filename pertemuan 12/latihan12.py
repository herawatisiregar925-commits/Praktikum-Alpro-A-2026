#Struktur Folder Skripsi Hera
struktur = {
    "Skripsi_Hera": {
        "Bab_1": {
            "pendahuluan.docx": 45,
            "latar_belakang.docx": 62
        },
        "Bab_2": {
            "landasan_teori.docx": 118,
            "referensi": {
                "paper_A.pdf": 340,
                "paper_B.pdf": 210
            }
        },
        "Bab_3": {
            "metodologi.docx": 89,
            "diagram": {
                "flowchart.png": 512,
                "erd.png": 278,
                "arsitektur": {
                    "sistem.png": 430
                }
            }
        },
        "Sidang": {
            "presentasi.pptx": 2048,
            "catatan_revisi.txt": 15
        },
        "README.txt": 8
    }
}

#Tugas A: Menghitung total ukuran
def total_ukuran(folder: dict) -> int:
    total = 0

    for item in folder:
        nilai = folder[item]

        if isinstance(nilai, dict):
            total = total + total_ukuran(nilai)
        else:
            total = total + nilai

    return total

print(f"Total ukuran skripsi:", total_ukuran(struktur), "KB")

#Tugas B: Menghitung jumlah file
def hitung_file(folder: dict) -> int:
    total_file = 0

    for item in folder:
        nilai = folder[item]

        if isinstance(nilai, dict):
            total_file = total_file + hitung_file(nilai)
        else:
            total_file = total_file + 1

    return total_file

print(f"Jumlah file:", hitung_file(struktur), "File")

#Tugas C: Mencari file terbesar
def cari_terbesar(folder: dict) -> tuple:
    # Kembalikan (nama_file, ukuran_kb)
    nama_file = ""
    ukuran_kb = 0

    for nama, nilai in folder.items():
        if isinstance(nilai, dict):
            file_terbesar, ukuran_terbesar = cari_terbesar(nilai)
            if ukuran_terbesar > ukuran_kb:
                nama_file = file_terbesar
                ukuran_kb = ukuran_terbesar
        else:
            if nilai > ukuran_kb:
                nama_file = nama
                ukuran_kb = nilai

    return nama_file, ukuran_kb

nama, ukuran = cari_terbesar(struktur)
print(f"File terbesar: {nama} ({ukuran} KB)")

#Tugas D: Mencetak struktur folder
def tampilkan_tree(folder: dict, nama: str = "root", level: int = 0):
    indentasi = "    " * level 

    print(indentasi + "📁 " + nama)

    for item in folder:
        nilai = folder[item]

        if isinstance(nilai, dict):
            tampilkan_tree(nilai, item, level + 1)
        else:
            print(indentasi + "    📄 " + item + " (" + str(nilai) + " KB)")

tampilkan_tree(struktur["Skripsi_Hera"], "Skripsi_Hera")