import base64
import random
import string
import os
import shutil

def generateBase64(correctFlag):
    encoded = base64.b64encode(correctFlag.encode()).decode()

    with open("system/readme.txt", "w") as f:
        f.write(f"Decode this:\n\n{encoded}")

    getUserAnswer(correctFlag)

def generateFindNeedle(correctFlag):
    baseDir = "system"
    allFilePaths = []

    if os.path.exists(baseDir):
        shutil.rmtree(baseDir)
    os.makedirs(baseDir)

    for i in range(10):
        level1 = os.path.join(baseDir, f"dir_{i}")
        os.makedirs(level1)
        for j in range(10):
            level2 = os.path.join(level1, f"dir_{j}")
            os.makedirs(level2)
            for k in range(10):
                level3 = os.path.join(level2, f"dir_{k}")
                os.makedirs(level3)
                for l in range(10):
                    filename = f"file_{l}.txt"
                    filepath = os.path.join(level3, filename)
                    allFilePaths.append(filepath)

    target_file = random.choice(allFilePaths)

    for path in allFilePaths:
        with open(path, 'w') as f:
            if path == target_file:
                f.write(correctFlag)
            else:
                junk = ''.join(random.choices(string.ascii_letters + string.digits, k=50))
                f.write(junk)

    getUserAnswer(correctFlag)

def getUserAnswer(correctFlag):
    print("Your challenge has just been created. Look for it in the \"system\" directory")
    print("Once you complete this challenge, paste your answer here: ")

    while True:
        userFlag = input("Enter your flag: ").strip()
        if userFlag == correctFlag:
            print("Congratulations! Your answer is correct!")
            break
        else:
            print("Incorrect answer, please try again")

def emptyDirectory(path):
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
    emptyDirectory("system")

    print("Capture the flag generator:")
    print("[1] Base 64")
    print("[2] Find needle in a haystack")

    flag = "FLAG{" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=8)) + "}"

    choice = int(input("Choose your challenge: "))

    if choice == 1:
        generateBase64(flag)
    elif choice == 2:
        generateFindNeedle(flag)
    else:
        print("Invalid input")

if __name__ == "__main__":
    menu()
