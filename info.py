from functions import *
import os, time

def info(user_aktif, list_user, list_game_di_toko, list_game_dipunya):
    count_game_dipunya = 0
    if list_game_dipunya != [] and user_aktif != []:
        for i in range(length(list_game_dipunya)):
            if list_game_dipunya[i][1] == user_aktif[0]:
                count_game_dipunya += 1
    if user_aktif != []:
        id_user = user_aktif[0]
        name = user_aktif[2]
        role = user_aktif[4]
        print("User yang sedang aktif: (ID" + id_user + ") " + name)
        if role == "user":
            print("Jumlah game dipunya user: " + str(count_game_dipunya))
    if list_user != []:
        count_user = 0
        count_admin = 0
        for i in range(length(list_user)):
            role = list_user[i][4]
            if role == "user":
                count_user += 1
            elif role == "admin":
                count_admin += 1
        print("Jumlah akun yang terdaftar: ", end="")
        if count_user > 0:
            print(str(count_user) + " user", end="")
            if count_admin > 0:
                print(", " +str(count_admin) + " admin")
        else:
            if count_admin > 0:
                print(str(count_admin) + " admin")
    if list_game_di_toko != []:
        jumlah_game_toko = str(length(list_game_di_toko))
        print("Jumlah game di toko: " + jumlah_game_toko)
    print()

def clear(user_aktif, list_user, list_game_di_toko, list_game_dipunya):
    os.system("clear||cls")
    string = ""
    for i in range(3):
        info(user_aktif, list_user, list_game_di_toko, list_game_dipunya)
        if string:
            string += ".. " + str(i + 1)
        else:
            string += "Loading...\n" + str(i + 1)
        print(string)
        time.sleep(0.2 * (i + 1))
        os.system("clear||cls")
    info(user_aktif, list_user, list_game_di_toko, list_game_dipunya)