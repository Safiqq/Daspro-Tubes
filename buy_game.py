from functions import *
import datetime

def buy_game(list_game, list_game_di_toko, list_riwayat, user_data):
    # Sudah login
    if user_data != []:
        is_admin = validasi_akses(user_data)
        if not is_admin:
            id_game = input("Masukkan ID Game: ")
            print()

            is_dipunya = validasi_game_dipunya(list_game, id_game, user_data)
            is_game_toko = validasi_game_toko(list_game_di_toko, id_game)

            if is_game_toko:
                if not is_dipunya:
                    index = get_game_index(list_game_di_toko, id_game)
                    game_data = list_game_di_toko[index]
                    # user_data[5] = saldo
                    # list_game_di_toko[i][1] = nama
                    # list_game_di_toko[i][4] = harga
                    # list_game_di_toko[i][5] = stok

                    # Cek stok
                    stok = int(game_data[5])
                    if stok > 0:
                        # Kurangi stok
                        list_game_di_toko[index][5] = str(stok - 1)

                        # Cek saldo
                        saldo = int(user_data[5])
                        harga = convert(game_data[4], int)
                        if saldo >= harga:
                            # Kurangi saldo
                            user_data[5] = str(saldo - harga)

                            riwayat = [id_game, game_data[1], game_data[4], user_data[0], datetime.datetime.now().strftime("%Y")]
                            list_riwayat = append(list_riwayat, riwayat)
                            game = [id_game, user_data[0]]
                            list_game = append(list_game, game)
                            print('Game "' + game_data[1] + '" berhasil dibeli!')
                        else:
                            print("Saldo anda tidak cukup untuk membeli game tersebut!")
                    else:
                        print("Stok game tersebut sedang habis!")
                else:
                    print("Anda sudah memiliki game tersebut!")
            else:
                print("Tidak ada game dengan ID tersebut!")
        else:
            print("Maaf, anda harus menjadi user untuk melakukan hal tersebut.")
    # Belum login
    else:
        print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login".')
    return (list_game, list_game_di_toko, list_riwayat, user_data)