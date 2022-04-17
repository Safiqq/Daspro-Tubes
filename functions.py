# Fungsi primitif umum
# Mengembalikan panjang dari suatu <element> (bisa string/array)
def length(element):
    count = 0
    for i in element:
        count += 1
    return count

# Mengembalikan nilai paling besar dari <array (of integer)>
def maximum(array):
    # Asumsi length(array) > 0
    # Definisi value
    value = 0
    for i in range(length(array)):
        if i == 0:
            value = array[i]
        else:
            if value < array[i]:
                value = array[i]
    return value

# Mengembalikan nilai paling kecil dari <array (of integer)>
def minimum(array):
    # Asumsi length(array) > 0
    # Definisi value
    value = 0
    for i in range(length(array)):
        if i == 0:
            value = array[i]
        else:
            if value > array[i]:
                value = array[i]
    return value


# Fungsi primitif array
# Menambahkan suatu <element> (bisa string/array) di belakang <array>
def append(array, element):
    count_1 = length(array)
    new_array = ["" for i in range(count_1 + 1)]
    tipe = type(element)
    # try:
    if tipe == str:
        # element : string
        for i in range(count_1):
            new_array[i] = array[i]
        new_array[count_1] = element
        return new_array
    # except:
    elif tipe == list:
        # element : array
        count_2 = length(element)
        new_array[count_1] = ["" for i in range(count_2)]
        for i in range(count_1):
            new_array[i] = array[i]
        for j in range(count_2):
            new_array[count_1][j] = element[j]
        return new_array

# Menghapus suatu <element> pada <array> (jika ada). Jika terdapat lebih dari 1 <element> pada array,
# dapat menghapus lebih dari 1 (parameter <number> opsional)
def remove(array, element, number=1):
    tipe = type(array)
    if tipe == str:
        string = ""
        for i in range(length(array)):
            if array[i] != element:
                string += array[i]
            else:
                if number > 0:
                    number -= 1
                else:
                    string += array[i]
        return string
    elif tipe == list:
        new_array = []
        for i in range(length(array)):
            if array[i] != element:
                new_array = append(new_array, array[i])
            else:
                if number > 0:
                    number -= 1
                else:
                    new_array = append(new_array, array[i])
        return new_array

# Mengubah <string> menjadi <array (of string)>, dengan memisahkan <string> berdasarkan <element>
def split(string, element):
    new_array = []
    new_word = ""
    string += element
    for i in range(length(string)):
        if string[i] != element:
            new_word += string[i]
        else:
            new_array = append(new_array, new_word)
            new_word = ""
    return new_array

# Mengurutkan <array (of integer)> berdasarkan ascending dan descending
def sort(array, x="a"):
    # a : ascending
    # d : descending
    count = length(array)
    new_array = ["" for i in range(count)]
    if x == "a":
        for i in range(count):
            element = minimum(array)
            array = remove(array, element)
            new_array[i] = element
        return new_array
    elif x == "d":
        for i in range(count):
            element = maximum(array)
            array = remove(array, element)
            new_array[i] = element
        return new_array

# Mengubah <array (of string)> menjadi <string>, dengan menambahkan <element> di antara array[i]
def join(array, element):
    string = ""
    for i in range(length(array)):
        string += array[i]
        if (i + 1) != length(array):
            string += element
    return string

# Mencari apakah suatu <element> adalah array[i]
def find(array, element):
    for i in range(length(array)):
        if array[i] == element:
            return True
    return False

# Mengambil beberapa karakter/elemen dari suatu string/array
def slicing(array, a, b):
    tipe = type(array)
    if tipe == str:
        string = ""
        for i in range(length(array)):
            if a <= i < b:
                string += array[i]
        return string
    elif tipe == list:
        new_array = []
        for i in range(length(array)):
            if a <= i < b:
                new_array = append(new_array, array[i])
        return new_array


# Fungsi validasi dan convert angka
# Mengembalikan boolean True apabila role dari <user_data> merupakan admin
def validasi_akses(user_data):
    # id;username;nama;password;role;saldo
    return user_data[4] == "admin"

# Mengembalikan boolean True apabila username dari <user_data> ditemukan di <list_user>
def validasi_user(list_user, user_data):
    # id;username;nama;password;role;saldo
    for i in range(length(list_user)):
        if list_user[i][1] == user_data[1]:
            return True
    return False

def validasi_game_toko(list_game_toko, input_game):
    # id;nama;kategori;tahun_rilis;harga;stok
    for i in range(length(list_game_toko)):
        if list_game_toko[i][0] == input_game[0]:
            return True
    return False

def convert(x, to_type):
    if to_type == str:
        string = ""
        x = str(x)
        count_period = (length(x)-1) // 3
        count = length(x) % 3
        if count == 0:
            count = 3
        for i in range(length(x)):
            if count > 0:
                string += x[i]
                count -= 1
            else:
                count = 2
                if count_period > 0:
                    string += "." + x[i]
                    count_period -= 1
        return string
    elif to_type == int:
        x = remove(x, ".", 999)
        x = int(x)
        return x
