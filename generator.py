import random
import string
import os
import shutil
from challenges.base64_challenge import generate_base64
from challenges.find_needle_challenge import generate_find_needle
from challenges.password_cracker_challenge import generate_password_cracker

def empty_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        return

    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path) or os.path.islink(item_path):
            os.unlink(item_path)
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)

def menu():
    empty_directory("system")

    print("Capture the flag generator:")
    print("[1] Base 64")
    print("[2] Find needle in a haystack")
    print("[3] Brute force password cracker")

    flag = "FLAG{" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=8)) + "}"

    choice = 0

    while(choice not in [1, 2, 3]):
        choice = int(input("Choose your challenge: "))
        
        if choice == 1:
            generate_base64(flag)
        elif choice == 2:
            generate_find_needle(flag)
        elif choice == 3:
            generate_password_cracker(flag)
        else:
            print("Invalid input")

if __name__ == "__main__":
    menu()
