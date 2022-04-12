from function import *

def inv(a, m):
    y = 1
    while (a * y) % m != 1:
        y += 1
    return y

def cipher(password, todo):
    # Affine cipher
    # http://rumkin.com/tools/cipher/affine.php
    # e(x) = (ax + b) mod m
    # d(x) = (x^(-1) * (x - b) mod m
    a = 9
    b = 9
    m = 26
    if todo == "encrypt":
        encrypted = ""
        for i in password:
            i = ord(i)
            # Cek a-z
            if 97 <= i <= 122:
                e = (a * (i - 97) + b) % m
                e += 97
                encrypted += chr(e)
            # Cek A-Z
            elif 65 <= i <= 90:
                e = (a * (i - 65) + b) % m
                e += 65
                encrypted += chr(e)
            else:
                encrypted += chr(i)
        return encrypted
    elif todo == "decrypt":
        decrypted = ""
        for i in password:
            i = ord(i)
            a_inv = inv(a, m)
            # Cek a-z
            if 97 <= i <= 122:
                d = (a_inv * ((i - 97) - b)) % m
                d += 97
                decrypted += chr(d)
            # Cek A-Z
            elif 65 <= i <= 90:
                d = (a_inv * ((i - 65) - b)) % m
                d += 65
                decrypted += chr(d)
            else:
                decrypted += chr(i)
        return decrypted