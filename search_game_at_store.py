from functions import *

def search_game_at_store(list_game_toko, user_data):
    # Sudah login
    if user_data != []:
        id_game = input("Masukkan ID Game: ")
        nama = input("Masukkan Nama Game: ")
        harga = input("Masukkan Harga Game: ")
        kategori = input("Masukkan Kategori Game: ")
        tahun_rilis = input("Masukkan Tahun Rilis Game: ")
        print("\nDaftar game pada toko yang memenuhi kriteria:")

        list_game = []

        # Cari game sesuai input
        for i in range(length(list_game_toko)):
            # Cek apakah game sesuai dengan input yang diminta
            if id_game != "":
                if list_game_toko[i][0] == id_game:
                    list_game = append(list_game, list_game_toko[i])
            elif nama != "":
                if list_game_toko[i][1] == nama:
                    list_game = append(list_game, list_game_toko[i])
            elif harga != "":
                if list_game_toko[i][4] == harga:
                    list_game = append(list_game, list_game_toko[i])
            elif kategori != "":
                if list_game_toko[i][2] == kategori:
                    list_game = append(list_game, list_game_toko[i])
            elif tahun_rilis != "":
                if list_game_toko[i][3] == tahun_rilis:
                    list_game = append(list_game, list_game_toko[i])
            else:
                list_game = append(list_game, list_game_toko[i])

        # Tampilkan ke layar sesuai format
        if length(list_game) > 0:
            # space_max_1 untuk nama game
            # space_max_2 untuk kategori
            space_max_1 = 0
            space_max_2 = 0
            for i in range(length(list_game)):
                if space_max_1 < length(list_game[i][1]):
                    space_max_1 = length(list_game[i][1])
            for i in range(length(list_game)):
                if space_max_2 < length(list_game[i][2]):
                    space_max_2 = length(list_game[i][2])
            for i in range(length(list_game)):
                string = ""
                space_count_1 = space_max_1 - length(list_game[i][1])
                space_count_2 = space_max_2 - length(list_game[i][2])
                string += str(i + 1) + ". " + list_game[i][0] + " | " + list_game[i][1] + (" " * space_count_1) + " | "
                string += list_game[i][2] + (" " * space_count_2) + " | " + list_game[i][3] + " | " + list_game[i][4]
                print(string)
        else:
            print("Tidak ada game pada toko yang memenuhi kriteria.")
    # Belum login
    else:
        print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login".')