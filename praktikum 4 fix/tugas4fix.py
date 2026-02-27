#Tugas Algoritma Pemrograman 3
class NamaError(Exception):
    def __init__(self, nama, message):
        self.nama = nama
        super().__init__(message)

class NamaTerlaluPendek(NamaError):
    def __init__(self, nama):
        super().__init__(nama, " Nama terlalu pendek nih! Minimal 3 karakter ya.")


class UmurError(Exception):
    def __init__(self,umur, message):
        self.umur = umur
        super().__init__(message)

class UmurTidakvalid(UmurError):
    def __init__(self, umur):
        super().__init__(umur," Umur hanya mengandung angka ya!")

class UmurTidakMencukupi(UmurError):
    def __init__(self, umur):
        super().__init__(umur," Umur tidak memenuhi syarat (17-60 tahun).")


class EmailError(Exception):
    def __init__(self, email, message):
        self.email = email
        super().__init__(message)

class EmailTidakValid(EmailError):
    def __init__(self, email):
        super().__init__(email, " Email tidak valid nih! Harus mengandung '@'. ")

class EmailOverAt(EmailError):
    def __init__(self, email):
        super().__init__(email, "Email hanya boleh mengandung satu '@' saja, Jangan over ya.")


class NomorHpError(Exception):
    def __init__(self, nomor, message):
        self.nomor = nomor
        super().__init__(message)

class NomorHpAngka(NomorHpError):
    def __init__(self, nomor):
        super().__init__(nomor, " Nomor HP hanya boleh mengandung angka saja.")

class NomorHpInvalid(NomorHpError):
    def __init__(self, nomor):
        super().__init__(nomor, " Nomor HP tidak valid nih! Harus 10 -13 digit angka.")

def check_nama(nama):
    if len(nama) < 3:
            raise NamaTerlaluPendek(nama)
    return True
    
def check_umur(umur):
    if not umur.isdigit():
        raise UmurTidakvalid(umur)
    umur = int(umur)
    if umur < 17 or umur > 60 :
        raise UmurTidakMencukupi(umur)

def check_email(email):
    if '@' not in email:
        raise EmailTidakValid(email)
    if email.count("@") > 1:
        raise EmailOverAt(email)

def check_nomor_hp(nomor):
    if not nomor.isdigit():
        raise NomorHpAngka(nomor)
    if len(nomor) < 10 or len(nomor) > 13:
        raise NomorHpInvalid(nomor)
    

print("=== REGISTRASI PESERTA SEMINAR ===")
while True:
    try:
        nama = input("Nama Lengkap : ")
        namaValid = check_nama(nama)
    except NamaError as ne:
        print(f"  [ERROR] {ne}")
    else:
        break

while True:
    try:
        umur = input("Umur         : ")
        umurValid = check_umur(umur)
    except UmurError as ue:
        print(f"  [ERROR] {ue}")
    else:
        break

while True:
    try:
        email = input("Email        : ")
        emailValid = check_email(email)
    except EmailError as ee:
        print(f"  [ERROR] {ee}")
    else:
        break

while True:
    try:
        nomor = input("Nomor HP     : ")
        nomorValid = check_nomor_hp(nomor)
    except NomorHpError as nhp:
        print(f"  [ERROR] {nhp}")
    else:
        break
    finally:
        print("Proses input selesai.\n")

print(f"""=== DATA PESERTA ===
Nama   : {nama}
Umur   : {umur}
Email  : {email}
No HP  : {nomor}
Status : TERDAFTAR""")
