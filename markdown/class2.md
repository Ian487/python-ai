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
