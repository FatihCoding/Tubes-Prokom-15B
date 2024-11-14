
# Simulasi ATM Sederhana
# Data awal
saldo = 1000000
pin = "1234"
riwayat_transaksi = []

# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("\n===== Menu ATM =====")
    print("1. Cek Saldo")
    print("2. Penarikan Uang")
    print("3. Transfer Uang")
    print("4. Setor Tunai")
    print("5. Ganti PIN")
    print("6. Cek Riwayat Transaksi")
    print("7. Informasi Akun")
    print("0. Keluar")
    print("====================")

# Fungsi untuk cek saldo
def cek_saldo():
    print(f"\nSaldo Anda saat ini: Rp {saldo}")
    riwayat_transaksi.append(f"Cek Saldo - Sisa saldo: Rp {saldo}")

# Fungsi untuk penarikan uang
def tarik_uang():
    global saldo
    jumlah = int(input("\nMasukkan jumlah penarikan: Rp "))
    if jumlah > saldo:
        print("Saldo tidak mencukupi.")
    else:
        saldo -= jumlah
        print(f"Penarikan berhasil. Saldo Anda sekarang: Rp {saldo}")
        riwayat_transaksi.append(f"Penarikan - Rp {jumlah}")

# Fungsi untuk transfer uang
def transfer_uang():
    global saldo
    rekening_tujuan = input("\nMasukkan nomor rekening tujuan: ")
    jumlah = int(input("Masukkan jumlah transfer: Rp "))
    if jumlah > saldo:
        print("Saldo tidak mencukupi.")
    else:
        saldo -= jumlah
        print(f"Transfer ke {rekening_tujuan} berhasil. Sisa saldo: Rp {saldo}")
        riwayat_transaksi.append(f"Transfer ke {rekening_tujuan} - Rp {jumlah}")

# Fungsi untuk setor tunai
def setor_tunai():
    global saldo
    jumlah = int(input("\nMasukkan jumlah setoran: Rp "))
    saldo += jumlah
    print(f"Setor tunai berhasil. Saldo Anda sekarang: Rp {saldo}")
    riwayat_transaksi.append(f"Setor Tunai - Rp {jumlah}")

# Fungsi untuk mengganti PIN
def ganti_pin():
    global pin
    pin_lama = input("\nMasukkan PIN lama: ")
    if pin_lama == pin:
        pin_baru = input("Masukkan PIN baru: ")
        pin = pin_baru
        print("PIN berhasil diganti.")
        riwayat_transaksi.append("Ganti PIN")
    else:
        print("PIN salah.")

# Fungsi untuk cek riwayat transaksi
def cek_riwayat():
    print("\n===== Riwayat Transaksi =====")
    if not riwayat_transaksi:
        print("Tidak ada transaksi.")
    else:
        for transaksi in riwayat_transaksi:
            print(transaksi)

# Fungsi untuk informasi akun
def informasi_akun():
    print("\n===== Informasi Akun =====")
    print("Nama Pemegang Akun: Fawwaz Fatih")  # Ganti dengan nama pengguna
    print("Nomor Rekening: 1234567890")
    print(f"Saldo saat ini: Rp {saldo}")

# Fungsi utama
def main():
    print("Selamat datang di ATM!")
    input_pin = input("Masukkan PIN Anda: ")
    if input_pin == pin:
        while True:
            tampilkan_menu()
            pilihan = input("Pilih menu: ")
            if pilihan == "1":
                cek_saldo()
            elif pilihan == "2":
                tarik_uang()
            elif pilihan == "3":
                transfer_uang()
            elif pilihan == "4":
                setor_tunai()
            elif pilihan == "5":
                ganti_pin()
            elif pilihan == "6":
                cek_riwayat()
            elif pilihan == "7":
                informasi_akun()
            elif pilihan == "0":
                print("Terima kasih telah menggunakan layanan ATM.")
                break
            else:
                print("Pilihan tidak valid.")
    else:
        print("PIN salah. Silakan coba lagi.")

# Menjalankan program
if __name__ == "__main__":
    main()
