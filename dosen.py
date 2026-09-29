# Class Dosen

class Dosen :
  def __init__(self, nama, NID, prodi, fakultas):
    self.nama = nama
    self.NID = NID
    self.prodi = prodi
    self.fakultas = fakultas

  def tampilkanProfilDosen(self):
    print("Nama", self.nama)
    print("NID", self.NID)
    print("Prodi", self.prodi)
    print("Fakultas", self.fakultas)

  def cekProdi(self):
    prodi = self.prodi
    match prodi:
      case "TI":
        print("Teknik Informatika")
      case "SI":
        print("Sistem Informasi")
      case "TIF":
        print("Teknologi Informasi")
  
Dosen1 = Dosen("Arindan Aditiya", "2565114013", "TI", "Teknologi Informasi")
Dosen1.cekProdi()
Dosen1.tampilkanProfilDosen()
print()

Dosen2 = Dosen("Ahmad Zainal", "2595448844", "SI", "Teknologi Kesehatan")
Dosen2.cekProdi()
Dosen2.tampilkanProfilDosen()
print()

Dosen3 = Dosen("ABU Ghufron", "2589887788", "TIF", "Teknik Manipulasi")
Dosen3.cekProdi()
Dosen3.tampilkanProfilDosen()
print()
