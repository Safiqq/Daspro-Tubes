from functions import *
import os, argparse, sys

def validasi_arg():
    parser = argparse.ArgumentParser()
    # Cek apakah ada argumen <nama_folder> yang digunakan
    parser.add_argument("nama_folder", type=str,
                        help="melakukan loading data ke dalam sistem")
    args = parser.parse_args()
    nama_folder = args.nama_folder
    return nama_folder

def validasi_folder(nama_folder):
    program_start = False
    # Cek apakah folder sudah ada
    if os.path.exists(nama_folder):
        program_start = True
    # Folder tidak ada
    else:
        print('Folder "{}" tidak ditemukan.'.format(nama_folder))
        sys.exit(0)
    return program_start

def load(path):
    with open(path, "r") as f:
        lines = f.read()
        list_line = split(lines, "\n")
        list_line = slicing(list_line, 1, 999)
        new_list = []
        for i in range(length(list_line)):
            line = split(list_line[i], ";")
            if length(line[0]) > 0:
                new_list = append(new_list, line)
    return new_list