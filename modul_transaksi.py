
from modul_core_utils import CoreUtils
from modul_security import Security

class TransactionManager:
    @staticmethod
    def add_transaction(current_user, description, amount):
        """Menambah transaksi ke riwayat"""
        datetime_info = CoreUtils.get_current_datetime()
        
        if 'riwayat' not in current_user:
            current_user['riwayat'] = {}
        
        transaction = {
            "deskripsi": description,
            "jumlah": amount,
            "tanggal": datetime_info['date'],
            "waktu": datetime_info['time']
        }
        
        current_user['riwayat'].setdefault(datetime_info['date'], []).append(transaction)

    @staticmethod
    def check_balance(current_user):
        """Mengecek saldo"""
        print(f"Saldo Anda: {CoreUtils.format_rupiah(current_user['saldo'])}")

    @staticmethod
    def withdraw_money(current_user):
        """Penarikan uang"""
        while True:
            try:
                amount = int(input("Masukkan jumlah penarikan: "))
                if amount <= 0:
                    print("Jumlah harus lebih dari 1.")
                elif amount > current_user['saldo']:
                    print("Saldo tidak mencukupi.")
                else:
                    current_user['saldo'] -= amount
                    TransactionManager.add_transaction(current_user, "Tarik Tunai", -amount)
                    print(f"Penarikan berhasil. Saldo Anda sekarang: {CoreUtils.format_rupiah(current_user['saldo'])}")
                    return True
            except ValueError:
                print("Masukkan jumlah yang valid.")

    @staticmethod
    def deposit_money(current_user):
        """Setor uang"""
        while True:
            try:
                amount = int(input("Masukkan jumlah setoran: "))
                if amount <= 0:
                    print("Jumlah harus lebih dari 1.")
                else:
                    current_user['saldo'] += amount
                    TransactionManager.add_transaction(current_user, "Setor Tunai", amount)
                    print(f"Setoran berhasil. Saldo Anda sekarang: {CoreUtils.format_rupiah(current_user['saldo'])}")
                    return True
            except ValueError:
                print("Masukkan jumlah yang valid.")

    @staticmethod
    def transfer_money(current_user, users):
        """Transfer uang"""
        while True:
            target_account = input("Masukkan nomor rekening tujuan: ")

            if target_account == current_user['rekening']:
                print("Anda tidak bisa mentransfer ke rekening Anda sendiri.")
                continue

            recipient = next((user for user in users if user['rekening'] == target_account), None)

            if not recipient:
                retry = input("Akun tujuan tidak ditemukan. Apakah Anda ingin mencoba lagi? (y/n): ").lower()
                if retry != 'y':
                    return False
                continue

            try:
                amount = int(input("Masukkan jumlah transfer: "))
                if amount <= 0:
                    print("Jumlah harus lebih dari 1.")
                elif amount > current_user['saldo']:
                    print("Saldo tidak mencukupi.")
                else:
                    email = current_user.get('email')
                    if not email:
                        email = input("Masukkan email Anda untuk menerima OTP: ")
                        if not CoreUtils.validate_email(email):
                            print("Format email harus @gmail.com.")
                            return False
                        current_user['email'] = email

                    otp = Security.generate_otp()
                    if Security.send_otp_email(email, otp):
                        Security.store_otp(email, otp)

                        for _ in range(3):  # Give 3 attempts for OTP
                            try:
                                input_otp = int(input("Masukkan kode OTP yang dikirim ke email Anda: "))
                                if Security.validate_otp(email, input_otp):
                                    current_user['saldo'] -= amount
                                    recipient['saldo'] += amount
                                    TransactionManager.add_transaction(current_user, f"Transfer ke {recipient['identitas']}", -amount)
                                    TransactionManager.add_transaction(recipient, f"Transfer dari {current_user['identitas']}", amount)
                                    print(f"Transfer berhasil. Saldo Anda sekarang: {CoreUtils.format_rupiah(current_user['saldo'])}")
                                    return True
                                else:
                                    print("OTP tidak valid.")
                            except ValueError:
                                print("OTP harus berupa angka.")
                        print("Batas percobaan OTP terlampaui.")
                        return False
                    else:
                        print("Gagal mengirim OTP. Transfer dibatalkan.")
                        return False
            except ValueError:
                print("Masukkan jumlah yang valid.")

    @staticmethod
    def display_transaction_history(current_user):
        """Menampilkan riwayat transaksi"""
        if 'riwayat' not in current_user or not current_user['riwayat']:
            print("Belum ada riwayat transaksi.")
            return

        for date, transactions in current_user['riwayat'].items():
            print(f"\nTanggal: {date}")
            for transaction in transactions:
                print(f"  - {transaction['waktu']} | {transaction['deskripsi']} | {CoreUtils.format_rupiah(transaction['jumlah'])}")

    @staticmethod
    def display_account_info(current_user):
        """Menampilkan informasi akun"""
        print(f"Identitas: {current_user['identitas']}")
        print(f"Rekening: {current_user['rekening']}")
        print(f"Email: {current_user.get('email', 'Tidak ada email terdaftar')}")
