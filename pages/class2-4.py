import streamlit as st

st.title("數字金字塔")
number = st.number_input("請輸入一個整數(1-9)", step=1, min_value=1, max_value=9)
st.markdown("數字金字塔:")
for i in range(1, number + 1):
    st.markdown(str(i) * i)

st.title("箭頭金字塔")
number = st.number_input("請輸入箭頭大小", step=1, min_value=1)
# st.markdown("箭頭金字塔:")
# number = int(input("請輸入箭頭大小"))
arrow = ""
for i in range(1, number * 2, 2):
    # print(" " * ((number * 2 - i) // 2) + "*" * i)
    arrow += " " * ((number * 2 - i) // 2) + "*" * i + "\n"
for i in range(number):
    # print(" " * (number - 1) + "*")
    arrow += " " * (number - 1) + "*" + "\n"
# print(arrow)
st.markdown(
    f"""
    ```\n箭頭金字塔:\n{arrow}\n```
"""
)
