import os
import json
from datetime import datetime

class CoreUtils:
    @staticmethod
    def clear_console():
        """Membersihkan layar konsol"""
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def format_rupiah(amount):
        """Format angka ke format Rupiah"""
        return f"Rp {amount:,.0f}".replace(",", ".")

    @staticmethod
    def validate_email(email):
        """Validasi format email"""
        return email.endswith("@gmail.com")

    @staticmethod
    def validate_pin(pin):
        """Validasi format PIN"""
        return len(pin) == 6 and pin.isdigit()

    @staticmethod
    def load_users(filename):
        """Memuat data pengguna dari file JSON"""
        try:
            with open(filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"File {filename} tidak ditemukan.")
            return []
        except json.JSONDecodeError:
            print("Error: Data pengguna tidak valid.")
            return []

    @staticmethod
    def save_users(filename, users):
        """Menyimpan data pengguna ke file JSON"""
        try:
            with open(filename, 'w') as file:
                json.dump(users, file, indent=4)
            return True
        except Exception as e:
            print(f"Error menyimpan data: {e}")
            return False

    @staticmethod
    def get_current_datetime():
        """Mendapatkan waktu dan tanggal saat ini"""
        now = datetime.now()
        return {
            'date': now.strftime("%Y-%m-%d"),
            'time': now.strftime("%H:%M:%S")
        }

    @staticmethod
    def find_account(account_number, pin, users):
        """Mencari akun berdasarkan nomor rekening dan PIN"""
        for user in users:
            if user['rekening'] == account_number and user['pin'] == pin:
                return user
        return None

    @staticmethod
    def find_account_by_email(email, users):
        """Mencari akun berdasarkan email"""
        for user in users:
            if user.get('email') == email:
                return user
        return None