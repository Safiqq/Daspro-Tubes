from function import *

def topup(list_user):
    username = input("Masukkan username: ")
    saldo = input("Masukkan saldo: ")
    # Cek apakah username ditemukan
    checker = False

    for i in range(length(list_user)):
        # list_user[i][1] = username
        # list_user[i][5] = saldo
        if list_user[i][1] == username:
            checker = True
            saldo_akhir = int(saldo) + int(list_user[i][5])
            if saldo_akhir < 0:
                print("Masukan tidak valid.")
            else:
                list_user[i][5] = saldo_akhir
                if int(saldo) > 0:
                    print("Top up berhasil. Saldo", username, "bertambah menjadi", saldo_akhir + ".")
                else:
                    print("Top up berhasil.Saldo", username, "berkurang menjadi", saldo_akhir + ".")
    if not checker:
        print('Username "' + username + '" tidak ditemukan.')