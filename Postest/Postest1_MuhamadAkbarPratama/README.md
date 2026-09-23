# Posttest 1 - Pemrograman Berorientasi Objek (PBO)

**Sistem Manajemen & Reservasi Wisata Antariksa (Orbit Wisata Antariksa)**

Dokumentasi ini dibuat untuk memenuhi tugas Posttest 1 mata kuliah Pemrograman Berorientasi Objek (PBO). Program diimplementasikan menggunakan bahasa pemrograman Python dengan menerapkan prinsip dasar OOP sesuai ketentuan Modul 1, Modul 2, dan Modul 3.

---

## Deskripsi Program

Program Orbit Wisata Antariksa merupakan sistem pengelolaan reservasi wisata antarplanet berbasis Object-Oriented Programming (OOP). Sistem ini mengintegrasikan tiga entitas utama:
1. Planet: Mengelola data destinasi, jarak dari matahari, serta kuota keberangkatan.
2. Wisatawan: Mengelola profil wisatawan, keanggotaan, saldo, serta mekanisme top up.
3. Reservasi: Memproses transaksi pemesanan, menghitung total biaya termasuk administrasi, serta memperbarui kuota dan saldo secara otomatis.

---

## Struktur Class & Penerapan OOP

### 1. class Planet
* Atribut Kelas:
  * instansi: Nama organisasi pengelola wisata ("Orbit Wisata Antariksa").
  * total_planet: Menghitung jumlah objek Planet yang berhasil dibuat.
  * satuan_jarak: Satuan unit jarak ("AU").
* Atribut Instance:
  * nama_planet: Nama destinasi planet.
  * jarak: Jarak planet dari matahari.
  * __kuota: Sisa kuota kunjungan wisatawan (Private Attribute).
* Method:
  * __str__(): Mengembalikan representasi string format informasi detail planet.
  * kurangi_kuota(n): Instance method untuk mengurangi kuota planet saat terjadi transaksi reservasi.
  * dari_dict(data): Class method (Factory Method) untuk membuat objek Planet dari tipe data dict.
  * set_instansi(nama_baru): Class method untuk mengubah nama instansi secara global.
  * validasi_jarak(j): Static method utilitas untuk memeriksa kevalidan nilai jarak.
* Encapsulation (Getter & Setter):
  * @property kuota: Mengambil nilai atribut private __kuota.
  * @kuota.setter: Memperbarui nilai kuota dengan validasi tipe data integer dan batas non-negatif (ValueError).

---

### 2. class Wisatawan
* Atribut Kelas:
  * total_wisatawan: Menghitung total wisatawan terdaftar.
  * min_topup: Batas nominal minimal top up saldo (50000).
  * kategori_default: Kategori standar keanggotaan ("Reguler").
* Atribut Instance:
  * nama: Nama lengkap wisatawan.
  * id_wisatawan: Kode/ID unik wisatawan.
  * kategori: Kategori keanggotaan wisatawan.
  * __saldo: Jumlah saldo transaksi wisatawan (Private Attribute).
* Method:
  * __str__(): Mengembalikan representasi string profil wisatawan dan saldo terkini.
  * top_up(nominal): Instance method untuk menambah saldo wisatawan jika memenuhi batasan minimal top up.
  * dari_dict(data): Class method (Factory Method) untuk membuat objek Wisatawan dari format dict.
  * set_min_topup(nominal_baru): Class method untuk mengubah batasan minimal top up.
  * validasi_nama(nama): Static method untuk memastikan input nama tidak kosong.
* Encapsulation (Getter & Setter):
  * @property saldo: Mengambil nilai atribut private __saldo.
  * @saldo.setter: Memperbarui saldo dengan validasi tipe data angka dan batas non-negatif (ValueError).

---

### 3. class Reservasi
* Atribut Kelas:
  * total_reservasi: Menghitung total transaksi pemesanan.
  * biaya_admin: Tarif administrasi standar per transaksi (25000).
  * mata_uang: Satuan mata uang transaksi ("IDR").
* Atribut Instance:
  * wisatawan: Objek Wisatawan yang melakukan pemesanan.
  * planet: Objek Planet yang menjadi destinasi.
  * status: Status transaksi ("Pending", "Berhasil", "Gagal (Saldo Kurang)").
  * kode_rsv: Kode transaksi otomatis (RSV-001, RSV-002, dst).
  * __biaya_paket: Harga paket perjalanan wisata (Private Attribute).
* Method:
  * proses(): Instance method untuk menjalankan logika pemesanan (memeriksa saldo, memotong kuota planet, memotong saldo wisatawan, dan memperbarui status).
  * __str__(): Mengembalikan string rincian detail reservasi.
  * dari_data(wisatawan, planet, biaya_paket): Class method konstruktor alternatif pembuatan objek pemesanan.
  * set_biaya_admin(biaya_baru): Class method untuk merubah biaya administrasi secara global.
  * hitung_total(paket, admin): Static method pembantu untuk mengkalkulasi total biaya transaksi.
* Encapsulation (Getter & Setter):
  * @property biaya_paket: Mengambil nilai atribut private __biaya_paket.
  * @biaya_paket.setter: Memperbarui harga paket dengan validasi angka bernilai positif (ValueError).

---

## Panduan & Alur Pengujian Program (`if __name__ == "__main__":`)

Driver code pada program menjalankan serangkaian pengujian sebagai berikut:

1. Inisialisasi Objek:
   * Planet: p1 (konstruktor biasa) dan p2 (menggunakan class method dari_dict).
   * Wisatawan: w1 (konstruktor biasa) dan w2 (menggunakan class method dari_dict).
2. Cetak Informasi Objek:
   * Menampilkan informasi objek (p1, p2, w1, w2) melalui pemanggilan magic method __str__().
3. Pengujian Static Method & Top Up:
   * Menguji pemanggilan static method Wisatawan.validasi_nama() dan Planet.validasi_jarak().
   * Melakukan pengujian top_up() pada w2 dengan nominal di bawah batas minimal (gagal) dan nominal valid (berhasil).
4. Pengujian Transaksi Reservasi:
   * Membuat transaksi r1 dan r2 (menggunakan class method dari_data).
   * Memproses transaksi menggunakan method .proses() untuk menguji pemotongan kuota, saldo, serta perubahan status transaksi.
5. Pengujian Validation Exception (Try-Except):
   * Menguji proteksi @property.setter saat diberi masukan nilai tidak valid/negatif (p1.kuota = -5, w1.saldo = -100000, dan r1.biaya_paket = 0) untuk membuktikan penanganan error via try-except.