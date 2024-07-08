# 註解筆記
# 代表註解的行
"""
這是多行註解
"""
# print("hello") # ctrl+?可以單行註解
print(123)  # 整數
print(123.456)  # 浮點數
print(True)  # 布林值
print(False)  # 布林值
print("hello")  # 字串
print('"')  # 印出雙引號
print("'")  # 印出單引號
a = 10
print(a)
b = "hello"
print(b)
print(1 + 1)  # 加法計算
print(2 - 1)  # 減法計算
print(2 * 3)  # 乘法計算
print(10 / 3)  # 除法計算
print(10 // 3)  # 整數除法計算
print(10 % 3)  # 取餘數計算
print(2**3)  #  次方計算就是2乘2乘2
# 根據以上符號列出優先順序
# 1. ()
# 2. **
# 3. * / // %
# 4. + -
# 字串運算
a = "hello"
b = "world"
print(a + b)  # 字串相加
print(a + " " + b)  # 字串相加
print(a * 3)  # 字串乘法
# 加法乘法混合
print(a + " " + b * 3)  # 字串相加
print(f"hello{10}{True}")
# 在字串前加f, 可以在字串中加入變數
print(len("hello"))  # 字串長度
print(int("123"))  # 字串轉整數
print(float("123.456"))  # 字串轉浮點數
print(str(123))  # 整數轉字串
print(bool(1))  # 整數轉布林值
print("input()可以在終端機輸入文字")
a = input("在這邊可以開始輸入文字")  # input()可以在終端機輸入文字
print(f"你輸入的內容是: {a}")  # 印出輸入的文字
print(f"input()輸入的內容型態是: {type(a)}")  # 輸入的內容型態是字串
# 計算正方形面積
a = input("請輸入正方形的邊長:")
area = int(a) * int(a)
print(f"正方形的面積是: {area}")
