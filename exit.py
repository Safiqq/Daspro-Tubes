import sys
from save import *

def exit(list_user, list_game_di_toko, list_game_dipunya, list_riwayat, user_data):
    # Sudah login
    if user_data != []:
        confirm = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (Y/n): ").lower()
        confirm = ord(confirm)

        # Cek apakah input adalah bukan y atau n
        while confirm < 110 or 110 < confirm < 121 or confirm > 121:
            confirm = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (Y/n): ")
        # Input adalah y atau n
        else:
            confirm = chr(confirm)
            if confirm.lower() == "y":
                save(list_user, list_game_di_toko, list_game_dipunya, list_riwayat, user_data)
            sys.exit(0)
    # Belum login
    else:
        print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login".')