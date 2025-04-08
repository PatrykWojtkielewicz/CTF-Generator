import base64
import random
import string

def generate_base64_challenge():
    flag = "FLAG{" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=8)) + "}"
    encoded = base64.b64encode(flag.encode()).decode()

    with open("challenges/base64_challenge.txt", "w") as f:
        f.write(f"Decode this:\n\n{encoded}")

    with open("flags/flags.txt", "a") as f:
        f.write(f"base64_challenge: {flag}\n")

    print("Base64 challenge created.")


def menu():
    print("Capture the flag generator:")
    print("[1] Base 64")

    choice = input("Choose your challenge: ")

    if choice == "1":
        generate_base64_challenge()
    else:
        print("Invalid input")

if __name__ == "__main__":
    generate_base64_challenge()
