import os
import json
import random
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Penyimpanan sementara OTP dan waktu kedaluwarsa
otp_storage = {}

# Fungsi Utility
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def format_rupiah(nilai):
    return f"Rp {nilai:,.0f}".replace(",", ".")

# Fungsi Validasi
def validasi_email(email):
    return email.endswith("@gmail.com")

# Fungsi Manajemen Data JSON
def muat_data_json(nama_file):
    try:
        with open(nama_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: Data pengguna tidak valid.")
        return []

def simpan_data_json(nama_file, data):
    with open(nama_file, 'w') as file:
        json.dump(data, file, indent=4)

# Fungsi Keamanan
def generate_otp():
    return random.randint(100000, 999999)

def kirim_otp_email(email, otp):
    sender_email = "bankfatisda@gmail.com"
    sender_password = "brig ksra ireu mnfe"  # Ganti dengan password asli akun Anda.

    subject = "Kode OTP Anda"
    body = f"Kode OTP Anda adalah: {otp}. Jangan bagikan kode ini kepada siapa pun."

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, email, message.as_string())
            print("Email OTP berhasil dikirim.")
    except Exception as e:
        print(f"Gagal mengirim email: {e}")

def store_otp(email, otp):
    expiration_time = datetime.now() + timedelta(minutes=5)
    otp_storage[email] = {
        "otp": otp,
        "expires_at": expiration_time
    }

def validate_otp(email, input_otp):
    if email not in otp_storage:
        return False

    stored_otp = otp_storage[email]
    if datetime.now() > stored_otp["expires_at"]:
        del otp_storage[email]
        return False

    if stored_otp["otp"] != input_otp:
        return False

    del otp_storage[email]
    return True

# Fungsi Transaksi dan Akun
def cari_akun(rekening, pin, users):
    for user in users:
        if user['rekening'] == rekening and user['pin'] == pin:
            return user
    return None

def cari_akun_dengan_email(email, users):
    for user in users:
        if user.get('email') == email:
            return user
    return None

def tambahkan_email_akun(current_user, email):
    current_user['email'] = email

def email_terdaftar(email, users):
    return any(user.get('email') == email for user in users)

def tambahkan_transaksi(current_user, deskripsi, jumlah):
    now = datetime.now()
    tanggal = now.strftime("%Y-%m-%d")
    waktu = now.strftime("%H:%M:%S")
    transaksi = {
        "deskripsi": deskripsi,
        "jumlah": jumlah,
        "tanggal": tanggal,
        "waktu": waktu
    }
    if 'riwayat' not in current_user or not isinstance(current_user['riwayat'], dict):
        current_user['riwayat'] = {}
    current_user['riwayat'].setdefault(tanggal, []).append(transaksi)

def transfer_akun_tidak_ditemukan():
    while True:
        pilihan = input("Akun tujuan tidak ditemukan. Apakah Anda ingin mencoba lagi? (y/n): ").lower()
        if pilihan == 'y':
            return True
        elif pilihan == 'n':
            return False

# Fungsi Transaksi Utama
def cek_saldo(current_user):
    print(f"Saldo Anda: {format_rupiah(current_user['saldo'])}")

def tarik_uang(current_user):
    while True:
        try:
            jumlah = int(input("Masukkan jumlah penarikan: "))
            if jumlah <= 0:
                print("Jumlah harus lebih dari 1.")
            elif jumlah > current_user['saldo']:
                print("Saldo tidak mencukupi.")
            else:
                current_user['saldo'] -= jumlah
                tambahkan_transaksi(current_user, "Tarik Tunai", -jumlah)
                print(f"Penarikan berhasil. Saldo Anda sekarang: {format_rupiah(current_user['saldo'])}")
                break
        except ValueError:
            print("Masukkan jumlah yang valid.")
    input("Tekan Enter untuk kembali ke menu utama...")
    clear_console()

def setor_tunai(current_user):
    while True:
        try:
            jumlah = int(input("Masukkan jumlah setoran: "))
            if jumlah <= 0:
                print("Jumlah harus lebih dari 1.")
            else:
                current_user['saldo'] += jumlah
                tambahkan_transaksi(current_user, "Setor Tunai", jumlah)
                print(f"Setoran berhasil. Saldo Anda sekarang: {format_rupiah(current_user['saldo'])}")
                break
        except ValueError:
            print("Masukkan jumlah yang valid.")
    input("Tekan Enter untuk kembali ke menu utama...")
    clear_console()

