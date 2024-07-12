import random


def get_user_choice():
    user_input = input("請選擇: 石頭 (r), 剪刀 (s), 布 (p): ")
    while user_input not in ["r", "s", "p"]:
        user_input = input("無效的選擇。請選擇: 石頭 (r), 剪刀 (s), 布 (p): ")
    return user_input


def get_computer_choice():
    choices = ["r", "s", "p"]
    return random.choice(choices)


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "平手！"
    elif (
        (user_choice == "r" and computer_choice == "s")
        or (user_choice == "s" and computer_choice == "p")
        or (user_choice == "p" and computer_choice == "r")
    ):
        return "你贏了！"
    else:
        return "你輸了！"


def main():
    print("歡迎來到石頭、剪刀、布遊戲！")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    choices_dict = {"r": "石頭", "s": "剪刀", "p": "布"}
    print(f"你選擇了: {choices_dict[user_choice]}")
    print(f"電腦選擇了: {choices_dict[computer_choice]}")

    result = determine_winner(user_choice, computer_choice)
    print(result)


if __name__ == "__main__":
    main()
