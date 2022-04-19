from functions import *

def ubah_stok(list_game_toko, user_data):
    # Sudah login
    if user_data != []:
        is_admin = validasi_akses(user_data)
        if is_admin:
            id_game = input("Masukkan ID game: ")
            jumlah = input("Masukkan jumlah: ")
            print()

            is_valid = validasi_game_toko(list_game_toko, id_game)

            if is_valid:
                if jumlah:
                    for i in range(length(list_game_toko)):
                        if list_game_toko[i][0] == id_game:
                            stok = int(list_game_toko[i][5]) + int(jumlah)
                            if stok < 0:
                                print("Stok game " + list_game_toko[i][1] + " gagal dikurangi karena stok kurang. Stok sekarang: " + list_game_toko[i][5] + " (<" + str(abs(int(jumlah))) + ")")
                            else:
                                list_game_toko[i][5] = stok
                                # Belum ada jumlah == 0
                                if int(jumlah) > 0:
                                    print("Stok game", list_game_toko[i][1], "berhasil ditambahkan. Stok sekarang:", stok)
                                else:
                                    print("Stok game", list_game_toko[i][1], "berhasil dikurangi. Stok sekarang:", stok)
                else:
                    print("Tidak ada informasi yang diubah.")
            else:
                print("Tidak ada game dengan ID tersebut!")
        else:
            print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
    # Belum login
    else:
        print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login".')
    return list_game_toko