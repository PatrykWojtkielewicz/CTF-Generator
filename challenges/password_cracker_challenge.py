import os
import random
import string
import base64
from challenges.common import get_user_answer

def generate_password_cracker(correct_flag):
    password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
    encoded_pw = base64.b64encode(password.encode()).decode()

    os.makedirs("system", exist_ok=True)
    with open("system/secret.txt", "w") as f:
        f.write(password)

    with open("system/readme.txt", "w") as f:
        f.write("Can you guess the 4-character lowercase+digit password?\n")
        f.write("Try to brute-force it by checking against the password checker script.\n")
        f.write("Call check_password.py with a guess!")

    with open("system/password_checker.py", "w") as f:
        f.write(f"""import sys
import base64

def check_password(pw):
    encoded = "{encoded_pw}"
    actual = base64.b64decode(encoded.encode()).decode()
    return pw == actual

if __name__ == "__main__":
    guess = sys.argv[1] if len(sys.argv) > 1 else ""
    if check_password(guess):
        print("Correct! The flag is: {correct_flag}")
    else:
        print("Incorrect password.")
""")

    print("Brute-force password challenge created. Check the system folder.")
    print("Try to write a script that cracks the password by calling password_checker.py")

    get_user_answer(correct_flag)
