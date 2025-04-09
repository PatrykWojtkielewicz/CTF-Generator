def get_user_answer(correct_flag):
    print('Your challenge has just been created. Look for it in the "system" directory')
    print("Once you complete this challenge, paste your answer here: ")

    while True:
        user_flag = input("Enter your flag: ").strip()
        if user_flag == correct_flag:
            print("Congratulations! Your answer is correct!")
            break
        else:
            print("Incorrect answer, please try again")
