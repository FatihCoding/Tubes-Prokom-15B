from modul_core_utils import CoreUtils
from modul_security import Security
from modul_transaksi import TransactionManager

def display_menu(current_user, users):
    """Menampilkan menu utama"""
    menu_options = {
        "1": ("Cek Saldo", lambda: TransactionManager.check_balance(current_user)),
        "2": ("Tarik Uang", lambda: TransactionManager.withdraw_money(current_user)),
        "3": ("Setor Tunai", lambda: TransactionManager.deposit_money(current_user)),
        "4": ("Transfer Uang", lambda: TransactionManager.transfer_money(current_user, users)),
        "5": ("Lihat Riwayat Transaksi", lambda: TransactionManager.display_transaction_history(current_user)),
        "6": ("Informasi Akun", lambda: TransactionManager.display_account_info(current_user)),
        "7": ("Ganti PIN", lambda: Security.change_pin(current_user)),
        "0": ("Keluar", None)
    }

    print("\n=== MENU UTAMA ===")
    for key, (option, _) in menu_options.items():
        print(f"{key}. {option}")

    choice = input("Pilih menu: ")
    if choice in menu_options:
        if choice == "0":
            return False
        
        menu_options[choice][1]()
        input("Tekan Enter untuk kembali ke menu utama...")
        CoreUtils.clear_console()
        return True
    else:
        print("Pilihan tidak valid.")
        return True

def main():
    """Fungsi utama program"""
    users_file = r"D:\projectA\Revisi tubes\LASSTT PLEASEEE\zatabase_terbaru.json"
    users = CoreUtils.load_users(users_file)
    if not users:
        print("Database pengguna tidak ditemukan.")
        return

    login_attempts = 3
    current_user = None

    while login_attempts > 0:
        rekening = input("Masukkan nomor rekening: ")
        pin = input("Masukkan PIN: ")
        current_user = CoreUtils.find_account(rekening, pin, users)

        if current_user:
            CoreUtils.clear_console()
            print(f"Selamat datang, {current_user['identitas']}!")
            break
        else:
            login_attempts -= 1
            print(f"Login gagal. Sisa percobaan: {login_attempts}")

            if login_attempts == 0:
                forgot = input("Lupa PIN? (yes/no): ").lower()
                if forgot == 'yes':
                    TransactionManager.handle_forgot_pin(users)
                return

    if current_user:
        while display_menu(current_user, users):
            pass
        CoreUtils.save_users(users_file, users)
        print("Terima kasih telah menggunakan layanan kami.")

if __name__ == "__main__":
    CoreUtils.clear_console()
    main()