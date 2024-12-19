# Simulasi ATM - Bank Fatisda

Proyek ini adalah **tugas besar mata kuliah Pemrograman Komputer (Prokom)** yang beranggotakan:  

1. **Muhammad Fawwaz Fatih** (I0324055)  
2. **Dzaki Azhar Radhitya** (I0324076)  
3. **Muhammad Salman Alfauzan Diqtaputra** (I0324090)  

Proyek ini bertujuan untuk memenuhi tugas besar dalam mata kuliah Prokom. Selain itu, proyek ini memberikan gambaran implementasi pemrograman dalam menciptakan aplikasi berbasis terminal yang berfungsi seperti ATM - Bank Fatisda. Melalui pengembangan ini, mahasiswa dapat mempraktikkan konsep dasar pemrograman seperti struktur data, kondisi logika, fungsi, dan interaksi dengan pengguna.  

---

## **Daftar Isi**

1. [Fitur](#fitur)  
2. [Instalasi](#instalasi)  
3. [Penggunaan](#penggunaan)  
4. [Contoh Interaksi](#contoh-interaksi)  
5. [Riwayat Transaksi Persisten](#riwayat-transaksi-persisten)  
6. [Penutup](#penutup)  

---

## **Fitur**

Simulasi ATM - Bank Fatisda - Bank Fatisda ini menyediakan fitur-fitur berikut:  

1. **Cek Saldo**: Memungkinkan pengguna untuk memeriksa saldo terkini dalam akun mereka.  
2. **Tarik Uang**: Pengguna dapat menarik uang dari akun mereka dengan pengecekan saldo untuk memastikan transaksi yang aman.  
3. **Setor Tunai**: Pengguna dapat menyetorkan uang ke dalam akun mereka.  
4. **Transfer Uang**: Mengirimkan uang ke akun lain yang terdaftar dalam sistem.  
5. **Ganti PIN**: Mengubah PIN akun untuk menjaga keamanan pengguna.  
6. **Lihat Riwayat Transaksi**: Menampilkan daftar transaksi terbaru yang dilakukan pengguna.  
7. **Informasi Akun**: Menampilkan detail akun pengguna, seperti nama pemilik dan ID pengguna.  
8. **Keluar**: Mengakhiri sesi penggunaan ATM - Bank Fatisda.  

---
## **Penggunaan**

1. Jalankan program dengan perintah berikut:  
   ```bash  
   python atm_simulation.py  
   ```  

2. Masukkan **ID Pengguna** dan **PIN** yang valid untuk mengakses akun Anda.  

3. Setelah berhasil masuk, Anda akan disajikan menu berikut:  
   ```plaintext  
   Pilihan:  
   1. Cek Saldo  
   2. Tarik Uang  
   3. Setor Tunai  
   4. Transfer Uang  
   5. Ganti PIN  
   6. Lihat Riwayat Transaksi  
   7. Informasi Akun  
   0. Keluar  
   ```  

4. Pilih opsi sesuai kebutuhan dengan memasukkan angka yang sesuai.  

---

## **Contoh Interaksi**

Berikut adalah contoh interaksi pengguna dengan program:  

```plaintext  
Selamat Datang di Simulasi ATM - Bank Fatisda - Bank Fatisda  
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
```

---

## **Riwayat Transaksi Persisten**

Fitur ini memungkinkan pengguna untuk melihat riwayat transaksi mereka, termasuk penarikan, setoran, transfer, dan perubahan PIN, bahkan setelah program dihentikan dan dijalankan ulang.  

### **Mekanisme Penyimpanan**  
- Data transaksi dicatat dalam file `accounts.json`.  
- Informasi yang disimpan mencakup jenis transaksi, jumlah, tanggal, dan pihak yang terlibat (untuk transfer).  

### **Keamanan Data**  
- PIN pengguna disimpan untuk menjaga kerahasiaan data.  

### **Pemulihan Data**  
- Saat program dijalankan kembali, file `accounts.json` akan dibaca untuk memuat data pengguna, termasuk saldo terbaru dan riwayat transaksi.  

### **Contoh Riwayat Transaksi**  
```plaintext  
Riwayat Transaksi:  
1. Setoran Tunai: Rp100.000  
2. Transfer Uang: Rp50.000 ke ID 67890  
3. Penarikan Tunai: Rp30.000  
```  

Dengan fitur ini, aplikasi ATM - Bank Fatisda dapat menyimpan data secara persisten, memastikan informasi tetap konsisten dan dapat diakses kapan saja.  

---

### **Flowchart Program**  
![Flowchart_Tubesl (2)](https://github.com/user-attachments/assets/ba9e4f8f-7e8d-4411-8f57-6a3a6d609484)


## **Penutup**

Proyek **Simulasi ATM - Bank Fatisda - Bank Fatisda** ini merupakan wujud nyata dari implementasi konsep pemrograman yang telah dipelajari selama perkuliahan. Dengan menampilkan fitur-fitur yang relevan dan mendekati fungsi nyata sebuah ATM - Bank Fatisda, proyek ini dirancang tidak hanya untuk memenuhi tugas besar mata kuliah Pemrograman Komputer, tetapi juga sebagai pengalaman belajar yang berharga dalam pengembangan aplikasi berbasis terminal.  

Kami berharap proyek ini dapat menggambarkan kemampuan kami dalam mengintegrasikan logika, algoritma, dan pemahaman struktur data untuk menyelesaikan permasalahan nyata. Dengan fitur seperti *cek saldo*, *tarik tunai*, *setor tunai*, hingga *transfer uang* dan *riwayat transaksi persisten*, proyek ini memberikan gambaran tentang bagaimana teknologi dapat diadaptasi untuk mendukung aktivitas sehari-hari.  

Kami mengundang pembaca untuk mengeksplorasi program ini lebih lanjut dan memberikan masukan yang membangun. Terima kasih atas perhatian dan dukungannya! 🚀  
