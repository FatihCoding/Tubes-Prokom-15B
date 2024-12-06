import json

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

def cari_akun(rekening, pin, users):
    for user in users:
        if user['rekening'] == rekening and user['pin'] == pin:
            return user
    return None
