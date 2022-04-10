import os


def validateUser (nama_folder,userInfo):
    directory = os.path.abspath(os.getcwd())
    path = os.path.join(directory, nama_folder, "user.csv")
    print(path)
    # disini buat yang ngambil data dari file yang buat nge cek
    return 


def loginSequence (nama_folder):
    User = str(input('Masukan username: '))
    password = str(input('Masukan Password: '))

    userInfo = [User,password]
    
    validateUser(nama_folder,userInfo)

    return valid

