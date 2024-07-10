import streamlit as st
import os

floderpath = (
    "markdown"  # 這是相對路徑, C:\Users\demon_bpsaktu\OneDrive\桌面\python-ai\markdown
)
files = os.listdir(floderpath)  # 取得資料夾中所有的檔案
print(files)  # 印出所有的檔案
files_name = []  # 建立一個空的list準備存需要的檔案
for f in files:
    if f.endswith(".md"):  # 如果檔案是以md結尾.
        files_name.append(f)  # 將檔案加到files_name中
print(files_name)  # 印出所有的markdown檔案
for f in files_name:  # 逐一讀取files_name中的檔案
    with open(f"{floderpath}/{f}", "r", encoding="utf-8") as file:  # 開啟檔案
        content = file.read()  # 讀取檔案內容
    with st.expander(f"{f[:-3]}"):  # 建立一個擴展元件, 標題是檔案名稱
        st.markdown(content)  # 把檔案內容顯示在擴展元件中
