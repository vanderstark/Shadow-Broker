#!/usr/bin/env python3
"""
Pushup Counter Application
-----------------------
Aplikasi penghitung pushup dengan antarmuka grafis (GUI) menggunakan tkinter.
Dibuat untuk Hermes Agent - mudah dipahami dan dijalankan.

Cara pakai:
1. Jalankan: python pushup_counter.py
2. Klik tombol Start untuk memulai penghitungan otomatis (setiap 1 detik)
3. Klik Pause untuk menghentikan, Reset untuk kembali ke nol
4. Klik Exit untuk keluar

Fitur:
- penghitungan otomatis berjalan di latar belakang
- pengaturan timeout 1 detik per rep
- antarmuka yang bersih dan sederhana
- fallback command-line interface (CLI) jika GUI tidak tersedia
"""

import tkinter as tk
from tkinter import messagebox


class PushupCounter:
    """
    Class untuk mengelola penghitungan pushup.
    Menggunakan metode setelah: menjalankan perulangan every 1000ms (1 detik).
    """

    def __init__(self, root):
        self.root = root
        self.root.title("Pushup Counter - Hermes Agent")
        self.root.geometry("300x250")
        self.root.resizable(False, False)

        self.count = 0
        self.running = False

        # --- Widget Utama ---
        # Judul aplikasi
        self.title_label = tk.Label(
            root, text="PUSHUP COUNTER", font=("Arial", 16, "bold"), pady=5
        )
        self.title_label.pack()

        # Label menampilkan jumlah
        self.count_label = tk.Label(
            root, text="Pushups: 0", font=("Arial", 24), pady=10
        )
        self.count_label.pack()

        # Frame untuk tombol-tombol
        self.frame = tk.Frame(root)
        self.frame.pack(pady=5)

        # Tombol Start/Pause
        self.start_btn = tk.Button(
            self.frame,
            text="Start",
            width=10,
            command=self.toggle_counting,
            font=("Arial", 12),
        )
        self.start_btn.pack(side=tk.LEFT, padx=5)

        # Tombol Reset
        self.reset_btn = tk.Button(
            self.frame,
            text="Reset",
            width=10,
            command=self.reset_count,
            font=("Arial", 12),
        )
        self.reset_btn.pack(side=tk.RIGHT, padx=5)

        # Tombol Exit
        self.exit_btn = tk.Button(
            root, text="Exit", width=10, command=self.on_closing, font=("Arial", 12)
        )
        self.exit_btn.pack(pady=10)

        # Protokol ketika menutup jendela
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def toggle_counting(self):
        """
        Berganti antara mulai dan berhenti.
        Setiap kali dipanggil, akan menukar status running dan teks tombol.
        """
        self.running = not self.running
        self.start_btn.config(text="Pause" if self.running else "Start")

        if self.running:
            # Mulai perulangan penambahan
            self._increment()

    def _increment(self):
        """
        Fungsi rekursif yang Menambah count setiap 1 detik (1000ms)
        selama status self.running masih True.
        """
        if self.running:
            self.count += 1
            self.count_label.config(text=f"Pushups: {self.count}")
            # Jadwalkan pemanggilan berikutnya setelah 1000ms (1 detik)
            self.root.after(1000, self._increment)

    def reset_count(self):
        """Mereset count ke nol dan menghentikan penghitungan."""
        self.running = False
        self.start_btn.config(text="Start")
        self.count = 0
        self.count_label.config(text="Pushups: 0")

    def on_closing(self):
        """Menangani kejadian menutup jendela."""
        if messagebox.askokcancel("Keluar", "Apakah Anda yakin ingin keluar?"):
            self.running = False
            self.root.destroy()


def main():
    """Titik masuk utama aplikasi."""
    try:
        root = tk.Tk()
        app = PushupCounter(root)
        root.mainloop()
    except Exception as e:
        # Fallback ke mode CLI jika GUI gagal (misal: tidak ada display)
        print(">>> GUI tidak tersedia, menjalankan mode CLI fallback <<<")
        count = 0
        running = False

        print("Pushup Counter CLI - Controls:")
        print("  'c' = Count/Pause")
        print("  'r' = Reset")
        print("  'q' = Quit")

        while True:
            try:
                cmd = input("\nPress key: ").strip().lower()
                if cmd == "c":
                    running = not running
                    status = "Running" if running else "Paused"
                    print(f"  Status: {status} | Current count: {count}")
                elif cmd == "r":
                    running = False
                    count = 0
                    print(f"  Reset. Count: {count}")
                elif cmd == "q":
                    print("  Keluar dari CLI.")
                    break
                else:
                    print("  Perintah tidak dikenal. Gunakan c, r, atau q.")
            except KeyboardInterrupt:
                print("\n  Terputus oleh user.")
                break


if __name__ == "__main__":
    main()