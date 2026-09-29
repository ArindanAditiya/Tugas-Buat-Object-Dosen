# Class Induk
class Pegawai:
    def __init__(self, id_pegawai, nama):
        self.id_pegawai = id_pegawai
        self.nama = nama

class Gaji:
    def __init__(self, gaji):
        self.gaji = gaji

class PegawaiProyek:
    def __init__(self, nama_proyek):
        self.nama_proyek = nama_proyek

# Class Anak yang mewarisi 3 Class Induk sekaligus (Multiple Inheritance)
class ProjectManager(Pegawai, Gaji, PegawaiProyek):
    def __init__(self, id_pegawai, nama, gaji, nama_proyek):
        # Memanggil __init__ dari masing-masing class induk
        Pegawai.__init__(self, id_pegawai, nama)
        Gaji.__init__(self, gaji)
        PegawaiProyek.__init__(self, nama_proyek)
    def cetakInfo(self):
        print(f"ID Pegawai  : {self.id_pegawai}")
        print(f"Nama        : {self.nama}")
        print(f"Gaji        : Rp {self.gaji:,}")
        print(f"Nama Proyek : {self.nama_proyek}")


# Inisialisasi objek
pm = ProjectManager("PM-01", "Budi Santoso", 12000000, "Sistem E-Commerce")
pm.cetakInfo()