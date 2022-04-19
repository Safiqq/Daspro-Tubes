from functions import *

def list_game(list_game_dipunya, list_game_toko, user_data):
    # Sudah login
    if user_data != []:
        is_admin = validasi_akses(user_data)
        if not is_admin:
            list_game_dipunya_user = []
            list_id_game_dipunya = get_id_game_owned(list_game_dipunya, user_data)
            for i in range(length(list_id_game_dipunya)):
                index = get_game_index(list_game_toko, list_id_game_dipunya[i])
                list_game_dipunya_user = append(list_game_dipunya_user, list_game_toko[index])

            # Tampilkan ke layar sesuai format
            if length(list_game_dipunya_user) > 0:
                print("Daftar game:")
                # 1 untuk nama, 2 untuk kategori
                space_max_1 = space_max(list_game_dipunya_user, 1)
                space_max_2 = space_max(list_game_dipunya_user, 2)
                for i in range(length(list_game_dipunya_user)):
                    string = ""
                    space_count_1 = space_max_1 - length(list_game_dipunya_user[i][1])
                    space_count_2 = space_max_2 - length(list_game_dipunya_user[i][2])
                    string += str(i + 1) + ". " + list_game_dipunya_user[i][0] + " | " + list_game_dipunya_user[i][1] + (" " * space_count_1) + " | "
                    string += list_game_dipunya_user[i][2] + (" " * space_count_2) + " | " + list_game_dipunya_user[i][3] + " | " + list_game_dipunya_user[i][4]
                    print(string)
            else:
                print("Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli.")
        else:
            print("Maaf, anda harus menjadi user untuk melakukan hal tersebut.")
    # Belum login
    else:
        print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login".')