import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dịch vụ thuê xe", page_icon="🚗", layout="wide")

# ===== LOGO =====
col1, col2 = st.columns([1,4])

with col1:
    st.image("logo.png", width=400)

with col2:
    st.title("Chauffeur & Limousine")
    st.write("Đưa đón sân bay • Công tác • Du lịch • Sự kiện")

st.divider()

menu = st.radio(
    "Menu",
    ["Trang chủ","Bảng giá","Đặt xe","Liên hệ"],
    horizontal=True
)

# ===============================
# TRANG CHỦ - GALLERY XE
# ===============================

import streamlit as st

st.set_page_config(page_title="Dịch vụ thuê xe", layout="wide")

menu = st.sidebar.selectbox(
    "Menu",
    ["Trang chủ","Báo giá","Đặt xe","Liên hệ"]
)

if menu == "Trang chủ":

    st.title("Dịch vụ cho thuê xe du lịch")

    cars = {
        "Toyota Innova":[
            "https://upload.wikimedia.org/wikipedia/commons/3/3e/Toyota_Innova.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/0/05/Toyota_Innova_interior.jpg"
        ],

        "Toyota Fortuner":[
            "https://upload.wikimedia.org/wikipedia/commons/7/7b/Toyota_Fortuner.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/e/e5/Toyota_Fortuner_interior.jpg"
        ],

        "Toyota Camry":[
            "https://upload.wikimedia.org/wikipedia/commons/3/3a/Toyota_Camry_2018.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/1/12/Toyota_Camry_interior.jpg"
        ],

        "Kia Carnival":[
            "https://upload.wikimedia.org/wikipedia/commons/5/5a/Kia_Carnival.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/b/b8/Kia_Carnival_interior.jpg"
        ]
    }

    cols = st.columns(4)

    for i,(car,images) in enumerate(cars.items()):

        with cols[i]:

            st.image(images[0], use_container_width=True)

            if st.button(f"Xem ảnh {car}"):

                st.subheader(car)

                gallery = st.columns(2)

                for j,img in enumerate(images):

                    with gallery[j%2]:

                        st.image(img, use_container_width=True)

# ===============================
# BẢNG GIÁ
# ===============================

elif menu == "Bảng giá":

    st.header("Bảng giá thuê xe")

    if st.button("⚡ Báo giá nhanh"):

        try:
            df = pd.read_excel("khung_bao_gia.xlsx")
            st.dataframe(df)

        except:
            st.error("Không tìm thấy file Excel báo giá")

# ===============================
# FORM ĐẶT XE
# ===============================

elif menu == "Đặt xe":

    st.header("Form đặt xe")

    name = st.text_input("Tên khách hàng")
    phone = st.text_input("Số điện thoại")

    car = st.selectbox(
        "Chọn xe",
        ["Toyota Innova","Toyota Fortuner","Toyota Camry","Kia Carnival"]
    )

    date = st.date_input("Ngày thuê")

    note = st.text_area("Yêu cầu thêm")

    if st.button("Gửi yêu cầu"):

        if name and phone:
            st.success("Đã gửi yêu cầu. Chúng tôi sẽ liên hệ lại!")
        else:
            st.warning("Vui lòng nhập tên và số điện thoại")

# ===============================
# LIÊN HỆ + GOOGLE MAP
# ===============================

elif menu == "Liên hệ":

    st.header("Thông tin liên hệ")
    st.write("Ha Noi Tourist and Trading")
    st.write("📍Head office: 13th Floor, Tower of Hanoi, 49 Hai Ba Trung, Tran Hung Dao Ward, Hoan Kiem District, Hanoi City")
    st.write("📍 Executive office: 829 Bạch Đằng, Hà Nội")
    st.write("📞 Hotline: +84 4 39361030")
    st.write("📞 Hotline: +84 439367602")

    st.subheader("Bản đồ")

    st.components.v1.iframe(
        "https://maps.google.com/maps?q=829%20bach%20dang%20ha%20noi&t=&z=15&ie=UTF8&iwloc=&output=embed",
        height=450
    )

st.divider()
st.caption("© 2026 Dịch vụ cho thuê xe")
