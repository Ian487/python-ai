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
