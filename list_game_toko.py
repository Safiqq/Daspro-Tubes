from functions import *

def sort_by_index(list_game, index, order):
    new_list_game = []
    for i in range(length(list_game)):
        element = list_game[i][index]
        if index == 0:
            element = slicing(element, 4, 999)
        elif index == 4:
            element = convert(element, int)
        new_list_game = append(new_list_game, element)
    new_list_game = sort(new_list_game, order)
    return new_list_game

# Kalo input kosong jadi sort berdasarkan id dari paling kecil (di atas) sampai paling besar (di bawah)
def list_game_toko(list_game, user_data):
    # Sudah login
    if user_data != []:
        skema = input("Skema sorting: ")
        print()

        if length(list_game) > 0:
            checker = True
            index = 0
            order = "+"

            print(skema)
            if skema:
                # list_game[i][3] = tahun
                # list_game[i][4] = harga
                if skema == "tahun-" or skema == "tahun+":
                    index = 3
                elif skema == "harga-" or skema == "harga+":
                    index = 4
                else:
                    checker = False
            if checker:
                if length(skema) == 6:
                    order = skema[5]
                to_be_sorted = sort_by_index(list_game, index, order)
                sorted_list = []

                if index == 4:
                    for i in range(length(to_be_sorted)):
                        to_be_sorted[i] = convert(to_be_sorted[i], str)

                for i in range(length(to_be_sorted)):
                    for j in range(length(list_game)):
                        if to_be_sorted[i] == list_game[j][index]:
                            sorted_list = append(sorted_list, list_game[j])
                
                # 1 untuk nama, 2 untuk kategori, 4 untuk harga
                space_max_1 = space_max(sorted_list, 1)
                space_max_2 = space_max(sorted_list, 2)
                space_max_3 = space_max(sorted_list, 4)

                for i in range(length(sorted_list)):
                    string = ""
                    space_count_1 = space_max_1 - length(sorted_list[i][1])
                    space_count_2 = space_max_2 - length(sorted_list[i][2])
                    space_count_3 = space_max_3 - length(sorted_list[i][4])
                    string += str(i + 1) + ". " + sorted_list[i][0] + " | " + sorted_list[i][1] + (" " * space_count_1) + " | "
                    string += sorted_list[i][4] + (" " * space_count_3) + " | " + sorted_list[i][2] + (" " * space_count_2) + " | "
                    string += sorted_list[i][3] + " | " + sorted_list[i][5]
                    print(string)
            else:
                print("Skema sorting tidak valid!")
        else:
            print("Tidak ada game pada toko.")
    # Belum login
    else:
        print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login".')