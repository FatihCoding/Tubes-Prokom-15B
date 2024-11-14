# Simulasi ATM

Proyek ini adalah program simulasi ATM sederhana yang dikembangkan menggunakan Python. Program ini memungkinkan pengguna untuk melakukan fungsi-fungsi dasar ATM, termasuk mengecek saldo, menarik uang tunai, melakukan setoran, dan mengelola akun.

## Daftar Isi

- [Fitur](#fitur)
- [Instalasi](#instalasi)
- [Penggunaan](#penggunaan)
- [Contoh](#contoh)
- [Kontribusi](#kontribusi)

**A. Fitur**

Cek Saldo: Memungkinkan pengguna untuk memeriksa saldo terkini dalam akun mereka.
Penarikan Uang Tunai: Pengguna dapat menarik uang tunai dari akun mereka, dengan pengecekan saldo untuk memastikan transaksi yang aman.

Setoran Tunai: Pengguna dapat menyetorkan uang ke dalam akun mereka.
Manajemen Akun: Program ini memungkinkan beberapa pengguna untuk memiliki akun yang terpisah, masing-masing dengan ID pengguna dan PIN unik.

**B. Instalasi**

Clone repositori ini ke komputer Anda dengan perintah berikut:
bash
Copy code
git clone https://github.com/username-anda/atm-simulation.git
Arahkan terminal ke direktori proyek:
bash
Copy code
cd atm-simulation

Pastikan Anda telah menginstal Python 3 di sistem Anda. Anda dapat memeriksanya dengan perintah:
bash
Copy code
python --version

Tidak ada ketergantungan khusus yang diperlukan. Pastikan Anda menjalankan file Python menggunakan Python 3.

**C.Penggunaan**

Jalankan program dengan perintah berikut:

bash
Copy code
python atm_simulation.py
Setelah program berjalan, Anda akan diminta untuk memasukkan ID Pengguna dan PIN. Pastikan Anda menggunakan ID dan PIN yang valid.

Setelah masuk, Anda akan disajikan dengan beberapa opsi, termasuk:

Mengecek saldo
Menarik uang tunai
Menyetor uang tunai
Keluar dari akun
Pilih opsi sesuai kebutuhan dengan memasukkan angka yang sesuai.

**D. Contoh**
Berikut adalah contoh interaksi dengan program (dengan asumsi input pengguna).

plaintext
Copy code
Selamat Datang di Simulasi ATM
Masukkan ID Pengguna Anda: 12345
Masukkan PIN Anda: ****

Pilihan:
1. Cek Saldo
2. Tarik Tunai
3. Setor Tunai
4. Keluar

Masukkan pilihan: 1
Saldo Anda adalah: Rp500.000

**E.Kontribusi**

Kami menyambut kontribusi dari siapa saja yang ingin membantu pengembangan proyek ini. 
Langkah-langkah kontribusi:

Fork repositori ini.
Buat branch baru untuk fitur atau perubahan Anda (git checkout -b fitur/FiturBaru).
Commit perubahan Anda (git commit -m 'Menambahkan fitur baru').
Push branch tersebut ke repository Anda (git push origin fitur/FiturBaru).
Buat Pull Request di GitHub.
