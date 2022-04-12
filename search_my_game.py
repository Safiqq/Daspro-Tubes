from function import *

def search_my_game(list_game_dipunya, list_game_toko, user_data):
    id_game = input("Masukkan ID Game: ")
    tahun_rilis = input("Masukkan Tahun Rilis Game: ")

    new_list_game = []
    list_game_dipunya_user = []
    # Cari id game yang dipunya user
    for i in range(length(list_game_dipunya)):
        # list_game_dipunya[i][1] = user id
        if list_game_dipunya[i][1] == user_data[0]:
            list_game_dipunya_user = append(list_game_dipunya_user, list_game_dipunya[i])
    # Cari info lengkap game yang dipunya user (dari id)
    for i in range(length(list_game_dipunya_user)):
        for j in range(length(list_game_toko)):
            if list_game_dipunya_user[i][0] == list_game_toko[j][0]:
                # Cek apakah game sesuai dengan input yang diminta
                if id_game != "":
                    if list_game_toko[j][0] == id_game:
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
        print("Tidak ada game pada inventory-mu yang memenuhi kriteria.")

# a = [["GAME001", "1"], ["GAME002", "1"], ["GAME001", "2"]]
# b = [['GAME001', 'BNMO - Play Along With Crypto', 'Adventure', '2022', '100.000', '1'], ['GAME002', 'Hehehe', 'Comedy', '2021', '100.000', '1'], ['GAME069', 'Python Gemink', 'Programming', '2001', '100.000', '1']]
# c = ["1", "admin", "Safiq", "jkndw", "admin", "999999"]
# search_my_game(a, b, c)