from functions import *

def tictactoe(user_data):
    if user_data != []:
        turn = 0
        player = ""
        papan = [["#" for i in range(3)] for j in range(3)]

        print("Legenda:",
            "\n# Kosong",
            "\nX Pemain 1",
            "\nO Pemain 2",
            "\n\nStatus Papan")

        # Cetak papan
        for i in range(length(papan)):
            for j in range(length(papan[i])):
                print(papan[i][j], end="")
            print()
            
        while turn < 9:
            if turn % 2 == 0:
                player = "X"
            else:
                player = "O"
            
            print('\nGiliran Pemain "{}"'.format(player))
            x = int(input("X: "))
            y = int(input("Y: "))
            
            if x > length(papan) or y > length(papan):
                print("Kotak tidak valid.")
            else:
                for i in range(length(papan)):
                    for j in range(length(papan[i])):
                        if (i + 1) == y and (j + 1) == x:
                            if papan[i][j] == "#":
                                papan[i][j] = player
                                turn += 1
                            else:
                                print("Kotak sudah terisi. Silakan pilih kotak lain.")

                # Cetak papan
                for i in range(length(papan)):
                    for j in range(length(papan[i])):
                        print(papan[i][j], end="")
                    print()

                # Tidak ada kata-kata jika menang secara (diagonal dan horizontal), (diagonal dan vertikal), atau (horizontal dan vertikal)
                # Cek apakah ada yang menang
                if (papan[0][0] == papan[1][1] == papan[2][2]  and papan[0][0] != "#") or (papan[0][2] == papan[1][1] == papan[2][0] and papan[0][2] != "#"):
                    print(player, "menang secara diagonal.")
                    break
                elif (papan[0][0] == papan[0][1] == papan[0][2] and papan[0][0] != "#") or (papan[1][0] == papan[1][1] == papan[1][2] and papan[1][0] != "#") or (papan[2][0] == papan[2][1] == papan[2][2] and papan[2][0] != "#"):
                    print(player, "menang secara horizontal.")
                    break
                elif (papan[0][0] == papan[1][0] == papan[2][0] and papan[0][0] != "#") or (papan[0][1] == papan[1][1] == papan[2][1] and papan[0][1] != "#") or (papan[0][2] == papan[1][2] == papan[2][2] and papan[0][2] != "#"):
                    print(player, "menang secara vertikal.")
                    break
        else:
            print("Seri. Tidak ada yang menang.")
    else:
        print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login".')