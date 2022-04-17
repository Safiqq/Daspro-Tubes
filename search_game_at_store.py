from functions import *

def search_game_at_store(list_game_toko, user_data):
    # Sudah login
    if user_data != []:
        id_game = input("Masukkan ID Game: ")
        nama = input("Masukkan Nama Game: ")
        harga = input("Masukkan Harga Game: ")
        kategori = input("Masukkan Kategori Game: ")
        tahun_rilis = input("Masukkan Tahun Rilis Game: ")

        new_list_game = []
        # Cari game sesuai input
        for i in range(length(list_game_toko)):
            for j in range(length(list_game_toko)):
                # Cek apakah game sesuai dengan input yang diminta
                if id_game != "":
                    if list_game_toko[j][0] == id_game:
                        new_list_game = append(new_list_game, list_game_toko[j])
                elif nama != "":
                    if list_game_toko[j][1] == nama:
                        new_list_game = append(new_list_game, list_game_toko[j])
                elif harga != "":
                    if list_game_toko[j][4] == harga:
                        new_list_game = append(new_list_game, list_game_toko[j])
                elif kategori != "":
                    if list_game_toko[j][2] == kategori:
                        new_list_game = append(new_list_game, list_game_toko[j])
                elif tahun_rilis != "":
                    if list_game_toko[j][3] == tahun_rilis:
                        new_list_game = append(new_list_game, list_game_toko[j])
                else:
                    new_list_game = append(new_list_game, list_game_toko[j])

        # Tampilkan ke layar sesuai format
        if length(new_list_game) > 0:
            # space_max_1 untuk nama game
            # space_max_2 untuk kategori
            space_max_1 = 0
            space_max_2 = 0
            for i in range(length(new_list_game)):
                if space_max_1 < length(new_list_game[i][1]):
                    space_max_1 = length(new_list_game[i][1])
            for i in range(length(new_list_game)):
                if space_max_2 < length(new_list_game[i][2]):
                    space_max_2 = length(new_list_game[i][2])
            for i in range(length(new_list_game)):
                string = ""
                space_count_1 = space_max_1 - length(new_list_game[i][1])
                space_count_2 = space_max_2 - length(new_list_game[i][2])
                string += str(i + 1) + ". " + new_list_game[i][0] + " | " + new_list_game[i][1] + (" " * space_count_1) + " | "
                string += new_list_game[i][2] + (" " * space_count_2) + " | " + new_list_game[i][3] + " | " + new_list_game[i][4]
                print(string)
        else:
            print("Tidak ada game pada toko yang memenuhi kriteria.")
    # Belum login
    else:
        print("Silakan lakukan login terlebih dahulu.")