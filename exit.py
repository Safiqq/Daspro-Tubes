import sys
from save import *

def exitt(list_user, list_game_di_toko, list_game_dipunya, list_riwayat, user_data):
    # Sudah login
    if user_data != []:
        confirm = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (Y/n) ")
        while confirm.lower() != "y" or confirm.lower() != "n":
            confirm = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (Y/n) ")
        if confirm.lower() == "y":
            save(list_user, list_game_di_toko, list_game_dipunya, list_riwayat, user_data)
        sys.exit(0)
    # Belum login
    else:
        print("Silakan lakukan login terlebih dahulu.")