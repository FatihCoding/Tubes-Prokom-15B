import os
from moduldatapengguna import muat_data_json, simpan_data_json, cari_akun
from modultransaksi import cek_saldo, tarik_uang, setor_tunai, transfer_uang, ganti_pin
from modul_io_pengguna import tampilkan_menu, input_angka, lihat_riwayat, informasi_akun, clear_console


def main():
    """
    Fungsi utama untuk menjalankan aplikasi ATM.
    """
    nama_file = r"prokomtubes\database_users.json"
    users = muat_data_json(nama_file)
    if not users:
        print("Database pengguna tidak ditemukan.")
        return

    percobaan_login = 3  # Batas percobaan login

    while percobaan_login > 0:
        # Input data login
        input_rekening = input("Masukkan nomor rekening Anda: ")
        input_pin = input("Masukkan PIN Anda: ")
        current_user = cari_akun(input_rekening, input_pin, users)

        if current_user:
            clear_console()
            print(f"Selamat Datang di Bank Fatisda, {current_user['identitas']}!")
            break
        else:
            percobaan_login -= 1
            print(f"Rekening atau PIN salah. Sisa percobaan: {percobaan_login}")
            if percobaan_login == 0:
                print("Anda telah melebihi batas percobaan login. Program akan keluar.")
                return

    while True:
        # Menampilkan menu utama
        tampilkan_menu()
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            cek_saldo(current_user)
        elif pilihan == "2":
            tarik_uang(current_user, input_angka)
        elif pilihan == "3":
            setor_tunai(current_user)
        elif pilihan == "4":
            transfer_uang(current_user, users)
        elif pilihan == "5":
            ganti_pin(current_user)
        elif pilihan == "6":
            lihat_riwayat(current_user)
        elif pilihan == "7":
            informasi_akun(current_user)
        elif pilihan == "0":
            # Simpan perubahan data sebelum keluar
            simpan_data_json(nama_file, users)
            clear_console()
            print("Terima kasih telah menggunakan layanan ATM. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid.")

        input("\nTekan Enter untuk kembali ke menu utama...")


if __name__ == "__main__":
    clear_console()
    main()
