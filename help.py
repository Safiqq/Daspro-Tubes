from functions import *

def help(user_data):
    # Sudah login
    if user_data != []:
        is_admin = validasi_akses(user_data)
        if is_admin:
            print("============ HELP ============",
                "1. register - Untuk melakukan registrasi user baru",
                "2. login - Untuk melakukan login ke dalam sistem",
                "3. tambah_game - Untuk menambah game yang dijual pada toko",
                "4. list_game_toko - Untuk melihat list game yang dijual pada toko")
            # dst.
        else:
            print("============ HELP ============",
                "1. login - Untuk melakukan login ke dalam sistem",
                "2. list_game_toko - Untuk melihat list game yang dijual pada toko")
            # dst.
    # Belum login
    else:
        print("============ HELP ============",
            "1. register - Untuk melakukan registrasi user baru",
            "2. login - Untuk melakukan login ke dalam sistem",
            "3. tambah_game - Untuk menambah game yang dijual pada toko",
            "4. list_game_toko - Untuk melihat list game yang dijual pada toko")
        # dst.
        print("============ HELP ============",
            "1. login - Untuk melakukan login ke dalam sistem",
            "2. list_game_toko - Untuk melihat list game yang dijual pada toko")
        # dst.