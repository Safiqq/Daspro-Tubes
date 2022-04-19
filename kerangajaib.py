import time
from functions import *

def random(x):
    x *= time.time() * 1000
    x %= 10
    return int(x)

def kerangajaib(user_data):
    if user_data != []:
        pertanyaan = input("Apa pertanyaanmu? ")
        number = random(length(pertanyaan))
        if number == 0:
            print("Ya.")
        elif number == 1:
            print("Tidak.")
        elif number == 2:
            print("Bisa jadi.")
        elif number == 3:
            print("Mungkin.")
        elif number == 4:
            print("Tentunya.")
        elif number == 5:
            print("Tidak mungkin.")
        elif number == 6:
            print("Tidak tahu.")
        elif number == 7:
            print("Nanti saja.")
        elif number == 8:
            print("Jangan.")
        # number = 9
        else:
            print("Hmm.")
    else:
        print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login".')