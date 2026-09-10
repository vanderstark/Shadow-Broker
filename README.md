# Shadow-Broker 🔍 Dark Web Intelligence Platform

Platform **Dark Web Monitoring & Intelligence Gathering** yang dirancang untuk analisis ancaman keamanan siber secara otomatis. Platform ini mengumpulkan dan mengkorelasikan data dari berbagai sumber untuk memberikan intelijen yang dapat ditindaklanjuti.

---

## 🎯 Fitur Utama

- 🕸️ **Scraper Otomatis**: Mengumpulkan data dari sumber seperti Reddit dan forum dark web.
- 🌐 **Onion Service Monitor**: Memantau situs .onion secara real-time untuk mendeteksi perubahan.
- 📊 **Dashboard Visualisasi**: Ringkasan hasil pemindaian dalam format yang mudah dipahami.
- 💾 **Data Persistence**: Penyimpanan data yang andal untuk analisis intelijen jangka panjang.
- 🐳 **Dockerized**: Deployment yang mudah dan dapat direplikasi di lingkungan manapun.

---

## 🚀 Cara Memulai (Deployment)

### Persyaratan
- [Docker](https://www.docker.com/) dan [Docker Compose](https://docs.docker.com/compose/) sudah terinstal.

### Langkah-langkah
```bash
# 1. Clone repositori
git clone https://github.com/vanderstark/Shadow-Broker.git
cd Shadow-Broker

# 2. Salin konfigurasi environment
cp .env.example .env

# 3. Jalankan platform dengan Docker
docker-compose up -d

# 4. Akses Dashboard
Buka http://localhost:5000 di browser Anda.
```

---

## 📁 Struktur Proyek

```
Shadow-Broker/
├── docker-compose.yml          # Konfigurasi container utama
├── start.sh                    # Skrip untuk memulai backend
├── .env.example                # Contoh konfigurasi environment
├── Mesh.md                     # Dokumentasi arsitektur jaringan
├── web/                        # Kode sumber untuk dashboard (Frontend)
└── CONTRIBUTING.md             # Panduan kontribusi
```

---

## ⚙️ Konfigurasi Environment

Pastikan file `.env` sudah diisi dengan parameter yang benar:

```env
REDDIT_CLIENT_ID=your_id_here
REDDIT_CLIENT_SECRET=your_secret_here
DATABASE_URL=your_db_connection_string
SECRET_KEY=your_random_key
```

---

## 🛡️ Keamanan & Etika

✅ **Penggunaan**: Platform ini ditujukan khusus untuk tujuan riset keamanan, edukasi, dan audit intelijen.
✅ **Tanggung Jawab**: Pengguna bertanggung jawab penuh atas data yang dikumpulkan dan diproses menggunakan alat ini.
❌ **Larangan**: Dilarang keras menggunakan alat ini untuk tindakan kriminal, peretasan ilegal, atau aktivitas yang melanggar hukum.

---

## 📚 Dokumentasi Lebih Lanjut

- `Mesh.md` - Detail arsitektur jaringan monitoring.
- `CONTRIBUTING.md` - Panduan jika Anda ingin berkontribusi pada pengembangan platform.

---

## 📜 Lisensi

© 2026 vanderstark. Semua hak dilindungi.
