### Python 程式技巧筆記

#### 1. `while` 迴圈

```python
i = 0
while i < 5:  # 條件式迴圈, 當i < 5時執行迴圈
    print(i)
    i = i + 1  # i = i + 1
```

- 使用 `while` 迴圈根據條件執行迴圈。

#### 2. 複合賦值運算符

```python
a = 10
a += 1  # 等同於 a = a + 1
print(a)

a -= 1  # 等同於 a = a - 1
print(a)

a *= 2  # 等同於 a = a * 2
print(a)

a /= 2  # 等同於 a = a / 2
print(a)

a //= 2  # 等同於 a = a // 2
print(a)

a %= 3  # 等同於 a = a % 3
print(a)

a **= 2  # 等同於 a = a ** 2
print(a)
```

- 使用複合賦值運算符進行簡潔的數值操作。

#### 3. 運算符優先順序

```python
# 根據以上符號列出優先順序
# 1. ()
# 2. **
# 3. * / // %
# 4. + -
# 5. == != > < >= <=
# 6. not, and, or
# 7. = += -= *= /= //= %= **=
```

- 列出運算符的優先順序。

#### 4. `break` 跳出迴圈

```python
i = 1
while i < 6:  # 條件式迴圈, 當i < 6時執行迴圈
    print(i)  # 印出i
    if i == 3:
        break  # 當 i 等於 3 時跳出迴圈
    i += 1

for i in range(1, 6):  # for 迴圈, 當i < 6時執行迴圈
    print(i)  # 印出i
    if i == 3:
        break  # 當 i 等於 3 時跳出迴圈
```

- 使用 `break` 跳出迴圈。

#### 5. `random` 模組

```python
import random  # 匯入random模組

print(random.randrange(10))  # 隨機產生0到9的變數
print(random.randrange(1, 10))  # 隨機產生1到9的變數
print(random.randrange(1, 10, 2))  # 隨機產生1到9的奇數

print(random.randint(1, 10))  # 隨機產生1到10的整數
```

- 使用 `random` 模組生成隨機數。

#### 6. 猜數字遊戲範例

```python
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
```

- 實現一個簡單的猜數字遊戲。

#### 7. 字典操作

```python
d = {"星期一": "蘋果", "星期二": "香蕉"}
print(d["星期一"])  # 蘋果
```

- 讀取字典中的值。

#### 8. 字典遍歷

```python
d = {"星期一": "蘋果", "星期二": "香蕉"}

for key in d:  # 預設只會獲得key
    print(key, d[key])

for key in d.keys():  # 使用 keys() 取得所有的key
    print(key)

for value in d.values():  # 取得所有的value
    print(value)

for key, value in d.items():  # 取得所有的key和value
    print(f"key = {key}, value = {value}")

for item in d.items():  # 取得所有的key和value
    print(f"key = {item[0]}, value = {item[1]}")
```

- 遍歷字典的不同方法。

#### 9. 字典新增與修改

```python
d = {"星期一": "蘋果", "星期二": "香蕉"}
d["星期一"] = "橘子"  # 修改值
d["星期三"] = "蘋果"  # 新增元素
print(d)
```

- 新增或修改字典中的元素。

#### 10. 檢查字典中是否存在特定的鍵或值

```python
d = {"星期一": "蘋果", "星期二": "香蕉"}
print("星期一" in d)  # True
print("星期三" in d)  # False
print("蘋果" in d.values())  # True
print("香蕉" in d.values())  # True

L = ["星期一", "星期二"]
print("星期一" in L)  # True
print("星期三" in L)  # False
```

- 檢查鍵或值是否在字典或列表中。

#### 11. 刪除字典中的元素

```python
d = {"星期一": "蘋果", "星期二": "香蕉"}
d.pop("星期一")  # 刪除 key = "星期一" 的元素
print(d)

d.pop("星期三", "找不到")  # 如果刪除的元素可能不存在
print(d)
```

- 使用 `pop` 方法刪除字典中的元素。

---

### Streamlit 程式技巧筆記

#### 1. 顯示圖片

```python
import streamlit as st
import os

st.title("圖片元件")
image_folder = "image"  # 資料夾名稱
image_files = os.listdir(image_folder)  # 取得資料夾內的所有檔案
st.write(image_files)  # 顯示所有檔案

image_size = st.number_input("圖片大小", min_value=50, max_value=500, step=50, value=100)
# 使用者輸入圖片大小, 最小50, 最大500, 預設100, 每次增加50

for image_file in image_files:
    st.image(f"{image_folder}/{image_file}", width=image_size)
    # 根據使用者輸入的大小顯示圖片

for image_file in image_files:  # 顯示所有圖片
    st.image(f"{image_folder}/{image_file}", use_column_width=True)
    # 使用欄寬度顯示圖片
```

- 使用 Streamlit 顯示圖片並調整大小。
