import argparse, os

program_start = False

# Argparse
parser = argparse.ArgumentParser()
parser.add_argument("nama_folder", type=str,
                    help="melakukan loading data ke dalam sistem")
args = parser.parse_args()
nama_folder = args.nama_folder
directory = os.getcwd()

if program_start == True:
    print("\nLoading...")
    print('Selamat datang di antarmuka "Binomo"')

    while(True):
        perintah = input(">>> ")
        if perintah == "register":
            nama = input("Masukkan nama: ")
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")

            
else:
    print('Folder "{}" tidak ditemukan.'.format(nama_folder))