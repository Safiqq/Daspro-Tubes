import time

def lcg(x):
    a = time.perf_counter_ns()
    time.sleep(0.2)
    c = time.perf_counter_ns()
    time.sleep(0.2)
    m = time.perf_counter_ns()
    x = (a * x + c) % m
    r = (x * 10) // m
    return r

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