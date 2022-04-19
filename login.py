from functions import *
from cipher import *
from load import *

def validasi_password(list_user, username, password):
    # list_user[i][1] = username
    # list_user[i][2] = nama
    # list_user[i][3] = password
    for i in range(length(list_user)):
        if list_user[i][1] == username:
            decrypted = cipher(list_user[i][3], "decrypt")
            if decrypted == password:
                return list_user[i]
    return

def login(list_user, path):
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    print()

    list_user_file = load(path)
    is_valid = validasi_password(list_user, username, password)
    is_valid_file = validasi_password(list_user_file, username, password)

    if is_valid:
        if is_valid_file:
            print("Halo", is_valid_file[2] + '! Selamat datang di "Binomo".')
            return is_valid_file
        else:
            print("Akun dengan username", username, "masih berstatus temporary. Silakan lakukan save terlebih dahulu dan login kembali.")
            return
    else:
        print("Password atau username salah atau tidak ditemukan.")
        return