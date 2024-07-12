import streamlit as st
import time
import os

# 設計products字典, 每個商品有價格(price), 庫存(stock), 圖片(image)三個屬性
# image可以讀取存放在image資料夾內的圖片
# 讀取圖片清單

image_folder = "image"
image_files = os.listdir(image_folder)

if "products" not in st.session_state:
    st.session_state.products = {}

for image_file in image_files:
    product_name = image_file[:-4]
    if product_name not in st.session_state.products:
        st.session_state.products[product_name] = {
            "price": 10,
            "stock": 10,
            "image": f"{image_folder}/{image_file}",
        }
# products 範例
# products = ("蘋果": {"price": 10, "stock": 10, "image": "image/apple.jpg"},
#             "香蕉": {"price": 20, "stock": 5, "image": "image/banana.jpg"},
#             "橘子": {"price": 15, "stock": 3, "image": "image/orange.jpg"},
#             "葡萄": {"price": 25, "stock": 8, "image": "image/grape.jpg"},
#             "芒果": {"price": 30, "stock": 2, "image": "image/mango.jpg"},
# )

# 顯示商品
st.title("購物平台")  # 標題
col_num = st.number_input("欄數", min_value=1, step=1, value=2)
cols = st.columns(col_num)
i = 0
for product_name, details in st.session_state.products.items():
    with cols[i % col_num]:  # 透過讀取榆樹來決定商品顯示在哪一欄
        st.image(details["image"], use_column_width=True)
        st.markdown(f"### {product_name}")
        st.markdown(f"價格: ${details['price']}")
        st.markdown(f"庫存: {details['stock']}")

    if st.button(f"購買 {product_name}", key=f"{product_name}"):
        if details["stock"] > 0:
            st.session_state.products[product_name]["stock"] -= 1
            st.success(f"購買 {product_name} 成功!")
            time.sleep(1)
            st.rerun()
        else:
            st.error(f"庫存不足!")

    i += 1
# 新增商品庫存區塊
st.title("新增商品庫存")
product_names = list(st.session_state.products.keys())
col1, col2 = st.columns(2)
with col1:
    selected_product = st.selectbox("選擇商品", product_names)
with col2:
    new_stock = st.number_input("新增庫存數量", min_value=1, step=1)

if st.button("新增庫存"):
    st.session_state.products[product_name]["stock"] += new_stock
    st.success(f"{selected_product} 的庫存已新增 {new_stock} 個件。")
    time.sleep(1)
    st.rerun()

# 重新顯示商品已反應更新後的庫存
st.markdown("目前商品庫存:")
for product_name, details in st.session_state.products.items():
    st.markdown(f"{product_name}: {details['stock']} 件")
