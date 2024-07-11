import random

number_to_guess = random.randint(1, 100)  # 隨機產生1到100的數字
guess = 0  # 假設猜測的數字為0

print("歡迎來到猜數字遊戲！")  # 顯示提示訊息
print("我已經選好了1到100之間的一個數字，來猜猜看是什麼吧！")  # 顯示提示訊息

while guess != number_to_guess:  # 在猜測的數字與隨機產生的數字不相等時執行迴圈
    guess = int(input("請輸入你的猜測："))  # 讀取用戶輸入的猜測
    if guess < 1 or guess > 100:  # 如果猜測的數字小於1或大於100
        print("請勿輸入非法數字！")  # 顯示提示訊息
    elif guess < number_to_guess:  # 如果猜測的數字小於隨機產生的數字
        print("太小了，再試一次！")  # 顯示提示訊息
    elif guess > number_to_guess:  # 如果猜測的數字大於隨機產生的數字
        print("太大了，再試一次！")  # 顯示提示訊息
    else:
        print("恭喜你，猜對了！")  # 顯示提示訊息
