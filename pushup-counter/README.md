# Pushup Counter

Aplikasi penghitung pushup sederhana dengan antarmuka grafis (GUI) dan fallback ke CLI.

## Cara Menggunakan

### 1. Persiapan
Pastikan Python 3 dan library `tkinter` terinstall.
Untuk Debian/Ubuntu:
```bash
sudo apt update && sudo apt install python3-tk -y
```

### 2. Dapatkan Aplikasi
Anda bisa mengkloning repositori ini atau mengunduh file `pushup_counter.py` secara langsung.
```bash
git clone https://github.com/vanderstark/pushup-counter.git
cd pushup-counter
```

### 3. Jalankan Aplikasi
```bash
python3 pushup_counter.py
```

### 4. Kontrol Aplikasi (GUI)
Jika Anda memiliki lingkungan desktop dengan GUI:
-   **Start**: Memulai penghitungan otomatis (+1 setiap detik).
-   **Pause**: Menghentikan sementara penghitungan.
-   **Reset**: Mengembalikan angka ke 0.
-   **Exit**: Menutup aplikasi.

### 5. Mode CLI (Jika GUI tidak ada)
Jika Anda menjalankan di server tanpa display (headless) atau GUI tidak ditemukan:
-   Aplikasi akan otomatis beralih ke mode CLI.
-   Ketik **'c'** untuk Start/Pause.
-   Ketik **'r'** untuk Reset.
-   Ketik **'q'** untuk Keluar.

### Contoh Tampilan CLI
```
>>> GUI tidak tersedia, menjalankan mode CLI fallback <<<
Pushup Counter CLI - Controls:
  'c' = Count/Pause
  'r' = Reset
  'q' = Quit

Press key: c
  Status: Running | Current count: 0

Press key: c
  Status: Paused | Current count: 1

Press key: r
  Reset. Count: 0

Press key: q
  Keluar dari CLI.
```

---

## Kontribusi

Merasa ada perbaikan atau ide fitur baru? Jangan ragu untuk membuat Pull Request!

---

## Lisensi

Aplikasi ini dirilis di bawah lisensi MIT.
