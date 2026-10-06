## Deskripsi Program

Program Orbit Wisata Antariksa merupakan sistem pengelolaan reservasi wisata antarplanet berbasis Object-Oriented Programming (OOP). Sistem ini mengintegrasikan tiga entitas utama:
1. Planet: Mengelola data destinasi, jarak dari matahari, serta kuota keberangkatan.
2. Wisatawan: Mengelola profil wisatawan, keanggotaan, saldo, serta mekanisme top up.
3. Reservasi: Memproses transaksi pemesanan, menghitung total biaya termasuk administrasi, serta memperbarui kuota dan saldo secara otomatis.

---

## Penerapan Konsep OOP & Relasi UML

### 1. Inheritance (Pewarisan)
* **Superclass (`Wisatawan`)**: Menyimpan data dasar wisatawan seperti nama (`_nama`), ID wisatawan (`__id_wisatawan`), dan saldo (`_saldo`).
* **Subclass 1 (`WisatawanReguler`)**: Turunan dari `Wisatawan` yang memiliki atribut spesifik `batas_bagasi_kg`.
* **Subclass 2 (`WisatawanVIP`)**: Turunan dari `Wisatawan` yang memiliki atribut spesifik `level_vip` serta kartu akses eksklusif.
* **Penggunaan `super()`**: Dipanggil pada konstruktor subclass untuk menginisialisasi atribut dari superclass.
* **Method Overriding**: Method `tampilkan_profil()` di-override pada subclass untuk menampilkan detail spesifik tiap jenis wisatawan.
* **Access Modifier**:
  * **Protected (`_nama`, `_saldo`)**: Dapat diakses oleh superclass dan subclass.
  * **Private (`__id_wisatawan`)**: Eksklusif hanya dapat diakses di dalam class `Wisatawan`.

---

### 2. Relasi UML
* **Asosiasi (`PaketWisataAntariksa` - `PesawatPenerbangan`)**:
  Method `proses_penerbangan()` pada `PaketWisataAntariksa` menggunakan objek `Wisatawan` dan `PesawatPenerbangan` sebagai parameter untuk memproses penerbangan.
* **Agregasi (`PaketWisataAntariksa` - `Planet`)**:
  Class `PaketWisataAntariksa` menampung daftar objek `Planet` (`daftar_destinasi_planet`). Objek `Planet` dibuat secara terpisah di luar class dan tetap ada meskipun paket wisata dihapus.
* **Komposisi (`WisatawanVIP` - `KartuAksesOrbit`)**:
  Objek `KartuAksesOrbit` dibuat langsung di dalam konstruktor `WisatawanVIP`. Keberadaan `KartuAksesOrbit` sangat bergantung pada keberadaan objek `WisatawanVIP`.

---

## Output Program

```text
=== ORBIT WISATA ANTARIKSA ===

[VIP Level 1] [W-AKBAR-01] Nama: Akbar Pratama | Saldo: Rp50,000,000.00 | Kartu Akses: CARD-VIP-999
[REGULER] [W-KEYZIA-02] Nama: Keyzia Putri | Saldo: Rp15,000,000.00 | Bagasi Max: 20 kg
-----------------------------------------------------------------
Destinasi Paket 'Jelajah Galaksi':
- Planet Mars (Kuota: 10 orang)
- Planet Saturnus (Kuota: 5 orang)

[PROSES PENERBANGAN]
Wisatawan   : Akbar Pratama
Pesawat     : Starship Orbit-X (FLIGHT-ORBIT-2026)
Paket Tur   : Jelajah Galaksi
Status      : Siap Meluncur ke Orbit!
