import os
from functions import *

def riwayat(list_riwayat, user_data):
    # Sudah login
    if user_data != []:
        is_admin = validasi_akses(user_data)
        if not is_admin:
            user_id = user_data[0]
            list_riwayat_user = []
            
            # game_id;nama;harga;user_id;tahun_beli
            for i in range(length(list_riwayat)):
                if list_riwayat[i][3] == user_id:
                    list_riwayat_user = append(list_riwayat_user, list_riwayat[i])
            
            # 1 untuk nama, 2 untuk harga
            space_max_1 = space_max(list_riwayat, 1)
            space_max_2 = space_max(list_riwayat, 2)
            if length(list_riwayat_user) > 0:
                print("Daftar game:")
                for i in range(length(list_riwayat_user)):
                    string = ""
                    count_space_1 = space_max_1 - length(list_riwayat_user[i][1])
                    count_space_2 = space_max_2 - length(list_riwayat_user[i][2])
                    string += str(i + 1) + ". " + list_riwayat_user[i][0] + " | " + list_riwayat_user[i][1] + (" " * count_space_1)
                    string += " | " + list_riwayat_user[i][2] + (" " * count_space_2) + " | " + list_riwayat_user[i][4] + " |"
                    print(string)
            else:
                print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk membeli.")
        else:
            print("Maaf, anda harus menjadi user untuk melakukan hal tersebut.")
    # Belum login
    else:
        print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login".')