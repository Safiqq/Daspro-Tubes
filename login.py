from function import *
from cipher import *

def login(list_user):
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    checker = False
    for i in range(length(list_user)):
        # list_user[i][1] = username
        # list_user[i][2] = nama
        # list_user[i][3] = password
        if list_user[i][1] == username:
            if cipher(list_user[i][3], "decrypt") == password:
                print("Halo", list_user[i][2] + '! Selamat datang di "Binomo".')
                checker = True
                return list_user[i]
    if not checker:
        print("Password atau username salah atau tidak ditemukan.")
        return