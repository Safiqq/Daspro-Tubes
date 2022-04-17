from functions import *
from cipher import *

def register(list_user, user_data):
    # Sudah login
    if user_data != []:
        # id;username;nama;password;role;saldo
        is_admin = validasi_akses(user_data)
        if is_admin:
            nama = input("Masukkan nama: ")
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")

            # Cek username tidak valid
            checker_1 = True
            # Cek username sudah ada
            checker_2 = False
            if length(nama) == 0 or length(username) == 0 or length(password) == 0:
                checker_1 = False
            for i in username:
                i = i.lower()
                i = ord(i)
                # Cek apakah a-z atau A-Z
                if i < 97 or i > 122:
                    # Cek apakah - atau _
                    if i != 95 and i != 45:
                        # Cek apakah 0-9
                        if i < 48 or i > 57:
                            print(chr(i))
                            checker_1 = False
            for i in list_user:
                if i[1] == username:
                    checker_2 = True

            if checker_1 and not checker_2:
                user_id = str(length(list_user) + 1)
                password = cipher(password, "encrypt")
                new_user = [user_id, username, nama, password, "user", "0"]
                list_user = append(list_user, new_user)
                print("Username", username, 'telah berhasil register ke dalam "Binomo".')
            else:
                if not checker_1:
                    print("Gagal mendaftarkan pengguna baru. Username tidak valid")
                else:
                    if checker_2:
                        print("Username", username, "sudah terpakai, silakan menggunakan username lain.")
        else:
            print("Perintah gagal dilaksanakan, Anda bukan admin.")
    # Belum login
    else:
        print("Silakan lakukan login terlebih dahulu.")
    return list_user