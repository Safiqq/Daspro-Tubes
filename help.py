from functions import *

def help(user_data):
    # Sudah login
    if user_data != []:
        is_admin = validasi_akses(user_data)
        if is_admin:
            print("============ HELP ============",
                "\n1.  register - Untuk melakukan registrasi user baru",
                "\n2.  login - Untuk melakukan login ke dalam sistem",
                "\n3.  tambah_game - Untuk menambah game yang dijual pada toko",
                "\n4.  ubah_game - Untuk mengubah informasi mengenai sebuah game pada toko",
                "\n5.  ubah_stok - Untuk mengubah stok sebuah game pada toko",
                "\n6.  list_game_toko - Untuk melihat list game yang dijual pada toko",
                "\n7.  search_game_at_store - Untuk mencari game pada toko berdasarkan 5 parameter (ID, nama, harga, kategori, dan tahun rilis)",
                "\n8.  topup - Untuk menambahkan saldo kepada user",
                "\n9.  help - Untuk melihat fungsi-fungsi yang tersedia",
                "\n10. save - Untuk menyimpan data yang sudah dirubah ke dalam file"
                "\n11. exit - Untuk keluar dari aplikasi",
                "\n12. cipher - Untuk melakukan enkripsi dan dekripsi suatu password",
                "\n13. kerangajaib - Untuk berbicara dengan kerang ajaib",
                "\n14. tictactoe - Untuk bermain game tictactoe (XOXO)")
        else:
            print("============ HELP ============",
                "\n1.  login - Untuk melakukan login ke dalam sistem",
                "\n2.  list_game_toko - Untuk melihat list game yang dijual pada toko",
                "\n3.  buy_game - Untuk membeli game",
                "\n4.  list_game - Untuk melihat list game yang dimiliki user",
                "\n5.  search_my_game - Untuk mencari game yang dimiliki user berdasarkan 2 parameter (ID dan tahun rilis)",
                "\n6.  search_game_at_store - Untuk mencari game pada toko berdasarkan 5 parameter (ID, nama, harga, kategori, dan tahun rilis)",
                "\n7.  riwayat - Untuk melihat riwayat pembelian game user",
                "\n8.  help - Untuk melihat fungsi-fungsi yang tersedia",
                "\n9.  save - Untuk menyimpan data yang sudah dirubah ke dalam file"
                "\n10. exit - Untuk keluar dari aplikasi",
                "\n11. cipher - Untuk melakukan enkripsi dan dekripsi suatu password",
                "\n12. kerangajaib - Untuk berbicara dengan kerang ajaib",
                "\n13. tictactoe - Untuk bermain game tictactoe (XOXO)")
            # dst.
    # Belum login
    else:
        print("============ HELP ============",
            "\n1. login - Untuk melakukan login ke dalam sistem",
            "\n2. help - Untuk melihat fungsi-fungsi yang tersedia")