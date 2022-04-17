import os
from functions import *

def riwayat(nama_folder, user_data):
    # Sudah login
    if user_data != []:
        is_admin = validasi_akses(user_data)
        if not is_admin:
            user_id = user_data[0]
            # path = os.getcwd() + "/" + nama_folder + "/" + "riwayat.csv"
            # path = os.path.join(os.getcwd(), nama_folder, "riwayat.csv")
            path = os.path.join(os.getcwd(), nama_folder, "riwayat.csv")
            with open(path, "r") as f:
                # space_max_1 untuk nama
                # space_max_2 untuk harga
                space_max_1 = 0
                space_max_2 = 0
                lines = f.read()
                list_line = split(lines, "\n")[1:]
                list_game = []
                for i in range(length(list_line)):
                    line = split(list_line[i], ";")
                    if length(line[0]) > 0:
                        if int(line[3]) == int(user_id):
                            if space_max_1 < length(line[1]):
                                space_max_1 = length(line[1])
                            if space_max_2 < length(line[2]):
                                space_max_2 = length(line[2])
                            list_game = append(list_game, line)
                if length(list_game) > 0:
                    for i in range(length(list_game)):
                        string = ""
                        count_space_1 = space_max_1 - length(list_game[i][1])
                        count_space_2 = space_max_2 - length(list_game[i][2])
                        string += str(i + 1) + ". " + list_game[i][0] + " | " + list_game[i][1] + (" " * count_space_1)
                        string += " | " + list_game[i][2] + (" " * count_space_2) + " | " + list_game[i][4] + " |"
                        print(string)
                else:
                    print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk membeli.")
        else:
            print("Perintah gagal dilaksanakan, Anda bukan user.")
    # Belum login
    else:
        print("Silakan lakukan login terlebih dahulu.")