import os

def tampilkan_menu():
    print("\n=== MENU UTAMA ===")
    print("1. Cek Saldo")
    print("2. Tarik Uang")
    print("3. Setor Tunai")
    print("4. Transfer Uang")
    print("5. Ganti PIN")
    print("6. Lihat Riwayat Transaksi")
    print("7. Informasi Akun")
    print("0. Keluar")

def input_angka(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Masukkan angka yang valid.")

def lihat_riwayat(current_user):
    print("\n=== RIWAYAT TRANSAKSI ===")
    riwayat = current_user.get('riwayat', [])
    if not riwayat:
        print("Belum ada riwayat transaksi.")
    else:
        for item in riwayat:
            print(f"- {item}")

def informasi_akun(current_user):
    print("\n=== INFORMASI AKUN ===")
    print(f"Nama Pemilik: {current_user['identitas']}")
    print(f"Nomor Rekening: {current_user['rekening']}")
    print(f"Saldo: Rp {current_user['saldo']}")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
