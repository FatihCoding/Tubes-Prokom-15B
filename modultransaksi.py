import random

def buat_otp():
    """
    Membuat kode OTP acak 6 digit.
    Returns:
        int: Kode OTP.
    """
    return random.randint(100000, 999999)


def validasi_otp(otp, input_otp):
    """
    Validasi OTP yang dimasukkan pengguna.
    Args:
        otp (int): Kode OTP yang dihasilkan.
        input_otp (int): Kode OTP yang dimasukkan pengguna.

    Returns:
        bool: True jika valid, False jika tidak.
    """
    return otp == input_otp


def cek_saldo(current_user):
    """
    Menampilkan saldo pengguna.
    Args:
        current_user (dict): Data pengguna yang sedang aktif.
    """
    print(f"\nSaldo Anda saat ini: Rp {current_user['saldo']}")
    return f"Cek Saldo - Sisa saldo: Rp {current_user['saldo']}"


def tarik_uang(current_user, otp_input_func):
    """
    Melakukan penarikan uang dari akun pengguna.
    Args:
        current_user (dict): Data pengguna yang sedang aktif.
        otp_input_func (callable): Fungsi untuk memasukkan kode OTP.

    Returns:
        str or None: Ringkasan transaksi jika berhasil, None jika gagal.
    """
    jumlah = int(input("\nMasukkan jumlah penarikan: Rp "))
    if jumlah > current_user['saldo']:
        print("Saldo tidak mencukupi.")
        return None
    otp = buat_otp()
    print(f"Kode OTP Anda: {otp}")
    otp_input = otp_input_func("Masukkan kode OTP untuk melanjutkan: ")
    if validasi_otp(otp, otp_input):
        current_user['saldo'] -= jumlah
        print(f"Penarikan berhasil. Saldo Anda sekarang: Rp {current_user['saldo']}")
        riwayat = f"Penarikan - Rp {jumlah}"
        current_user.setdefault('riwayat', []).append(riwayat)
        return riwayat
    print("Kode OTP salah. Penarikan dibatalkan.")
    return None


def setor_tunai(current_user):
    """
    Menambahkan saldo ke akun pengguna.
    Args:
        current_user (dict): Data pengguna yang sedang aktif.

    Returns:
        str: Ringkasan transaksi.
    """
    jumlah = int(input("\nMasukkan jumlah setoran: Rp "))
    current_user['saldo'] += jumlah
    print(f"Setor tunai berhasil. Saldo Anda sekarang: Rp {current_user['saldo']}")
    riwayat = f"Setor Tunai - Rp {jumlah}"
    current_user.setdefault('riwayat', []).append(riwayat)
    return riwayat


def transfer_uang(current_user, users):
    """
    Melakukan transfer uang ke pengguna lain.
    Args:
        current_user (dict): Data pengguna yang sedang aktif.
        users (list): Daftar pengguna lain.

    Returns:
        str or None: Ringkasan transaksi jika berhasil, None jika gagal.
    """
    rekening_tujuan = input("\nMasukkan nomor rekening tujuan: ")
    penerima = next((user for user in users if user['rekening'] == rekening_tujuan), None)
    if not penerima:
        print("Rekening tujuan tidak ditemukan.")
        return None

    jumlah = int(input("Masukkan jumlah transfer: Rp "))
    if jumlah > current_user['saldo']:
        print("Saldo tidak mencukupi.")
        return None

    otp = buat_otp()
    print(f"Kode OTP Anda: {otp}")
    otp_input = int(input("Masukkan kode OTP untuk melanjutkan: "))
    if validasi_otp(otp, otp_input):
        current_user['saldo'] -= jumlah
        penerima['saldo'] += jumlah
        print(f"Transfer berhasil. Saldo Anda sekarang: Rp {current_user['saldo']}")

        riwayat_pengirim = f"Transfer - Rp {jumlah} ke {penerima['identitas']} ({penerima['rekening']})"
        current_user.setdefault('riwayat', []).append(riwayat_pengirim)

        riwayat_penerima = f"Transfer Masuk - Rp {jumlah} dari {current_user['identitas']} ({current_user['rekening']})"
        penerima.setdefault('riwayat', []).append(riwayat_penerima)

        return riwayat_pengirim
    print("Kode OTP salah. Transfer dibatalkan.")
    return None


def ganti_pin(current_user):
    """
    Mengganti PIN akun pengguna.
    Args:
        current_user (dict): Data pengguna yang sedang aktif.

    Returns:
        str or None: Ringkasan aksi jika berhasil, None jika gagal.
    """
    pin_baru = input("\nMasukkan PIN baru Anda (6 digit): ")
    if len(pin_baru) == 6 and pin_baru.isdigit():
        current_user['pin'] = pin_baru
        print("PIN berhasil diubah.")
        return "Ganti PIN"
    print("PIN tidak valid. Ganti PIN gagal.")
    return None
