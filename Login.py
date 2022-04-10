import os


def validateUser (nama_folder,userInfo):
    directory = os.path.abspath(os.getcwd())
    path = os.path.join(directory, nama_folder, "user.csv")
    print(path)
    # disini buat yang ngambil data dari file yang buat nge cek ke user.csv
    if userInfo in path :
        validate= True
    else:
        validate= False
    return validate


def loginSequence (nama_folder):
    user = str(input('Masukan username: '))
    password = str(input('Masukan Password: '))

    while user == '' or password == '':
        print ('Silahkan masukkan username dan password terlebih dahulu')
        user = str(input('Masukan username: '))
        password = str(input('Masukan Password: '))

    userInfo = [user,password]
    
    acces=validateUser(nama_folder,userInfo) #ngecek user ada atau tidak

    return acces

