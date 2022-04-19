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
    return array + [element]

def konkat(array1, array2):
    return array1 + array2

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
def sort(array, order="a"):
    # a : ascending
    # d : descending
    count = length(array)
    new_array = ["" for i in range(count)]
    if order == "a" or order == "+":
        for i in range(count):
            element = minimum(array)
            array = remove(array, element)
            new_array[i] = element
        return new_array
    elif order == "d" or order == "-":
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


# Fungsi validasi, convert angka, cari space maksimum
# Mengembalikan boolean True apabila role dari <user_data> merupakan admin
def validasi_akses(user_data):
    # id;username;nama;password;role;saldo
    return user_data[4] == "admin"

# Mengembalikan boolean True apabila username ditemukan di <list_user>
def validasi_user(list_user, username):
    # id;username;nama;password;role;saldo
    for i in range(length(list_user)):
        if list_user[i][1] == username:
            return True
    return False
# print(validasi_user([["id", "username"]], "usernam1e"))

def validasi_game_toko(list_game_toko, id_game):
    # id;nama;kategori;tahun_rilis;harga;stok
    for i in range(length(list_game_toko)):
        if list_game_toko[i][0] == id_game:
            return True
    return False

def validasi_game_dipunya(list_game, id_game, user_data):
    # game_id;user_id
    # id;username;nama;password;role;saldo
    for i in range(length(list_game)):
        if list_game[i][0] == id_game and list_game[i][1] == user_data[0]:
            return True
    return False

def get_game_index(list_game_toko, id_game):
    # id;nama;kategori;tahun_rilis;harga;stok
    for i in range(length(list_game_toko)):
        if list_game_toko[i][0] == id_game:
            return i

def get_id_game_owned(list_game_dipunya, user_data):
    array = []
    # game_id;user_id
    # id;username;nama;password;role;saldo
    for i in range(length(list_game_dipunya)):
        if list_game_dipunya[i][1] == user_data[0]:
            array = append(array, list_game_dipunya[i][0])
    return array

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

def space_max(list_game, index):
    count = 0
    for i in range(length(list_game)):
        if length(list_game[i][index]) > count:
            count = length(list_game[i][index])
    return count
