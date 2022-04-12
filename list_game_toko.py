from function import *

def list_game_toko(list_game):
    skema = input("Skema sorting: ")
    to_be_sorted = ["" for i in range(length(list_game))]
    sort_by = 0

    # Descending = -
    # Ascending = +
    tipe = skema[5]
    if tipe == "-":
        tipe = "d"
    elif tipe == "+":
        tipe = "a"
    checker = True

    # list_game[i][3] = tahun
    # list_game[i][4] = harga
    if skema[:5] == "tahun":
        sort_by = 3
    elif skema[:5] == "harga":
        sort_by = 4
    else:
        checker = False
        print("Skema sorting tidak valid!")

    if checker:
        for i in range(length(list_game)):
            to_be_sorted[i] = list_game[i][sort_by]
        to_be_sorted = sort(to_be_sorted, tipe)

        if length(list_game) > 0:
            # space_max_1 untuk nama game
            # space_max_2 untuk kategori
            # space_max_3 untuk harga
            space_max_1 = 0
            space_max_2 = 0
            space_max_3 = 0
            new_list_game = []
            count = length(list_game)

            for i in range(length(list_game)):
                if space_max_1 < length(list_game[i][1]):
                    space_max_1 = length(list_game[i][1])
            for i in range(length(list_game)):
                if space_max_2 < length(list_game[i][2]):
                    space_max_2 = length(list_game[i][2])
            for i in range(length(list_game)):
                if space_max_3 < length(list_game[i][4]):
                    space_max_3 = length(list_game[i][4])

            for i in range(length(to_be_sorted)):
                for j in range(length(list_game)):
                    if to_be_sorted[i] == list_game[j][sort_by]:
                        new_list_game = append(new_list_game, list_game[j])

            for i in range(length(new_list_game)):
                string = ""
                space_count_1 = space_max_1 - length(new_list_game[i][1])
                space_count_2 = space_max_2 - length(new_list_game[i][2])
                space_count_3 = space_max_2 - length(new_list_game[i][4])
                string += str(i + 1) + ". " + new_list_game[i][0] + " | " + new_list_game[i][1] + (" " * space_count_1) + " | "
                string += new_list_game[i][4] + (" " * space_count_3) + " | " + new_list_game[i][2] + (" " * space_count_2) + " | "
                string += new_list_game[i][3] + " | " + new_list_game[i][5]
                print(string)