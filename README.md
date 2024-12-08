Simulasi ATM
Proyek ini adalah tugas besar mata kuliah Pemrograman Komputer (Prokom) yang beranggotakan:

Muhammad Fawwaz Fatih (I0324055)
Dzaki Azhar Radhitya (I0324076)
Muhammad Salman Alfauzan Diqtaputra (I0324090)
Proyek ini bertujuan untuk memenuhi tugas besar dalam mata kuliah Prokom. Selain itu, proyek ini memberikan gambaran implementasi pemrograman dalam menciptakan aplikasi berbasis terminal yang berfungsi seperti ATM. Melalui pengembangan ini, mahasiswa dapat mempraktikkan konsep dasar pemrograman seperti struktur data, kondisi logika, fungsi, dan interaksi dengan pengguna.

Daftar Isi
Fitur
Instalasi
Penggunaan
Contoh
Kontribusi
A. Fitur
Simulasi ATM ini menyediakan fitur-fitur berikut:

Cek Saldo: Memungkinkan pengguna untuk memeriksa saldo terkini dalam akun mereka.
Tarik Uang: Pengguna dapat menarik uang dari akun mereka, dengan pengecekan saldo untuk memastikan transaksi yang aman.
Setor Tunai: Pengguna dapat menyetorkan uang ke dalam akun mereka.
Transfer Uang: Mengirimkan uang ke akun lain yang terdaftar dalam sistem.
Ganti PIN: Mengubah PIN akun untuk menjaga keamanan pengguna.
Lihat Riwayat Transaksi: Menampilkan daftar transaksi terbaru yang dilakukan pengguna.
Informasi Akun: Menampilkan detail akun pengguna, seperti nama pemilik dan ID pengguna.
Keluar: Mengakhiri sesi penggunaan ATM.
B. Instalasi
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
Tidak ada ketergantungan khusus yang diperlukan. Jalankan file Python menggunakan Python 3.

C. Penggunaan
Jalankan program dengan perintah berikut:

bash
Copy code
python atm_simulation.py  
Setelah program berjalan, Anda akan diminta untuk memasukkan ID Pengguna dan PIN. Pastikan Anda menggunakan ID dan PIN yang valid.

Setelah berhasil masuk, Anda akan disajikan menu dengan opsi berikut:

plaintext
Copy code
Pilihan:  
1. Cek Saldo  
2. Tarik Uang  
3. Setor Tunai  
4. Transfer Uang  
5. Ganti PIN  
6. Lihat Riwayat Transaksi  
7. Informasi Akun  
0. Keluar  
Pilih opsi yang sesuai kebutuhan dengan memasukkan angka yang sesuai.

D. Contoh
Berikut adalah contoh interaksi dengan program (asumsi input pengguna):

plaintext
Copy code
Selamat Datang di Simulasi ATM  
Masukkan ID Pengguna Anda: 12345  
Masukkan PIN Anda: ****  

Pilihan:  
1. Cek Saldo  
2. Tarik Uang  
3. Setor Tunai  
4. Transfer Uang  
5. Ganti PIN  
6. Lihat Riwayat Transaksi  
7. Informasi Akun  
0. Keluar  

Masukkan pilihan: 1  
Saldo Anda adalah: Rp500.000  

Masukkan pilihan: 4  
Masukkan ID tujuan transfer: 67890  
Masukkan jumlah transfer: Rp100.000  
Transfer berhasil! Saldo Anda sekarang: Rp400.000  

Masukkan pilihan: 0  
Terima kasih telah menggunakan layanan kami!  
E. Kontribusi
Kami menyambut kontribusi dari siapa saja yang ingin membantu pengembangan proyek ini.
Langkah-langkah kontribusi:

Fork repositori ini.
Buat branch baru untuk fitur atau perubahan Anda:
bash
Copy code
git checkout -b fitur/FiturBaru  
Commit perubahan Anda:
bash
Copy code
git commit -m 'Menambahkan fitur baru'  
Push branch tersebut ke repository Anda:
bash
Copy code
git push origin fitur/FiturBaru  
Buat Pull Request di GitHub.

Riwayat Transaksi Persisten
Fitur ini memungkinkan pengguna untuk melihat riwayat transaksi mereka, termasuk penarikan, setoran, transfer, dan perubahan PIN, bahkan setelah program dihentikan dan dijalankan ulang. Hal ini dicapai dengan memanfaatkan penyimpanan data persisten menggunakan file JSON.

Mekanisme Penyimpanan

Setiap kali pengguna melakukan transaksi, detail transaksi akan dicatat ke file accounts.json.
Informasi yang disimpan meliputi jenis transaksi, jumlah, tanggal, dan pihak yang terlibat (jika transaksi berupa transfer).
Riwayat Transaksi

Pengguna dapat melihat daftar semua transaksi yang telah dilakukan sebelumnya, termasuk:
Penarikan Uang Tunai
Setoran Tunai
Transfer Uang
Penerimaan Transfer
Perubahan PIN
Keamanan Data

PIN pengguna disimpan dalam bentuk hash menggunakan algoritma SHA-256 untuk menjaga kerahasiaan data.
Pemulihan Data

Saat program dijalankan kembali, file accounts.json akan dibaca untuk memuat data pengguna, termasuk saldo terbaru dan riwayat transaksi.
Contoh Interaksi
Berikut adalah contoh riwayat transaksi yang ditampilkan dalam program:

plaintext
Copy code
Riwayat Transaksi:
1. [2024-12-03 10:00:00] Setoran Tunai: Rp100.000
2. [2024-12-03 10:05:00] Transfer Uang: Rp50.000 ke ID 67890
3. [2024-12-03 10:10:00] Penarikan Tunai: Rp30.000
Fitur Multi-Akun

Setiap akun memiliki riwayat transaksi dan saldo yang terpisah berdasarkan ID pengguna.
Dengan fitur ini, aplikasi ATM tidak hanya bersifat interaktif tetapi juga mampu menjaga data pengguna agar tetap konsisten dan dapat diakses kembali kapan saja.

Penutup
Proyek Simulasi ATM ini merupakan wujud nyata dari implementasi konsep pemrograman yang telah dipelajari selama perkuliahan. Dengan menampilkan fitur-fitur yang relevan dan mendekati fungsi nyata sebuah ATM, proyek ini dirancang tidak hanya untuk memenuhi tugas besar mata kuliah Pemrograman Komputer, tetapi juga sebagai pengalaman belajar yang berharga dalam pengembangan aplikasi berbasis terminal.

Kami berharap proyek ini dapat menggambarkan kemampuan kami dalam mengintegrasikan logika, algoritma, dan pemahaman struktur data untuk menyelesaikan permasalahan nyata. Dengan fitur seperti cek saldo, tarik tunai, setor tunai, hingga transfer uang dan riwayat transaksi persisten, proyek ini memberikan gambaran tentang bagaimana teknologi dapat diadaptasi untuk mendukung aktivitas sehari-hari.

Terakhir, README ini juga bertujuan untuk menyampaikan presentasi yang jelas dan terstruktur dari proyek kami. Kami mengundang pembaca untuk mengeksplorasi program ini lebih lanjut dan memberikan masukan yang membangun. Terima kasih atas perhatian dan dukungannya! 🚀






