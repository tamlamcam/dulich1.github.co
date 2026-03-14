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

if menu == "Trang chủ":

    st.header("Các dòng xe của chúng tôi")

    cars = {
        "Toyota Innova": [
            st.image("Toyota Innova2.jpg",width=400),
            st.image("Toyota Innova2.jpg",width=400)
        ],

        "Toyota Fortuner":[
             st.image("Toyota Fortuner.jpg",width=400),
             st.image("Toyota Fortuner2.jpg",width=400)
        ],

        "Toyota Camry":[
            st.image("Toyota Camry.jpg",width=400),
            st.image("Toyota Camry2.jpg",width=400)
        ],

        "Kia Carnival":[
            st.image("Kia Carnival.jpg",width=400),
            st.image("Kia Carnival2.jpg",width=400)
        ]
    }

    cols = st.columns(4)

    i = 0
    for car, images in cars.items():

        with cols[i]:

            st.image(images[0])

            if st.button(f"Xem chi tiết {"Toyota Innova"}"):

                st.subheader("Toyota Innova")

                st.image("Toyota Innova.png")

        i += 1


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
