from abc import ABC, abstractmethod


class PesawatAntariksa(ABC):
    def __init__(self, nama, tarif_per_hari, kapasitas):
        self.nama = nama
        self._tarif_per_hari = tarif_per_hari
        self.__kursi_terisi = 0
        self._kapasitas = kapasitas

    @property
    def kursi_terisi(self):
        return self.__kursi_terisi

    def pesan_kursi(self):
        if self.__kursi_terisi >= self._kapasitas:
            return False
        self.__kursi_terisi += 1
        return True

    @abstractmethod
    def hitung_biaya(self, hari): ...

    @abstractmethod
    def info_misi(self): ...

    def jalankan(self, hari):
        print(f"[{self.nama}] {self.info_misi()} | "
              f"Biaya {hari} hari: ${self.hitung_biaya(hari):,}")

    def __str__(self):
        return f"{self.nama} (kapasitas {self._kapasitas})"

    def __lt__(self, other):
        return self._tarif_per_hari < other._tarif_per_hari

    def __eq__(self, other):
        return self.nama == other.nama


class PesawatOrbit(PesawatAntariksa):
    def __init__(self, nama, tarif_per_hari, kapasitas, ketinggian_km):
        super().__init__(nama, tarif_per_hari, kapasitas)
        self.ketinggian_km = ketinggian_km

    def hitung_biaya(self, hari):
        return self._tarif_per_hari * hari + 10_000

    def info_misi(self):
        return f"Orbit rendah {self.ketinggian_km} km"


class PesawatBulan(PesawatAntariksa):
    def __init__(self, nama, tarif_per_hari, kapasitas, jarak_km):
        super().__init__(nama, tarif_per_hari, kapasitas)
        self.jarak_km = jarak_km

    def hitung_biaya(self, hari):
        return int(self._tarif_per_hari * hari * 1.25)

    def info_misi(self):
        return f"Perjalanan ke Bulan {self.jarak_km:,} km"


class Invoice:
    def __init__(self, nama_turis, pesawat, hari, total):
        self.nama_turis, self.pesawat = nama_turis, pesawat
        self.hari, self.total = hari, total

    def cetak(self):
        print(f"INVOICE: {self.nama_turis} | {self.pesawat} | "
              f"{self.hari} hari | ${self.total:,}")


class JadwalPeluncuran:
    def __init__(self, daftar_tiket):
        self.daftar_tiket = daftar_tiket

    def cetak(self):
        print(f"JADWAL: {len(self.daftar_tiket)} turis siap diluncurkan")


def tampilkan(dokumen):
    dokumen.cetak()


class Turis:
    def __init__(self, nama, negara):
        self.nama = nama
        self.negara = negara


class Tiket:
    def __init__(self, turis: Turis, pesawat: PesawatAntariksa, hari):
        if not pesawat.pesan_kursi():
            raise ValueError(f"Kursi {pesawat.nama} penuh")
        self.turis = turis
        self.pesawat = pesawat
        total = pesawat.hitung_biaya(hari)
        self.invoice = Invoice(turis.nama, str(pesawat), hari, total)


class BandarAntariksa:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_pesawat = []

    def tambah(self, pesawat):
        self.daftar_pesawat.append(pesawat)


if __name__ == "__main__":
    print("=== ORBIT WISATA ANTARIKSA ===")

    print("\n--- Validasi Kelas Dasar ---")
    try:
        p = PesawatAntariksa("Test", 1000, 5)
    except TypeError as e:
        print("TypeError:", e)

    orbit = PesawatOrbit("Nova Orbit-1", 5_000, 4, 400)
    bulan = PesawatBulan("Luna Voyager", 20_000, 6, 384_400)

    bandar = BandarAntariksa("Bandar Antariksa Borneo")
    bandar.tambah(orbit)
    bandar.tambah(bulan)

    print("\n--- Paket Misi ---")
    for pesawat in bandar.daftar_pesawat:
        pesawat.jalankan(3)

    print("\n--- Perbandingan Tarif ---")
    print(orbit, "|", bulan)
    print("Orbit lebih murah dari Bulan?", orbit < bulan)
    print("Urut tarif:", [str(p) for p in sorted(bandar.daftar_pesawat)])

    print("\n--- Dokumen Perjalanan ---")
    tiket = Tiket(Turis("Budi", "Indonesia"), bulan, 3)
    for dok in (tiket.invoice, JadwalPeluncuran([tiket])):
        tampilkan(dok)