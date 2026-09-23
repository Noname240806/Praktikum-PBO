class Planet:
    instansi = "Orbit Wisata Antariksa"
    total_planet = 0
    satuan_jarak = "AU"

    def __init__(self, nama_planet, jarak, kuota):
        self.nama_planet = nama_planet
        self.jarak = jarak
        self.__kuota = kuota
        Planet.total_planet += 1

    @property
    def kuota(self):
        return self.__kuota

    @kuota.setter
    def kuota(self, val):
        if not isinstance(val, int) or val < 0:
            raise ValueError("Kuota harus berupa angka bulat positif!")
        self.__kuota = val

    def __str__(self):
        return f"Planet: {self.nama_planet:<10} | Jarak: {self.jarak} {Planet.satuan_jarak:<2} | Kuota: {self.__kuota} orang"

    def kurangi_kuota(self, n=1):
        if n > self.__kuota:
            print(f"[-] Kuota {self.nama_planet} habis/tidak cukup.")
            return False
        if n <= 0:
            print("[-] Jumlah tidak valid.")
            return False
        
        self.__kuota -= n
        return True

    @classmethod
    def dari_dict(cls, data):
        return cls(data["nama_planet"], data["jarak"], data["kuota"])

    @classmethod
    def set_instansi(cls, nama_baru):
        cls.instansi = nama_baru

    @staticmethod
    def validasi_jarak(j):
        return isinstance(j, (int, float)) and j > 0


class Wisatawan:
    total_wisatawan = 0
    min_topup = 50000
    kategori_default = "Reguler"

    def __init__(self, nama, id_wisatawan, saldo=0):
        self.nama = nama
        self.id_wisatawan = id_wisatawan
        self.kategori = Wisatawan.kategori_default
        self.__saldo = saldo
        Wisatawan.total_wisatawan += 1

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, val):
        if not isinstance(val, (int, float)) or val < 0:
            raise ValueError("Nominal saldo tidak valid!")
        self.__saldo = val

    def __str__(self):
        return f"[{self.id_wisatawan}] {self.nama:<15} | Kategori: {self.kategori} | Saldo: Rp{self.__saldo:,}"

    def top_up(self, nominal):
        if nominal < Wisatawan.min_topup:
            print(f"[-] Gagal topup: Minimal Rp{Wisatawan.min_topup:,}")
            return
        self.__saldo += nominal
        print(f"[+] Topup berhasil: Saldo {self.nama} sekarang Rp{self.__saldo:,}")

    @classmethod
    def dari_dict(cls, data):
        return cls(data["nama"], data["id_wisatawan"], data["saldo"])

    @classmethod
    def set_min_topup(cls, nominal_baru):
        cls.min_topup = nominal_baru

    @staticmethod
    def validasi_nama(nama):
        return bool(nama and nama.strip())


class Reservasi:
    total_reservasi = 0
    biaya_admin = 25000
    mata_uang = "IDR"

    def __init__(self, wisatawan, planet, biaya_paket):
        self.wisatawan = wisatawan
        self.planet = planet
        self.biaya_paket = biaya_paket
        self.status = "Pending"
        
        Reservasi.total_reservasi += 1
        self.kode_rsv = f"RSV-{Reservasi.total_reservasi:03d}"

    @property
    def biaya_paket(self):
        return self.__biaya_paket

    @biaya_paket.setter
    def biaya_paket(self, val):
        if not isinstance(val, (int, float)) or val <= 0:
            raise ValueError("Biaya paket harus lebih dari 0!")
        self.__biaya_paket = val

    def proses(self):
        total = self.hitung_total(self.__biaya_paket, Reservasi.biaya_admin)
        
        if self.wisatawan.saldo < total:
            self.status = "Gagal (Saldo Kurang)"
            print(f"[-] Transaksi {self.kode_rsv} gagal: Saldo {self.wisatawan.nama} tidak cukup.")
            return

        if self.planet.kurangi_kuota(1):
            self.wisatawan.saldo -= total
            self.status = "Berhasil"
            print(f"[+] Reservasi {self.kode_rsv} BERHASIL! {self.wisatawan.nama} -> {self.planet.nama_planet}")

    def __str__(self):
        total_biaya = self.biaya_paket + Reservasi.biaya_admin
        return (
            f"========================================\n"
            f"            DETAIL RESERVASI            \n"
            f"========================================\n"
            f" Kode RSV  : {self.kode_rsv}\n"
            f" Nama      : {self.wisatawan.nama}\n"
            f" Destinasi : {self.planet.nama_planet}\n"
            f" Total     : Rp{total_biaya:,} {Reservasi.mata_uang}\n"
            f" Status    : {self.status}\n"
            f"========================================"
        )

    @classmethod
    def dari_data(cls, wisatawan, planet, biaya_paket):
        return cls(wisatawan, planet, biaya_paket)

    @classmethod
    def set_biaya_admin(cls, biaya_baru):
        cls.biaya_admin = biaya_baru

    @staticmethod
    def hitung_total(paket, admin):
        return paket + admin


if __name__ == "__main__":
    p1 = Planet("Mars", 1.52, 20)
    p2 = Planet.dari_dict({"nama_planet": "Saturnus", "jarak": 9.58, "kuota": 10})

    w1 = Wisatawan("Akbar Pratama", "W01", 2000000)
    w2 = Wisatawan.dari_dict({"nama": "Keyzia Putri", "id_wisatawan": "W02", "saldo": 300000})

    print(p1)
    print(p2)
    print(w1)
    print(w2)
    print("-" * 50)

    print("Isi Nama Valid? :", Wisatawan.validasi_nama("Keyzia"))
    print("Jarak Valid?    :", Planet.validasi_jarak(1.52))
    
    w2.top_up(20000)
    w2.top_up(100000)
    print("-" * 50)

    r1 = Reservasi(w1, p1, 1500000)
    r2 = Reservasi.dari_data(w2, p2, 3000000)

    r1.proses()
    print(r1)

    r2.proses()
    print(r2)

    try:
        p1.kuota = -5
    except ValueError as err:
        print(f"Error Caught: {err}")

    try:
        w1.saldo = -100000
    except ValueError as err:
        print(f"Error Caught: {err}")

    try:
        r1.biaya_paket = 0
    except ValueError as err:
        print(f"Error Caught: {err}")