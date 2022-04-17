from functions import *

def topup(list_user, user_data):
    # Sudah login
    if user_data != []:
        is_admin = validasi_akses(user_data)
        if is_admin:
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
        else:
            print("Perintah gagal dilaksanakan, Anda bukan admin.")
    # Belum login
    else:
        print("Silakan lakukan login terlebih dahulu.")
    return (list_user, user_data)