def transfer_uang(current_user, users):
    while True:
        rekening_tujuan = input("Masukkan nomor rekening tujuan: ")

        # Tidak bisa transfer ke rekening sendiri
        if rekening_tujuan == current_user['rekening']:
            print("Anda tidak bisa mentransfer ke rekening Anda sendiri.")
            continue

        penerima = next((user for user in users if user['rekening'] == rekening_tujuan), None)

        if not penerima:
            if not transfer_akun_tidak_ditemukan():
                input("Tekan Enter untuk kembali ke menu utama...")
                clear_console()
                return
            continue

        try:
            jumlah = int(input("Masukkan jumlah transfer: "))
            if jumlah <= 0:
                print("Jumlah harus lebih dari 1.")
            elif jumlah > current_user['saldo']:
                print("Saldo tidak mencukupi.")
            else:
                email = current_user.get('email')
                if not email:
                    email = input("Masukkan email Anda untuk menerima OTP: ")
                    if not validasi_email(email):
                        print("Format email harus @gmail.com. Keluar dari program.")
                        exit()
                    if email_terdaftar(email, users):
                        print("Email sudah terdaftar pada akun lain. Keluar dari program.")
                        exit()
                    tambahkan_email_akun(current_user, email)

                otp = generate_otp()
                kirim_otp_email(email, otp)
                store_otp(email, otp)

                while True:
                    try:
                        input_otp = int(input("Masukkan kode OTP yang dikirim ke email Anda: "))
                        if validate_otp(email, input_otp):
                            current_user['saldo'] -= jumlah
                            penerima['saldo'] += jumlah
                            tambahkan_transaksi(current_user, f"Transfer ke {penerima['identitas']}", -jumlah)
                            tambahkan_transaksi(penerima, f"Transfer dari {current_user['identitas']}", jumlah)
                            print(f"Transfer berhasil. Saldo Anda sekarang: {format_rupiah(current_user['saldo'])}")
                            break
                        else:
                            print("OTP tidak valid. Silakan coba lagi.")
                            otp = generate_otp()
                            kirim_otp_email(email, otp)
                            store_otp(email, otp)
                    except ValueError:
                        print("OTP harus berupa angka.")
                break
        except ValueError:
            print("Masukkan jumlah yang valid.")
    input("Tekan Enter untuk kembali ke menu utama...")
    clear_console()

def lupa_pin(users):
    email = input("Masukkan email terdaftar Anda: ")
    if not validasi_email(email):
        print("Format email harus @gmail.com. Keluar dari program.")
        exit()

    user = cari_akun_dengan_email(email, users)
    if not user:
        print("Email tidak ditemukan.")
        return

    otp = generate_otp()
    kirim_otp_email(email, otp)
    store_otp(email, otp)

    for _ in range(3):
        try:
            input_otp = int(input("Masukkan kode OTP: "))
            if validate_otp(email, input_otp):
                while True:
                    new_pin = input("Masukkan PIN baru (6 digit): ")
                    if len(new_pin) == 6 and new_pin.isdigit():
                        user['pin'] = new_pin
                        print("PIN berhasil direset.")
                        return
                    else:
                        print("PIN harus 6 digit.")
        except ValueError:
            print("OTP harus berupa angka.")

    print("Gagal mereset PIN.")

# Fungsi Informasi Akun dan Ganti PIN
def informasi_akun(current_user):
    print(f"Identitas: {current_user['identitas']}")
    print(f"Rekening: {current_user['rekening']}")
    print(f"Email: {current_user.get('email', 'Tidak ada email terdaftar')}")

def ganti_pin(current_user):
    old_pin = input("Masukkan PIN lama: ")
    if old_pin == current_user['pin']:
        while True:
            new_pin = input("Masukkan PIN baru (6 digit): ")
            if len(new_pin) == 6 and new_pin.isdigit():
                current_user['pin'] = new_pin
                print("PIN berhasil diubah.")
                break
            else:
                print("PIN harus 6 digit.")
    else:
        print("PIN lama salah.")

# Fungsi Utama
def main():
    nama_file = r"Revisi tubes/zatabase_users.json"
    users = muat_data_json(nama_file)
    if not users:
        print("Database pengguna tidak ditemukan.")
        return

    percobaan_login = 3
    while percobaan_login > 0:
        rekening = input("Masukkan nomor rekening: ")
        pin = input("Masukkan PIN: ")
        current_user = cari_akun(rekening, pin, users)

        if current_user:
            clear_console()
            print(f"Selamat datang, {current_user['identitas']}!")
            break
        else:
            percobaan_login -= 1
            print(f"Login gagal. Sisa percobaan: {percobaan_login}")

            if percobaan_login == 0:
                lupa = input("Lupa PIN? (y/n): ").lower()
                if lupa == 'y':
                    lupa_pin(users)
                return

    while True:
        print("\n=== MENU UTAMA ===")
        print("1. Cek Saldo")
        print("2. Tarik Uang")
        print("3. Setor Tunai")
        print("4. Transfer Uang")
        print("5. Lihat Riwayat Transaksi")
        print("6. Informasi Akun")
        print("7. Ganti PIN")
        print("0. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            cek_saldo(current_user)
            input("Tekan Enter untuk kembali ke menu utama...")
            clear_console()
        elif pilihan == "2":
            tarik_uang(current_user)
        elif pilihan == "3":
            setor_tunai(current_user)
        elif pilihan == "4":
            transfer_uang(current_user, users)
        elif pilihan == "5":
            for tanggal, transaksi_list in current_user.get('riwayat', {}).items():
                print(f"\nTanggal: {tanggal}")
                for transaksi in transaksi_list:
                    print(f"  - {transaksi['waktu']} | {transaksi['deskripsi']} | {format_rupiah(transaksi['jumlah'])}")
            input("Tekan Enter untuk kembali ke menu utama...")
            clear_console()
        elif pilihan == "6":
            informasi_akun(current_user)
            input("Tekan Enter untuk kembali ke menu utama...")
            clear_console()
        elif pilihan == "7":
            ganti_pin(current_user)
        elif pilihan == "0":
            simpan_data_json(nama_file, users)
            print("Terima kasih telah menggunakan layanan kami.")
            break
        else:
            print("Pilihan tidak valid.") 

if __name__ == "__main__":
    clear_console()
    main()
    