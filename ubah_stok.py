from function import *

def ubah_stok(list_game):
    id_game = input("Masukkan ID game: ")
    jumlah = input("Masukkan jumlah: ")

    checker = False
    error = ""

    for i in range(length(list_game)):
        if list_game[i][0] == id_game[0]:
            checker = True
            stok = int(list_game[i][5]) + int(jumlah)
            if stok < 0:
                error = "Stok game " + list_game[i][1] + " gagal dikurangi karena stok kurang. Stok sekarang: " + list_game[i][5] + " (<" + abs(jumlah) + ")"
            else:
                list_game[i][5] = stok
                # Belum ada jumlah == 0
                if int(jumlah) > 0:
                    print("Stok game", list_game[i][1], "berhasil ditambahkan. Stok sekarang:", stok)
                else:
                    print("Stok game", list_game[i][1], "berhasil dikurangi. Stok sekarang:", stok)

    if not checker:
        error = "Tidak ada game dengan ID tersebut!"
    if error != "":
        print(error)
    return list_game