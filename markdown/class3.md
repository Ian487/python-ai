### Python List 操作筆記

#### 1. 創建列表並追加元素

```python
l = [1, 2, 3]
l.append(4)
print(l)
```

- 使用 `append` 方法在列表末尾添加元素。

#### 2. 移除列表中的特定元素

```python
l = ["a", "b", "c", "a"]
l.remove("a")
print(l)
```

- 使用 `remove` 方法移除列表中第一次出現的指定元素。

#### 3. 計算列表中元素的出現次數

```python
l = [9, 1, -4, 3, 7, 11, 3]
print(l.count(3))
```

- 使用 `count` 方法計算特定元素在列表中的出現次數。

#### 4. 列表的其他操作

```python
l = [3, 12, 7, 9, 5, 3, 3, 3, 2, 4]
l.append(8)
print(l)

c = l.count(3)
for i in range(c):
    l.remove(3)

print(l)

l.pop(0)
print(l)
```

- `append` 用於在列表末尾添加元素。
- `count` 用於計算特定元素的出現次數。
- `remove` 用於移除列表中第一次出現的特定元素。
- `pop` 用於根據索引移除列表中的元素。

#### 5. 列表排序

```python
l.sort()
print(l)

l.sort(reverse=True)
print(l)
```

- 使用 `sort` 方法對列表進行排序。
  - 默認從小到大排序。
  - 設置 `reverse=True` 從大到小排序。

#### 6. 查找元素的索引

```python
l = [3, 1, 2, 4, 5]
print(l.index(5))
```

- 使用 `index` 方法查找特定元素在列表中的索引。

---

### Streamlit 筆記

#### 1. 標題和欄位佈局

```python
import streamlit as st

st.title("欄位元件")
col1, col2 = st.columns(2)
col1.button("按鈕1")
col2.button("按鈕2")
```

- 使用 `st.title` 方法設置標題。
- 使用 `st.columns` 方法創建多欄佈局。
- 在指定欄中添加按鈕。

#### 2. 使用 `with` 語句添加欄位內的元素

```python
with col1:
    st.markdown("這是欄一")
    st.button("左邊按鈕")

with col2:
    st.markdown("這是欄二")
    st.button("右邊按鈕")
```

- 使用 `with` 語句在特定欄位內添加元件。

#### 3. 設定欄位的比例

```python
cols = st.columns([1, 5, 1])
cols[0].button("按鈕1", key="button1")
cols[1].button("按鈕2", key="button2")
cols[2].button("按鈕3", key="button3")
```

- 通過傳遞列表設置欄位比例。

#### 4. 文字輸入元件

```python
st.title("文字輸入元件")
text = st.text_input("請輸入文字")
st.markdown(f"您輸入的文字是：{text}")
```

- 使用 `st.text_input` 創建文字輸入框。

#### 5. 使用 session state

```python
st.title("session_state")
ans = 1
st.write(f"#####{ans}")

if st.button("按鈕", key="btn"):
    ans += 1

st.write(f"#####{ans}")

if "ans" not in st.session_state:
    st.session_state.ans = 1

if st.button("session_state按鈕", key="session_state_btn"):
    st.session_state.ans += 1

st.markdown(f"#####{st.session_state.ans}")
```

- 使用 `st.session_state` 保持跨頁面狀態。

#### 6. 點餐機範例

```python
st.title("點餐機")

if "order" not in st.session_state:
    st.session_state.order = []

col1, col2 = st.columns(2)

with col1:
    foodInput = st.text_input("請輸入餐點")

with col2:
    if st.button("加入", key="add"):
        st.session_state.order.append(foodInput)

st.write(f"### 購物籃")
for i in range(len(st.session_state.order)):
    col1, col2 = st.columns(2)
    with col1:
        st.write(st.session_state.order[i])
    with col2:
        if st.button("刪除", key=f"remove_{i}"):
            st.session_state.order.pop(i)
            st.rerun()
```

- 用於創建簡單的點餐應用，展示如何使用 `st.session_state` 儲存和管理狀態。
