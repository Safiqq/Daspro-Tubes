from functions import *

def ubah_game(list_game_toko, user_data):
    # Sudah login
    if user_data != []:
        is_admin = validasi_akses(user_data)
        if is_admin:
            id_game = input("Masukkan ID game: ")
            nama_game = input("Masukkan nama game: ")
            kategori = input("Masukkan kategori: ")
            tahun_rilis = input("Masukkan tahun rilis: ")
            harga = input("Masukkan harga: ")
            print()

            array = []
            string = ""

            is_valid = validasi_game_toko(list_game_toko, id_game)
            if is_valid:
                for i in range(length(list_game_toko)):
                    if list_game_toko[i][0] == id_game:
                        if nama_game != "":
                            list_game_toko[i][1] = nama_game
                            array = append(array, "nama game")
                        if kategori != "":
                            list_game_toko[i][2] = kategori
                            array = append(array, "kategori")
                        if tahun_rilis != "":
                            list_game_toko[i][3] = tahun_rilis
                            array = append(array, "tahun rilis")
                        if harga != "":
                            list_game_toko[i][4] = harga
                            array = append(array, "harga")

                # Merapikan keluaran output
                for i in range(length(array)):
                    if array:
                        if i == 0:
                            string += array[i]
                        else:
                            if length(array) > 2:
                                string += ","
                            string += " "
                            if i == (length(array) - 1):
                                string += "dan "
                            string += array[i]

                if string:
                    print("Berhasil mengubah", string, "untuk game dengan ID", id_game + ".")
                else:
                    print("Tidak ada informasi yang diubah.")
            else:
                print("Tidak ada game dengan ID tersebut.")
        else:
            print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
    # Belum login
    else:
        print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login".')
    return list_game_toko