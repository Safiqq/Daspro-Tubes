from function import *

def ubah_game(list_game):
    id_game = input("Masukkan ID game: ")
    nama_game = input("Masukkan nama game: ")
    kategori = input("Masukkan kategori: ")
    tahun_rilis = input("Masukkan tahun rilis: ")
    harga = input("Masukkan harga: ")

    for i in range(length(list_game)):
        # Belum ada validasi ID game
        if list_game[i][0] == id_game[0]:
            if nama_game != "":
                list_game[i][1] = nama_game
            if kategori != "":
                list_game[i][2] = kategori
            if tahun_rilis != "":
                list_game[i][3] = tahun_rilis
            if harga != "":
                list_game[i][4] = harga
    return list_game