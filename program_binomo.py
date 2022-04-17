import argparse, os, sys
from merge_files import *

program_start = False
user_aktif = []

# Argparse
parser = argparse.ArgumentParser()
parser.add_argument("nama_folder", type=str,
                    help="melakukan loading data ke dalam sistem")
args = parser.parse_args()
nama_folder = args.nama_folder
directory = os.path.join(os.getcwd(), nama_folder)

if os.path.exists(directory):
    program_start = True
else:
    print('Folder "{}" tidak ditemukan.'.format(nama_folder))
    sys.exit(0)

list_user = []
list_game_di_toko = []
list_game_dipunya = []
list_riwayat = []

user_csv = os.path.join(directory, "user.csv")
game_csv = os.path.join(directory, "game.csv")
kepemilikan_csv = os.path.join(directory, "kepemilikan.csv")
riwayat_csv = os.path.join(directory, "riwayat.csv")

def load(path):
    with open(path, "r") as f:
        lines = f.read()
        list_line = split(lines, "\n")[1:]
        new_list = []
        for i in range(length(list_line)):
            line = split(list_line[i], ";")
            if length(line[0]) > 0:
                new_list = append(new_list, line)
    return new_list

list_user = load(user_csv)
list_game_di_toko = load(game_csv)
list_game_dipunya = load(kepemilikan_csv)
list_riwayat = load(riwayat_csv)

# print(list_user, list_game_di_toko, list_game_dipunya, list_riwayat)
print("\nLoading...")
print('Selamat datang di antarmuka "Binomo"')

while(True):
    perintah = input(">>> ")
    # Akses admin
    if perintah == "register":
        list_user = register(list_user, user_aktif)

    # Akses user dan admin
    elif perintah == "login":
        user_data = login(list_user)
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
        search_game_at_store(list_game_dipunya, list_game_di_toko, user_aktif)

    # Akses admin
    elif perintah == "topup":
        list_user, user_aktif = topup(list_user, user_aktif)

    # Akses user
    elif perintah == "riwayat":
        riwayat(nama_folder, user_aktif)

    # Akses user dan admin
    elif perintah == "help":
        help(user_aktif)

    # Akses user dan admin
    elif perintah == "save":
        save(list_user, list_game_di_toko, list_game_dipunya, list_riwayat, user_aktif)
        
    # Akses user dan admin
    elif perintah == "exit":
        exit(list_user, list_game_di_toko, list_game_dipunya, list_riwayat, user_aktif)

    # print(user_aktif)
    print(list_user)
    print(list_game_di_toko)
    print(list_game_dipunya)
    print(list_riwayat)