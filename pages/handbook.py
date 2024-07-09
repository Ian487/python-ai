import streamlit as st

with st.expander("class1 程式筆記"):
    st.markdown(
        """
# 程式技巧筆記

## 註解

- **單行註解**: 使用 `#` 開頭標註。

    ```python
    # 這是一行註解
    ```

- **多行註解**: 使用三個引號 `'''` 或 `'''` 包裹多行文字。

  ```python
  '''
  這是一個多行註解的例子。
  可以包含多行文字。
  '''
  ```

- **單行註解快捷鍵**: 在大多數編輯器中，`Ctrl + /` 可以快速註解或取消註解選中的行。

  ```python
  # print("hello")  # 使用 Ctrl + / 可以註解掉這行
  ```

## 輸出和資料類型

- **使用 `print()` 輸出各類資料**:

  ```python
  print(123)  # 整數
  print(123.456)  # 浮點數
  print(True)  # 布林值
  print("hello")  # 字串
  ```

- **使用 `print()` 輸出特殊字元**:

  ```python
  print('"')  # 雙引號
  print("'")  # 單引號
  ```

- **變數的使用**:

  ```python
  a = 10
  print(a)  # 輸出變數 a 的值

  b = "hello"
  print(b)  # 輸出變數 b 的值
  ```

## 數學運算

- **基本運算**:

  ```python
  print(1 + 1)  # 加法
  print(2 - 1)  # 減法
  print(2 * 3)  # 乘法
  print(10 / 3)  # 除法
  print(10 // 3)  # 整數除法
  print(10 % 3)  # 取餘數
  print(2**3)  # 次方計算
  ```

- **運算優先順序**:
  1. 括號 `()`
  2. 次方 `**`
  3. 乘法 `*`、除法 `/`、整數除法 `//`、取餘數 `%`
  4. 加法 `+`、減法 `-`

## 字串操作

- **字串相加**:

  ```python
  a = "hello"
  b = "world"
  print(a + b)  # "helloworld"
  print(a + " " + b)  # "hello world"
  ```

- **字串乘法**:

  ```python
  print(a * 3)  # "hellohellohello"
  ```

- **混合操作**:

  ```python
  print(a + " " + b * 3)  # "hello worldworldworld"
  ```

- **格式化字串**:

  ```python
  print(f"hello{10}{True}")  # "hello10True"
  ```

- **字串長度**:

  ```python
  print(len("hello"))  # 5
  ```

## 資料型別轉換

- **字串轉整數**:

  ```python
  print(int("123"))  # 123
  ```

- **字串轉浮點數**:

  ```python
  print(float("123.456"))  # 123.456
  ```

- **數值轉字串**:

  ```python
  print(str(123))  # "123"
  ```

- **數值轉布林值**:

  ```python
  print(bool(1))  # True
  ```

## 使用 `input()` 獲取使用者輸入

- **基本使用**:

  ```python
  print("input()可以在終端機輸入文字")
  a = input("在這邊可以開始輸入文字")  # 提示使用者輸入
  print(f"你輸入的內容是: {a}")  # 輸出使用者輸入的內容
  ```

- **輸入的內容型態**:

  ```python
  print(f"input()輸入的內容型態是: {type(a)}")  # 顯示內容型態，預設為字串
  ```

## 範例：計算正方形面積

- **計算範例**:

  ```python
  a = input("請輸入正方形的邊長:")
  area = int(a) * int(a)  # 記得將輸入轉換為整數
  print(f"正方形的面積是: {area}")
  ```

---

以上是一些 Python 程式設計的基礎技巧，這些技巧對於理解和撰寫程式碼非常重要。

    """
    )
