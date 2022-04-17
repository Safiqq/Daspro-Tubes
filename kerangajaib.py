import time

def lcg(x):
    x *= time.perf_counter_ns()
    a = 11
    c = 7
    m = 10
    x = (a * x + c) % m

    print(x)
lcg(1)

def kerangajaib():
    input("Apa pertanyaanmu? ")
    number = lcg(100)
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