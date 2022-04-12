from function import *

def tambah_game(list_game):
    nama_game = input("Masukkan nama game: ")
    kategori = input("Masukkan kategori: ")
    tahun_rilis = input("Masukkan tahun rilis: ")
    harga = input("Masukkan harga: ")
    stok_awal = input("Masukkan stok awal: ")

    while nama_game == "" or kategori == "" or tahun_rilis == "" or harga == "" or stok_awal == "":
        print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
        nama_game = input("Masukkan nama game: ")
        kategori = input("Masukkan kategori: ")
        tahun_rilis = input("Masukkan tahun rilis: ")
        harga = input("Masukkan harga: ")
        stok_awal = input("Masukkan stok awal: ")
    else:
        game_id = len(list_game) + 1
        if game_id < 10:
            game_id = "GAME00" + str(game_id)
        elif game_id < 100:
            game_id = "GAME0" + str(game_id)
        else:
            game_id = "GAME" + str(game_id)
        print("Selamat! Berhasil menambahkan game " + nama_game)
        new_game = [game_id, nama_game, kategori, tahun_rilis, harga, stok_awal]
        list_game = append(list_game, new_game)
        return list_game