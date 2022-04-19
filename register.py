from functions import *
from cipher import *

def validasi_input(nama, username, password):
    if length(nama) == 0 or length(username) == 0 or length(password) == 0:
        return False
    else:
        for i in username:
            i = i.lower()
            i = ord(i)
            # Cek apakah a-z atau A-Z
            if i < 97 or i > 122:
                # Cek apakah - atau _
                if i != 95 and i != 45:
                    # Cek apakah 0-9
                    if i < 48 or i > 57:
                        return False
        return True

def register(list_user, user_data):
    # Sudah login
    if user_data != []:
        # id;username;nama;password;role;saldo
        is_admin = validasi_akses(user_data)
        if is_admin:
            nama = input("Masukkan nama: ")
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")
            print()

            is_user = validasi_user(list_user, username)
            is_valid = validasi_input(nama, username, password)

            if is_valid and not is_user:
                user_id = str(length(list_user) + 1)
                password = cipher(password, "encrypt")
                new_user = [user_id, username, nama, password, "user", "0"]
                list_user = append(list_user, new_user)
                print("Username", username, 'telah berhasil register ke dalam "Binomo".')
            else:
                if not is_valid:
                    print("Gagal mendaftarkan pengguna baru. Username tidak valid")
                else:
                    if is_user:
                        print("Username", username, "sudah terpakai, silakan menggunakan username lain.")
        else:
            print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
    # Belum login
    else:
        print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login".')
    return list_user