import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
from modul_core_utils import CoreUtils

class Security:
    otp_storage = {}

    @staticmethod
    def generate_otp():
        """Menghasilkan kode OTP"""
        return random.randint(100000, 999999)

    @staticmethod
    def send_otp_email(email, otp):
        """Mengirim OTP melalui email"""
        sender_email = "bankfatisda@gmail.com"
        sender_password = "brig ksra ireu mnfe"

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
                return True
        except Exception as e:
            print(f"Gagal mengirim email: {e}")
            return False

    @classmethod
    def store_otp(cls, email, otp):
        """Menyimpan OTP dengan waktu kedaluwarsa"""
        expiration_time = datetime.now() + timedelta(minutes=5)
        cls.otp_storage[email] = {
            "otp": otp,
            "expires_at": expiration_time
        }

    @classmethod
    def validate_otp(cls, email, input_otp):
        """Validasi OTP yang dimasukkan"""
        if email not in cls.otp_storage:
            return False

        stored_otp = cls.otp_storage[email]
        if datetime.now() > stored_otp["expires_at"]:
            del cls.otp_storage[email]
            return False

        if stored_otp["otp"] != input_otp:
            return False

        del cls.otp_storage[email]
        return True

    @staticmethod
    def handle_forgot_pin(users):
        """Menangani lupa PIN"""
        email = input("Masukkan email terdaftar Anda: ")
        if not CoreUtils.validate_email(email):
            print("Format email harus @gmail.com.")
            return False

        user = CoreUtils.find_account_by_email(email, users)
        if not user:
            print("Email tidak ditemukan.")
            return False

        otp = Security.generate_otp()
        if Security.send_otp_email(email, otp):
            Security.store_otp(email, otp)
            
            for _ in range(3):
                try:
                    input_otp = int(input("Masukkan kode OTP: "))
                    if Security.validate_otp(email, input_otp):
                        while True:
                            new_pin = input("Masukkan PIN baru (6 digit): ")
                            if CoreUtils.validate_pin(new_pin):
                                user['pin'] = new_pin
                                print("PIN berhasil direset.")
                                return True
                            else:
                                print("PIN harus 6 digit.")
                except ValueError:
                    print("OTP harus berupa angka.")
        print("Gagal mereset PIN.")
        return False

    @staticmethod
    def change_pin(current_user):
        """Mengubah PIN"""
        old_pin = input("Masukkan PIN lama: ")
        if old_pin == current_user['pin']:
            while True:
                new_pin = input("Masukkan PIN baru (6 digit): ")
                if CoreUtils.validate_pin(new_pin):
                    current_user['pin'] = new_pin
                    print("PIN berhasil diubah.")
                    break
                else:
                    print("PIN harus 6 digit.")
        else:
            print("PIN lama salah.")
