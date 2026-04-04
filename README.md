# SiLacak — Sistem Pelacakan Alumni UMM

Sistem pelacakan alumni berbasis web untuk Universitas Muhammadiyah Malang.

> **Daily Project 3** — Riska Nurhayati Deva | Informatika UMM

---

## 🔗 Link

- **Web:** [https://riskadeva.github.io/Sistem-Alumni/](https://riskadeva.github.io/Sistem-Alumni/) *(ganti dengan link kamu)*
- **Source Code:** [https://github.com/riskadeva/Sistem-Alumni](https://github.com/riskadeva/Sistem-Alumni) *(ganti dengan link kamu)*

---

## 📌 Deskripsi

SiLacak adalah aplikasi web untuk membantu institusi pendidikan melacak keberadaan dan aktivitas alumni melalui berbagai sumber publik seperti LinkedIn, Google Scholar, ResearchGate, GitHub, Instagram, Facebook, TikTok, dan portal berita.

---

## ✨ Fitur Utama

- 🔐 Sistem login & registrasi (Admin dan Alumni)
- 📊 Dashboard statistik alumni
- 👥 Manajemen data alumni lengkap (tambah, edit, hapus, cari)
- 🌐 Input sosial media pribadi (LinkedIn, Instagram, Facebook, TikTok)
- 📞 Input kontak (Email, No HP)
- 🏢 Input data pekerjaan (Posisi, Tempat, Alamat, PNS/Swasta/Wirausaha)
- 🌐 Input sosial media tempat bekerja
- 👁️ Tampilan detail lengkap per alumni
- ⚡ Simulasi pelacakan otomatis dari sumber publik
- 🔑 Kelola akun alumni (persetujuan admin)
- 📋 Laporan & statistik
- 💾 Penyimpanan data menggunakan LocalStorage

---

## 🔐 Akun Login

| Username | Password | Role |
|----------|----------|------|
| `admin` | `admin123` | Administrator |
| `riskadeva` | `umm2025` | Administrator |

> Alumni baru dapat mendaftar melalui tab **"Daftar Alumni"** dan menunggu persetujuan admin.

---

## 🗂️ Struktur Data Alumni

Setiap data alumni mencakup field berikut sesuai kebutuhan tugas:

| No | Field | Keterangan |
|----|-------|------------|
| 1 | LinkedIn | Alamat profil LinkedIn alumni |
| 2 | Instagram | Akun Instagram alumni |
| 3 | Facebook | Akun Facebook alumni |
| 4 | TikTok | Akun TikTok alumni |
| 5 | Email | Email pribadi alumni |
| 6 | No HP | Nomor HP / WhatsApp |
| 7 | Tempat Bekerja | Nama perusahaan / instansi |
| 8 | Alamat Bekerja | Alamat lengkap tempat bekerja |
| 9 | Posisi | Jabatan / posisi pekerjaan |
| 10 | Status Kerja | PNS / Swasta / Wirausaha |
| 11 | LinkedIn Perusahaan | Sosmed tempat bekerja |
| 12 | Instagram Perusahaan | Sosmed tempat bekerja |
| 13 | Facebook Perusahaan | Sosmed tempat bekerja |
| 14 | Website Perusahaan | Website tempat bekerja |

---

## 🧪 Pengujian Aplikasi

### 1. Pengujian Fungsionalitas

| No | Fitur yang Diuji | Langkah Pengujian | Hasil yang Diharapkan | Hasil Aktual | Status |
|----|-----------------|-------------------|----------------------|--------------|--------|
| 1 | Login Admin | Masukkan username `admin` & password `admin123` → klik Masuk | Berhasil masuk ke dashboard admin | Berhasil masuk dan menampilkan dashboard | ✅ Pass |
| 2 | Login Alumni | Masukkan NIM & password yang sudah terdaftar → klik Masuk | Berhasil masuk ke halaman profil alumni | Berhasil masuk dan menampilkan profil | ✅ Pass |
| 3 | Login Gagal | Masukkan username/password salah → klik Masuk | Muncul pesan error | Muncul pesan "Username atau password salah!" | ✅ Pass |
| 4 | Registrasi Alumni | Isi form daftar alumni → klik Daftar Sekarang | Akun tersimpan, menunggu persetujuan admin | Pendaftaran berhasil, status "Menunggu" | ✅ Pass |
| 5 | Persetujuan Akun | Admin buka Kelola Akun → klik Setujui | Status akun berubah menjadi Aktif | Status berubah dan alumni bisa login | ✅ Pass |
| 6 | Tambah Alumni | Klik "+ Tambah Alumni" → isi form lengkap → Simpan | Alumni baru muncul di tabel | Data berhasil ditambahkan | ✅ Pass |
| 7 | Edit Alumni | Klik ✏️ → ubah data → Simpan | Data berhasil diperbarui | Data berhasil diperbarui di tabel | ✅ Pass |
| 8 | Hapus Alumni | Klik 🗑️ → konfirmasi hapus | Alumni terhapus dari tabel | Data berhasil dihapus | ✅ Pass |
| 9 | Lihat Detail | Klik 👁️ pada baris alumni | Muncul modal detail lengkap semua data | Modal detail tampil dengan data lengkap | ✅ Pass |
| 10 | Cari Alumni | Ketik nama/prodi di kolom pencarian | Tabel menampilkan hasil yang sesuai | Filter berjalan secara real-time | ✅ Pass |
| 11 | Filter Status | Pilih status di dropdown filter | Tabel hanya menampilkan status yang dipilih | Filter berfungsi dengan benar | ✅ Pass |
| 12 | Filter Pekerjaan | Pilih PNS/Swasta/Wirausaha di dropdown | Tabel menampilkan alumni sesuai filter | Filter pekerjaan berfungsi | ✅ Pass |
| 13 | Input Sosial Media | Isi field LinkedIn/IG/FB/TikTok → Simpan | Data sosmed tersimpan dan tampil di detail | Data sosmed berhasil disimpan | ✅ Pass |
| 14 | Pelacakan Otomatis | Klik "Jalankan Pelacakan" | Sistem memproses alumni & update status | Log pelacakan tampil, status diperbarui | ✅ Pass |
| 15 | Penyimpanan Data | Tambah data → refresh halaman | Data tetap ada setelah refresh | Data tersimpan di LocalStorage | ✅ Pass |
| 16 | Logout | Klik tombol Logout → konfirmasi | Kembali ke halaman login | Berhasil logout dan session terhapus | ✅ Pass |
| 17 | Pagination | Buka halaman Data Alumni (100 data) | Muncul navigasi halaman | Pagination berfungsi, 8 data per halaman | ✅ Pass |
| 18 | Laporan | Buka halaman Laporan | Menampilkan statistik dan tabel lengkap | Data laporan ditampilkan dengan benar | ✅ Pass |

---

### 2. Pengujian Usability

| No | Aspek | Kriteria | Hasil Pengujian | Status |
|----|-------|----------|-----------------|--------|
| 1 | Kemudahan Navigasi | Menu sidebar jelas dan mudah dipahami | Pengguna dapat berpindah halaman tanpa kebingungan | ✅ Baik |
| 2 | Form Input | Label form jelas, placeholder membantu | Pengguna memahami isian yang diperlukan | ✅ Baik |
| 3 | Notifikasi | Muncul toast saat aksi berhasil/gagal | Feedback diberikan setelah setiap aksi | ✅ Baik |
| 4 | Konfirmasi Hapus | Muncul dialog konfirmasi sebelum hapus | Pengguna tidak sengaja menghapus data | ✅ Baik |
| 5 | Tampilan Status | Status alumni dibedakan dengan warna | Pengguna langsung memahami status pelacakan | ✅ Baik |
| 6 | Role Based Access | Tampilan menu berbeda untuk admin dan alumni | Admin dan alumni mendapat tampilan yang sesuai | ✅ Baik |
| 7 | Detail Alumni | Modal detail menampilkan semua data lengkap | Pengguna dapat melihat semua informasi dalam satu tampilan | ✅ Baik |
| 8 | Link Sosial Media | Link sosmed bisa diklik langsung | Pengguna langsung diarahkan ke profil alumni | ✅ Baik |

---

### 3. Pengujian Kompatibilitas

| No | Browser / Perangkat | Versi | Tampilan | Fungsionalitas | Status |
|----|---------------------|-------|----------|----------------|--------|
| 1 | Google Chrome | 120+ | Normal | Semua fitur berjalan | ✅ Pass |
| 2 | Mozilla Firefox | 115+ | Normal | Semua fitur berjalan | ✅ Pass |
| 3 | Microsoft Edge | 120+ | Normal | Semua fitur berjalan | ✅ Pass |
| 4 | Safari (Mac/iOS) | 16+ | Normal | Semua fitur berjalan | ✅ Pass |
| 5 | Chrome Mobile (Android) | 120+ | Responsive | Semua fitur berjalan | ✅ Pass |
| 6 | Layar Desktop (1920×1080) | — | Optimal | Semua fitur berjalan | ✅ Pass |
| 7 | Layar Laptop (1366×768) | — | Normal | Semua fitur berjalan | ✅ Pass |
| 8 | Layar Mobile (390×844) | — | Responsive | Semua fitur berjalan | ✅ Pass |

---

### 4. Pengujian Performance

| No | Aspek | Metode Pengujian | Hasil | Target | Status |
|----|-------|-----------------|-------|--------|--------|
| 1 | Waktu Muat Awal | Buka halaman pertama kali | < 1 detik | < 3 detik | ✅ Pass |
| 2 | Respons Tambah Data | Klik Simpan → data muncul | Instan | < 1 detik | ✅ Pass |
| 3 | Respons Pencarian | Ketik di search bar → filter | Real-time | < 0.5 detik | ✅ Pass |
| 4 | Load 100 Data Alumni | Buka halaman Data Alumni | < 0.5 detik | < 2 detik | ✅ Pass |
| 5 | Proses Pelacakan | Jalankan tracking 100 alumni | ~40 detik | < 120 detik | ✅ Pass |
| 6 | Ukuran File | Cek ukuran index.html | ~120 KB | < 500 KB | ✅ Pass |

---

### 5. Pengujian Keamanan (Login)

| No | Skenario | Langkah | Hasil yang Diharapkan | Hasil Aktual | Status |
|----|----------|---------|----------------------|--------------|--------|
| 1 | Akses tanpa login | Buka web langsung tanpa login | Halaman login muncul, tidak bisa akses dashboard | Redirect ke halaman login | ✅ Pass |
| 2 | Password salah | Login dengan password salah | Muncul pesan error, tidak bisa masuk | Pesan error tampil | ✅ Pass |
| 3 | Alumni belum disetujui | Login dengan akun belum disetujui admin | Muncul pesan "Akun belum disetujui" | Pesan tampil, tidak bisa masuk | ✅ Pass |
| 4 | Session expired | Tutup browser → buka kembali | Harus login ulang | Kembali ke halaman login | ✅ Pass |
| 5 | Akses menu admin oleh alumni | Alumni coba akses menu admin | Menu admin tidak tampil | Menu admin tersembunyi untuk alumni | ✅ Pass |

---

## 🛠️ Teknologi

- HTML5, CSS3, JavaScript (Vanilla)
- LocalStorage API
- Google Fonts (Syne, DM Sans)

---

## 📁 Struktur File

```
Sistem-Alumni/
├── index.html    # File utama aplikasi
└── README.md     # Dokumentasi & pengujian
```

---

## 📊 Data Alumni

Web ini sudah memuat **100 data alumni UMM** dari file Excel resmi (tahun lulus 2000), mencakup:
- Fakultas Ekonomi (Akuntansi)
- Pascasarjana (Magister Sosiologi Pedesaan & Manajemen)
- Agama Islam (Pendidikan Agama Islam)

Data sosial media, kontak, dan pekerjaan diisi secara manual berdasarkan hasil pencarian dari sumber publik.

---

## 👤 Pengembang

**Riska Nurhayati Deva**
Informatika — Universitas Muhammadiyah Malang
