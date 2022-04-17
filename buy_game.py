from functions import *
import datetime

def buy_game(list_game, list_game_di_toko, list_riwayat, user_data):
    # Sudah login
    if user_data != []:
        is_admin = validasi_akses(user_data)
        if not is_admin:
            id_game = input("Masukkan ID Game: ")
            checker_1 = False
            idx_1 = -1
            checker_2 = False
            idx_2 = -1

            for i in range(length(list_game_di_toko)):
                if id_game == list_game_di_toko[i][0]:
                    checker_1 = True
                    idx_1 = i
            for i in range(length(list_game)):
                if id_game == list_game[i][0]:
                    checker_2 = True
                    idx_2 = i
            
            if checker_1:
                if checker_2:
                    print("Anda sudah memiliki Game tersebut!")
                else:
                    # user_data[5] = saldo
                    # list_game_di_toko[i][4] = harga
                    # list_game_di_toko[i][5] = stok
                    harga = convert(list_game_di_toko[idx_1][4], int)
                    if list_game_di_toko[idx_1][5] > 0:
                        if user_data[5] >= harga:
                            user_data[5] -= harga
                            list_game_di_toko[idx_1][5] -= 1
                            riwayat = [id_game, list_game_di_toko[idx_1][1], list_game_di_toko[idx_1][4], user_data[0], datetime.datetime.now().strftime("%Y")]
                            list_riwayat = append(list_riwayat, riwayat)
                            print('Game "' + list_game[idx_2][1] + '" berhasil dibeli!')
                        else:
                            print("Saldo anda tidak cukup untuk membeli game tersebut!")
                    else:
                        print("Stok game tersebut sedang habis!")
            else:
                # Tidak ada game
                print("Tidak ada game dengan ID tersebut!")
        else:
            print("Perintah gagal dilaksanakan, Anda bukan user.")
    # Belum login
    else:
        print("Silakan lakukan login terlebih dahulu.")
    return (list_game, list_game_di_toko, list_riwayat, user_data)