import os
from function import *

def riwayat(nama_folder, user_id):
    # path = os.getcwd() + "/" + nama_folder + "/" + "riwayat.csv"
    # path = os.path.join(os.getcwd(), nama_folder, "riwayat.csv")
    directory = os.path.abspath(os.getcwd())
    path = os.path.join(directory, nama_folder, "riwayat.csv")
    print(path)
    with open(path, "r") as f:
        space_max = 0
        lines = f.read()
        lines = split(lines, "\n")[1:]
        new_lines = []
        for i in range(length(lines)):
            line = split(lines[i], ",")
            if length(line[0]) > 0:
                if int(line[3]) == int(user_id):
                    for j in range(length(line)):
                        if j == 1 and space_max < length(line[j]):
                            space_max = length(line[j])
                    new_lines = append(new_lines, line)
        if length(new_lines) > 0:
            for i in range(length(new_lines)):
                string = ""
                for j in range(length(new_lines[i])):
                    if j != 3:
                        if j == 0:
                            string += str(i + 1) + ". " + new_lines[i][j] + " |"
                        elif j == 1:
                            space_count = space_max - length(new_lines[i][j])
                            string += " " + new_lines[i][j] + (" " * space_count) + " |"
                        else:
                            string += " " + new_lines[i][j] + " |"
                print(string)
        else:
            print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk membeli.")
            

riwayat("tes", 1)