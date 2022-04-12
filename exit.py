import sys
from save import *

def exitt():
    confirm = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (Y/n) ")
    while confirm.lower() != "y" or confirm.lower() != "n":
        confirm = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (Y/n) ")
    if confirm.lower() == "y":
        save()
    sys.exit(0)