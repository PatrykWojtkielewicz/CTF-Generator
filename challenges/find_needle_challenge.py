import os
import shutil
import random
import string
from challenges.common import get_user_answer

def generate_find_needle(correct_flag):
    base_dir = "system"
    all_paths = []

    if os.path.exists(base_dir):
        shutil.rmtree(base_dir)
    os.makedirs(base_dir)

    for i in range(10):
        level1 = os.path.join(base_dir, f"dir_{i}")
        os.makedirs(level1)
        for j in range(10):
            level2 = os.path.join(level1, f"dir_{j}")
            os.makedirs(level2)
            for k in range(10):
                level3 = os.path.join(level2, f"dir_{k}")
                os.makedirs(level3)
                for l in range(10):
                    filename = f"file_{l}.txt"
                    path = os.path.join(level3, filename)
                    all_paths.append(path)

    target = random.choice(all_paths)

    for path in all_paths:
        with open(path, 'w') as f:
            if path == target:
                f.write(correct_flag)
            else:
                junk = ''.join(random.choices(string.ascii_letters + string.digits, k=50))
                f.write(junk)

    get_user_answer(correct_flag)
