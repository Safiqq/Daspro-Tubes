from functions import *

def topup(list_user, user_data):
    # Sudah login
    if user_data != []:
        is_admin = validasi_akses(user_data)
        if is_admin:
            username = input("Masukkan username: ")
            saldo_masukan = input("Masukkan saldo: ")
            print()

            # Cek apakah username ditemukan
            is_user = validasi_user(list_user, username)
            if is_user:
                for i in range(length(list_user)):
                    # list_user[i][1] = username
                    # list_user[i][4] = role
                    # list_user[i][5] = saldo
                    if list_user[i][1] == username:
                        if list_user[i][4] == "user":
                            curr_saldo = int(list_user[i][5])
                            saldo_akhir = int(saldo_masukan) + curr_saldo
                            if saldo_akhir < 0:
                                print("Masukan tidak valid.")
                            else:
                                list_user[i][5] = str(saldo_akhir)
                                if int(saldo_masukan) > 0:
                                    print("Top up berhasil. Saldo", username, "bertambah menjadi", str(saldo_akhir) + ".")
                                else:
                                    print("Top up berhasil. Saldo", username, "berkurang menjadi", str(saldo_akhir) + ".")
                        else:
                            print("Gagal top up. Hanya bisa melakukan top up ke akun dengan role user.")
            else:
                print('Username "' + username + '" tidak ditemukan.')
        else:
            print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
    # Belum login
    else:
        print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login".')
    return (list_user, user_data)