import streamlit as st

number = st.number_input("請輸入一個數字", step=1)
st.markdown(f"你輸入的數字是: {number}")
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
st.title("按鈕元件練習")
st.button("點我", key="button1")
if st.button("點我", key="button2"):
    st.balloons()
