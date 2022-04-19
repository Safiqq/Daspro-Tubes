import os
from functions import *

def save_file(directory, nama_file, array):
    path = os.path.join(directory, nama_file)
    title = ""
    if nama_file == "game.csv":
        title = "id;nama;kategori;tahun_rilis;harga;stok"
    elif nama_file == "kepemilikan.csv":
        title = "game_id;user_id"
    elif nama_file == "riwayat.csv":
        title = "game_id;nama;harga;user_id;tahun_beli"
    elif nama_file == "user.csv":
        title = "id;username;nama;password;role;saldo"
    for i in range(length(array)):
        array[i] = "\n" + join(array[i], ";")
    array = konkat([title], array)
    open(path, "w").writelines(array)

def save(list_user, list_game_di_toko, list_game_dipunya, list_riwayat, user_data):
    # Sudah login
    if user_data != []:
        nama_folder = input("Masukkan nama folder penyimpanan: ")
        directory = os.path.join(os.getcwd(), nama_folder)

        print("\nSaving...")
        if not os.path.exists(directory):
            os.mkdir(directory)

        save_file(directory, "user.csv", list_user)
        save_file(directory, "game.csv", list_game_di_toko)
        save_file(directory, "kepemilikan.csv", list_game_dipunya)
        save_file(directory, "riwayat.csv", list_riwayat)

        print("Data telah disimpan pada folder", nama_folder)
    # Belum login
    else:
        print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login".')