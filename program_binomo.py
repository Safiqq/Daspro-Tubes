import os
from merge_files import *

nama_folder = validasi_arg()
program_start = validasi_folder(nama_folder)

# Inisialisasi array
user_aktif = []
list_user = []
list_game_di_toko = []
list_game_dipunya = []
list_riwayat = []

# Path untuk tiap file
user_csv = os.path.join(nama_folder, "user.csv")
game_csv = os.path.join(nama_folder, "game.csv")
kepemilikan_csv = os.path.join(nama_folder, "kepemilikan.csv")
riwayat_csv = os.path.join(nama_folder, "riwayat.csv")

# Convert data pada csv menjadi bentuk array
list_user = load(user_csv)
list_game_di_toko = load(game_csv)
list_game_dipunya = load(kepemilikan_csv)
list_riwayat = load(riwayat_csv)

clear(user_aktif, list_user, list_game_di_toko, list_game_dipunya)
print('Selamat datang di antarmuka "Binomo"')

while(True):
    perintah = input(">>> ")
    clear(user_aktif, list_user, list_game_di_toko, list_game_dipunya)

    # Akses admin
    if perintah == "register":
        list_user = register(list_user, user_aktif)

    # Akses user dan admin
    elif perintah == "login":
        user_data = login(list_user, user_csv)
        if user_data:
            user_aktif = user_data

    # Akses admin
    elif perintah == "tambah_game":
        list_game_di_toko = tambah_game(list_game_di_toko, user_aktif)

    # Akses admin
    elif perintah == "ubah_game":
        list_game_di_toko = ubah_game(list_game_di_toko, user_aktif)

    # Akses admin
    elif perintah == "ubah_stok":
        list_game_di_toko = ubah_stok(list_game_di_toko, user_aktif)

    # Akses user dan admin
    elif perintah == "list_game_toko":
        list_game_toko(list_game_di_toko, user_aktif)

    # Akses user
    elif perintah == "buy_game":
        result = buy_game(list_game_dipunya, list_game_di_toko, list_riwayat, user_aktif)
        list_game_dipunya, list_game_di_toko, list_riwayat, user_aktif = result
        if user_aktif != []:
            for i in range(length(list_user)):
                # list_user[i][0] = id user
                if list_user[i][0] == user_aktif[0]:
                    list_user[i] = user_aktif

    # Akses user
    elif perintah == "list_game":
        list_game(list_game_dipunya, list_game_di_toko, user_aktif)

    # Akses user
    elif perintah == "search_my_game":
        search_my_game(list_game_dipunya, list_game_di_toko, user_aktif)

    # Akses user dan admin
    elif perintah == "search_game_at_store":
        search_game_at_store(list_game_di_toko, user_aktif)

    # Akses admin
    elif perintah == "topup":
        list_user, user_aktif = topup(list_user, user_aktif)

    # Akses user
    elif perintah == "riwayat":
        riwayat(list_riwayat, user_aktif)

    # Akses user dan admin
    elif perintah == "help":
        help(user_aktif)

    # Akses user dan admin
    elif perintah == "save":
        save(list_user, list_game_di_toko, list_game_dipunya, list_riwayat, user_aktif)
        
    # Akses user dan admin
    elif perintah == "exit":
        exit(list_user, list_game_di_toko, list_game_dipunya, list_riwayat, user_aktif)

    # Bonus
    elif perintah == "cipher":
        cipher_input(user_aktif)
    elif perintah == "kerangajaib":
        kerangajaib(user_aktif)
    elif perintah == "tictactoe":
        tictactoe(user_aktif)

    else:
        print("Ketik help untuk melihat fungsi-fungsi yang tersedia")
    
    # print(user_aktif)
    # print(list_user)
    # print(list_game_di_toko)
    # print(list_game_dipunya)
    # print(list_riwayat)