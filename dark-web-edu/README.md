# 🌐 Dark Web Edu: Panduan Edukasi & Cara Mengakses Secara Aman

Repo ini berisi **panduan edukasi** tentang situs-situs dark web, jenis-jenis website yang ada di sana, serta **tahapan cara mengaksesnya dengan aman** (khusus untuk riset keamanan siber, akademik, atau pembelajaran).

> **⚠️ Penting:** Repo ini bersifat **edukasi dan preventive security**. Tidak menyediakan tautan ke konten ilegal, dan sangat menyarankan penggunaan Virtual Machine (VM) atau Tails OS saat mengakses dark web.

---

## 📑 Daftar Isi

- [Tentang Website PrivacySavvy](#1-tentang-website-privacysavvy)
- [Jenis-Jenis Situs Dark Web](#2-jenis-jenis-situs-dark-web)
- [Tahapan Mengakses Dark Web Secara Aman](#3-tahapan-mengakses-dark-web-secara-aman)
- [Alat & Sumber Daya](#4-alat--sumber-daya)
- [Perintah Esensial Git & GitHub](#5-perintah-esensial-git--github)
- [Referensi & Buku Saku](#6-referensi--buku-saku)

---

## 1. Tentang Website PrivacySavvy

**PrivacySavvy** adalah situs berita & panduan privasi yang membahas berbagai topik terkait:
*   Keamanan siber (cybersecurity)
*   Privasi data
*   Review VPN dan alat keamanan
*   **Daftar situs dark web terbaik** (best dark web sites)

**Halaman yang Dibahas:**  
`https://privacysavvy.com/security/safe-browsing/best-dark-web-sites/`

Halaman ini biasanya mencantumkan daftar situs `.onion` yang dikategorikan berdasarkan topik, seperti:
*   Berita & Jurnalisme
*   Privasi & Keamanan
*   Pendidikan & Riset
*   Forum & Komunitas

---

## 2. Jenis-Jenis Situs Dark Web

Website di dark web sebagian besar beroperasi dengan domain `.onion` dan memerlukan **Tor Browser** untuk diakses. Berikut adalahjenis-jenis umumnya:

| Kategori | Deskripsi | Contoh Umum (biasanya) |
|----------|-----------|------------------------|
| 📰 **Berita & Jurnalisme** | Situs berita independen, tanpa sensor. | ProPublica, NY Times, BBC |
| 🛡️ **Privasi & Keamanan** | Panduan penggunaan Tor, VPN, Tails. | Privacy Guides |
| 📚 **Pendidikan & Riset** | Literal ilmiah, buku, referensi. | Sci-Hub, Library Genesis |
| 💬 **Forum & Komunitas** | Diskusi tentang berbagai topik. | Forum teknis, r/onions |
| ⚠️ **Marketplace** | Jual beli barang (biasanya ilegal). | Hindari untuk riset dasar |
| 📎 **Paste Sites** | Seperti Pastebin, berisi data bocor. | Hindari unduhan sembarangan |

---

## 3. Tahapan Mengakses Dark Web Secara Aman

> **Sangat Diperankan:** Selalu gunakan environment terisolasi.

### ✅ **Tahap 1: Persiapan Alat**

1. **Instal Tor Browser**
   ```bash
   # Ubuntu/Debian
   sudo apt update && sudo apt install torbrowser-launcher -y
   ```

2. **Siapkan Virtual Machine (VM)** *SANGAT DISARANKAN*
   *   Gunakan **VirtualBox** atau **VMware**.
   *   Install **Tails OS** (system operasi live focused pada privasi).
   *   Jangan pernah akses dark web dari OS utama (host).

### ✅ **Tahap 2: Konfigurasi Aman**

1. **Buka Tor Browser**
   *   Pastikan ikon di pojok kanan berwarna oren (menyambar bahwa Tor aktif).
   *   Jangan mengubah setting "New Identity" terlalu sering kecuali perlu.

2. **Aktifkan VPN (Opsional Tapi Disarankan)**
   *   Beberapa peneliri menggunakan VPN *sebelum* Tor (VPN > Tor) untuk lapisan anonimitas tambahan.
   *   Gunakan VPN yang tidak merekam log (no-logs policy).

### ✅ **Tahap 3: Praktik Aman Saat Browsing**

1. **Jangan Unduh File Sembarangan**
   *   Jika perlu, pindahkan ke *sandbox* terisolasi terlebih dahulu.
   *   Gunakan **ClamAV** atau ** VirusTotal** untuk scan file.

2. **Jangan Klik Link Acak**
   *   Banyak link bisa mengarahkan ke konten ilegal atau phishing.
   *   Hanya kunjungi tautan yang relevan dengan riset.

3. **Jangan Berinteraksi**
   *   Hindari memposting, komentar, atau transaksi di situs gelap.
   *   Gunakan **pseudonym** (nama samaran) jika harus berinteraksi.

4. **Jangan Berikan Identitas Pribadi**
   *   Jangan login ke akun Google, GitHub, atau email utama.
   *   Buat email alias jika butuh pendaftaran.

### ✅ **Tahap 4: Penutup Aman**

1. **Tutup Tab Tor**
2. **Matikan Tor Browser** lengkap.
3. **Lepas VM** (jika menggunakan VM) atau **Restart Komputer** (jika menggunakan Tails).

---

## 4. Alat & Sumber Daya

### 🛠️ **Tools Wajib**
*   **Tor Browser** – Untuk mengakses situs `.onion`.
*   **VirtualBox / VMware** – Untuk membuat environment terisolasi.
*   **Tails OS** – Sistem operasi live fokus privasi (boots from USB).

### 🌐 **Sumber Edukasi**
*   **Have I Been Pwned** – Cek apakah email sudah bocor: `https://haveibeenpwned.com`
*   **IntelX** – Cari data bocor tanpa masuk ke dark web: `https://intelx.io`
*   **Ahmia** – Mesin pencari dark web yang aman: `https://ahmia.fi`
*   **Dark.fail** – Cek status situs .onion: `https://dark.fail`

### 📚 **Buku Saku Praktis**
*   *Open Source Intelligence Techniques* – Oleh Michael Bazzell
*   *Guide to Tor* – Dokumentasi resmi Proyek Tor

---

## 5. Perintah Esensial Git & GitHub

Karena repo ini juga berfungsi sebagai repositori dokumentasi, berikut adalah perintah yang sering digunakan:

| Perintah | Fungsi |
|----------|--------|
| `gh auth login` | Login ke GitHub |
| `gh auth status` | Cek status login |
| `gh repo create <repo>` | Buat repo baru |
| `gh repo list vanderstark` | Lihat daftar repo |
| `gh repo clone <repo> <path>` | Clone repo ke lokal |
| `git init` | Inisialisasi repo Git |
| `git add .` | Tambah file ke staging |
| `git commit -m "msg"` | Commit file |
| `git push origin main` | Push ke GitHub |
| `git pull origin main` | Pull perubahan dari GitHub |

---

## 6. Referensi & Buku Saku

- 🌐 **Proyek Tor** – https://www.torproject.org
- 📖 **Have I Been Pwned** – https://haveibeenpwned.com
- 🔍 **IntelX** – https://intelx.io
- 🛡️ **PrivacySavvy (Asal Link)** – https://privacysavvy.com/security/safe-browsing/best-dark-web-sites/
- 🦊 **EFF Surveillance Self-Defense** – https://ssd.eff.org

---

## 🧪 **Catatan Penting untuk Bos**

1. **Jangan pernah mengakses dark web dari OS utama (host)** — selalu gunakan VM atau Tails.
2. **Jangan unduh atau berinteraksi dengan konten ilegal** — ini melanggar hukum dan mengesampingkan keamanan.
3. **Gunakan hanya untuk riset edukasi, akademik, atau preventive security.**
4. **Simpan hasil temuan di file terenkripsi** jika perlu, dan hapus setelah selesai.

---

**Repo ini dibuat oleh [vanderstark](https://github.com/vanderstark) untuk keperluan edukasi dan riset keamanan siber.**

*Terakhir diperbarui: September 2025*