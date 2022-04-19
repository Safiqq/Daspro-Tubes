from functions import *

def search_my_game(list_game_dipunya, list_game_toko, user_data):
    # Sudah login
    if user_data != []:
        is_admin = validasi_akses(user_data)
        if not is_admin:
            id_game = input("Masukkan ID Game: ")
            tahun_rilis = input("Masukkan Tahun Rilis Game: ")
            print("\nDaftar game pada inventory yang memenuhi kriteria:")

            list_game_dipunya_user = []
            list_id_game_dipunya = get_id_game_owned(list_game_dipunya, user_data)
            for i in range(length(list_id_game_dipunya)):
                index = get_game_index(list_game_toko, list_id_game_dipunya[i])
                # list_game_dipunya_user = append(list_game_dipunya_user, list_game_toko[index])

                game_data = list_game_toko[index]
                # Cek apakah game sesuai dengan input yang diminta
                if id_game:
                    if game_data[0] == id_game:
                        list_game_dipunya_user = append(list_game_dipunya_user, game_data)
                elif tahun_rilis:
                    if game_data[3] == tahun_rilis:
                        list_game_dipunya_user = append(list_game_dipunya_user, game_data)
                else:
                    list_game_dipunya_user = append(list_game_dipunya_user, game_data)

            # Tampilkan ke layar sesuai format
            if length(list_game_dipunya_user) > 0:
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
                print("Tidak ada game pada inventory-mu yang memenuhi kriteria.")
        else:
            print("Maaf, anda harus menjadi user untuk melakukan hal tersebut.")
    # Belum login
    else:
        print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login".')