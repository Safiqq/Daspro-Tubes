import os
from functions import *

def save(list_user, list_game_di_toko, list_game_dipunya, list_riwayat, user_data):
    # Sudah login
    if user_data != []:
        nama_folder = input("Masukkan nama folder penyimpanan: ")
        directory = os.path.join(os.getcwd(), nama_folder)

        print("\nSaving...")
        if not os.path.exists(directory):
            os.mkdir(directory)
        game_csv = os.path.join(directory, "game.csv")
        kepemilikan_csv = os.path.join(directory, "kepemilikan.csv")
        riwayat_csv = os.path.join(directory, "riwayat.csv")
        user_csv = os.path.join(directory, "user.csv")

        # Save game.csv
        lines_game_di_toko = ["" for i in range(length(list_game_di_toko) + 1)]
        lines_game_di_toko[0] = "id;nama;kategori;tahun_rilis;harga;stok"
        for i in range(length(list_game_di_toko)):
            lines_game_di_toko[i+1] = "\n" + join(list_game_di_toko[i], ";")
        open(game_csv, "w").writelines(lines_game_di_toko)
        
        # Save kepemilikan.csv
        lines_game_dipunya = ["" for i in range(length(list_game_dipunya) + 1)]
        lines_game_dipunya[0] = "game_id;user_id"
        for i in range(length(list_game_dipunya)):
            lines_game_dipunya[i+1] = "\n" + join(list_game_dipunya[i], ";")
        open(kepemilikan_csv, "w").writelines(lines_game_dipunya)

        # Save riwayat.csv
        lines_riwayat = ["" for i in range(length(list_riwayat) + 1)]
        lines_riwayat[0] = "game_id;nama;harga;user_id;tahun_beli"
        for i in range(length(list_riwayat)):
            lines_riwayat[i+1] = "\n" + join(list_riwayat[i], ";")
        open(riwayat_csv, "w").writelines(lines_riwayat)

        # Save user.csv
        lines_user = ["" for i in range(length(list_user) + 1)]
        lines_user[0] = "id;username;nama;password;role;saldo"
        for i in range(length(list_user)):
            lines_user[i+1] = "\n" + join(list_user[i], ";")
        open(user_csv, "w").writelines(lines_user)
        
        print("Data telah disimpan pada folder", nama_folder)
    # Belum login
    else:
        print("Silakan lakukan login terlebih dahulu.")

# save([], [['GAME001', 'BNMO - Play Along With Crypto', 'Adventure', '2022', '100.000', '1'], ['GAME002', 'Hehehe', 'Comedy', '2021', '100.000', '1'], ['GAME069', 'Python Gemink', 'Programming', '2001', '100.000', '1']], [], [])