# class induk nya yang nurunin semua class
class Kendaraan:
    def __init__(self, nama, merk, tahun, kecepatan):
        self.nama = nama
        self.merk = merk
        self.tahun = tahun
        self.kecepatan = kecepatan

# blueprint mobi
class Mobil(Kendaraan):
    def __init__(self, nama, merk, tahun, kecepatan, jumlah_kursi):
        super().__init__(nama, merk, tahun, kecepatan)
        self.jumlah_kursi = jumlah_kursi

    def cetakInfo(self):
        print(f"Nama        : {self.nama}")
        print(f"Merk        : {self.merk}")
        print(f"Tahun       : {self.tahun}")
        print(f"Kecepatan   : {self.kecepatan} km/jam")
        print(f"Jumlah kursi: {self.jumlah_kursi}")

# blueprint motor
class Motor(Kendaraan):
    def __init__(self, nama, merk, tahun, kecepatan, tipe_motor):
        super().__init__(nama, merk, tahun, kecepatan)
        self.tipe_motor = tipe_motor

    def cetakInfo(self):
        print(f"Nama       : {self.nama}")
        print(f"Merk       : {self.merk}")
        print(f"Tahun      : {self.tahun}")
        print(f"Kecepatan  : {self.kecepatan} km/jam")
        print(f"Tipe motor : {self.tipe_motor}")

# initialisasi objek
mobil = Mobil("Civic", "Honda", 2020, 200, 5)
mobil.cetakInfo()
motor = Motor("NMAX", "Yamaha", 2023, 130, "Matic")
motor.cetakInfo()