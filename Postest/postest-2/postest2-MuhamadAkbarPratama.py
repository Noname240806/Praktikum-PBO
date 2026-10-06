class Wisatawan:
    def __init__(self, nama: str, id_wisatawan: str, saldo: float):
        self._nama = nama
        self.__id_wisatawan = id_wisatawan
        self._saldo = saldo

    def get_id_wisatawan(self):
        return self.__id_wisatawan

    def tampilkan_profil(self):
        return f"[{self.__id_wisatawan}] Nama: {self._nama} | Saldo: Rp{self._saldo:,.2f}"


class WisatawanReguler(Wisatawan):
    def __init__(self, nama: str, id_wisatawan: str, saldo: float, batas_bagasi_kg: int):
        super().__init__(nama, id_wisatawan, saldo)
        self.batas_bagasi_kg = batas_bagasi_kg

    def tampilkan_profil(self):
        base_info = super().tampilkan_profil()
        return f"[REGULER] {base_info} | Bagasi Max: {self.batas_bagasi_kg} kg"


class KartuAksesOrbit:
    def __init__(self, kode_kartu: str):
        self.kode_kartu = kode_kartu


class WisatawanVIP(Wisatawan):
    def __init__(self, nama: str, id_wisatawan: str, saldo: float, level_vip: int, kode_kartu: str):
        super().__init__(nama, id_wisatawan, saldo)
        self.level_vip = level_vip
        self.kartu_akses = KartuAksesOrbit(kode_kartu)

    def tampilkan_profil(self):
        base_info = super().tampilkan_profil()
        return f"[VIP Level {self.level_vip}] {base_info} | Kartu Akses: {self.kartu_akses.kode_kartu}"


class Planet:
    def __init__(self, nama_planet: str, kuota: int):
        self.nama_planet = nama_planet
        self.kuota = kuota


class PesawatPenerbangan:
    def __init__(self, nama_pesawat: str, kode_penerbangan: str):
        self.nama_pesawat = nama_pesawat
        self.kode_penerbangan = kode_penerbangan


class PaketWisataAntariksa:
    def __init__(self, nama_paket: str, harga_paket: float):
        self.nama_paket = nama_paket
        self.harga_paket = harga_paket
        self.daftar_destinasi_planet = []

    def tambah_destinasi(self, planet: Planet):
        self.daftar_destinasi_planet.append(planet)

    def proses_penerbangan(self, wisatawan: Wisatawan, pesawat: PesawatPenerbangan):
        print("\n[PROSES PENERBANGAN]")
        print(f"Wisatawan   : {wisatawan._nama}")
        print(f"Pesawat     : {pesawat.nama_pesawat} ({pesawat.kode_penerbangan})")
        print(f"Paket Tur   : {self.nama_paket}")
        print("Status      : Siap Meluncur ke Orbit!")


if __name__ == "__main__":
    print("=== ORBIT WISATA ANTARIKSA ===\n")

    akbar = WisatawanVIP("Akbar Pratama", "W-AKBAR-01", 50000000.0, 1, "CARD-VIP-999")
    keyzia = WisatawanReguler("Keyzia Putri", "W-KEYZIA-02", 15000000.0, 20)

    print(akbar.tampilkan_profil())
    print(keyzia.tampilkan_profil())
    print("-" * 65)

    p1 = Planet("Mars", 10)
    p2 = Planet("Saturnus", 5)

    paket_super = PaketWisataAntariksa("Jelajah Galaksi", 35000000.0)
    paket_super.tambah_destinasi(p1)
    paket_super.tambah_destinasi(p2)

    print(f"Destinasi Paket '{paket_super.nama_paket}':")
    for dest in paket_super.daftar_destinasi_planet:
        print(f"- Planet {dest.nama_planet} (Kuota: {dest.kuota} orang)")

    starship = PesawatPenerbangan("Starship Orbit-X", "FLIGHT-ORBIT-2026")
    paket_super.proses_penerbangan(akbar, starship)