import base64
from challenges.common import get_user_answer

def generate_base64(correct_flag):
    encoded = base64.b64encode(correct_flag.encode()).decode()

    with open("system/readme.txt", "w") as f:
        f.write(f"Decode this:\n\n{encoded}")

    get_user_answer(correct_flag)