with st.expander("class2 程式筆記"):
    st.markdown(
        """
## 程式技巧筆記

### 比較運算符

- **相等運算符** (`==`):

  ```python
  print(1 == 1)  # 比較是否相等，結果為 True
  ```

- **不相等運算符** (`!=`):

  ```python
  print(1 != 1)  # 比較是否不相等，結果為 False
  ```

- **大於運算符** (`>`):

  ```python
  print(1 > 1)  # 比較是否大於，結果為 False
  ```

- **小於運算符** (`<`):

  ```python
  print(1 < 1)  # 比較是否小於，結果為 False
  ```

- **大於等於運算符** (`>=`):

  ```python
  print(1 >= 1)  # 比較是否大於等於，結果為 True
  ```

- **小於等於運算符** (`<=`):

  ```python
  print(1 <= 1)  # 比較是否小於等於，結果為 True
  ```

### 邏輯運算符

- **否定運算符** (`not`):

  ```python
  print(not True)  # 否定 True，結果為 False
  print(not False)  # 否定 False，結果為 True
  ```

- **與運算符** (`and`):

  ```python
  print(True and True)  # 兩個條件都為 True，結果為 True
  print(True and False)  # 其中一個條件為 False，結果為 False
  ```

- **或運算符** (`or`):

  ```python
  print(True or True)  # 其中一個條件為 True，結果為 True
  print(True or False)  # 其中一個條件為 True，結果為 True
  ```

### 運算優先順序

1. 括號 `()`
2. 次方 `**`
3. 乘法 `*`、除法 `/`、整數除法 `//`、取餘數 `%`
4. 加法 `+`、減法 `-`
5. 比較運算符 `== != > < >= <=`
6. 邏輯運算符 `not and or`

### 條件判斷

- **使用 `if` 進行條件判斷**:

  ```python
  pwd = input("請輸入密碼：")
  if pwd == "123":
      print("密碼正確")
  elif pwd == "456":
      print("密碼正確")
  else:
      print("密碼錯誤")
  ```

  - `if`: 必須有且只能有一個。
  - `elif`: 可以有多個，也可以沒有。
  - `else`: 可以有一個，也可以沒有。

### 使用 Streamlit

- **輸入和顯示數值**:

  ```python
  import streamlit as st
  number = st.number_input("請輸入一個數字", step=1)
  st.markdown(f"你輸入的數字是: {number}")
  ```

- **條件判斷與顯示等級**:

  ```python
  grade = st.number_input("輸入你的分數")
  if grade >= 90 and grade <= 100:
      st.markdown("你的等級是: A")
  elif grade >= 80 and grade <= 89:
      st.markdown("你的等級是: B")
  elif grade >= 70 and grade <= 79:
      st.markdown("你的等級是: C")
  elif grade >= 60 and grade <= 69:
      st.markdown("你的等級是: D")
  else:
      st.markdown("你的等級是: E")
  ```

- **按鈕與氣球效果**:

  ```python
  st.title("按鈕元件練習")
  st.button("點我", key="button1")
  if st.button("點我", key="button2"):
      st.balloons()
  ```

### 迴圈

- **使用 `for` 迴圈遍歷範圍**:

  ```python
  for i in range(10):  # 0 到 9
      print(i)
  for i in range(2, 100):  # 2 到 99
      print(i)
  for i in range(2, 100, 2):  # 2 到 99 的偶數
      print(i)
  for i in range(100, 3, -2):  # 100 到 4 的偶數
      print(i)
  ```

### 建立金字塔

- **數字金字塔**:

  ```python
  st.title("數字金字塔")
  number = st.number_input("請輸入一個整數(1-9)", step=1, min_value=1, max_value=9)
  st.markdown("數字金字塔:")
  for i in range(1, number + 1):
      st.markdown(str(i) * i)
  ```

- **箭頭金字塔**:

  ```python
  st.title("箭頭金字塔")
  number = st.number_input("請輸入箭頭大小", step=1, min_value=1)
  arrow = ""
  for i in range(1, number * 2, 2):
      arrow += " " * ((number * 2 - i) // 2) + "*" * i + "\n"
  for i in range(number):
      arrow += " " * (number - 1) + "*" + "\n"
  st.markdown(
      f'''
      ```
      箭頭金字塔:
      {arrow}
      ```
      '''
  )
  ```

### 列表操作

- **建立和操作列表**:

  ```python
  print([])  # 空列表
  print([1, 2, 3])  # 有三個元素的列表
  print([1, 2, 3, "a", "b", "c"])  # 混合型列表
  print([1, 2, 3, ["a", "b", "c"]])  # 嵌套列表
  ```

- **列表索引**:

  ```python
  L = ["moO", "MOo", "moo", "mOO", "MoO", "moO"]
  print(L[0])  # 第一個元素
  print(L[1])  # 第二個元素
  print(L[2])  # 第三個元素
  ```

- **遍歷列表**:

  ```python
  for index in range(len(L)):
      print(L[index])  # 使用索引遍歷
  for cow in L:
      print(cow)  # 直接遍歷元素
  ```

    """
    )
