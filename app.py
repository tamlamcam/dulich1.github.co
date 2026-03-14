import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dịch vụ thuê xe", page_icon="🚗", layout="wide")

# ===== LOGO =====
col1, col2 = st.columns([1,4])

with col1:
    st.image("logo.png", width=120)

with col2:
    st.title("DỊCH VỤ CHO THUÊ XE DU LỊCH")
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
            "https://upload.wikimedia.org/wikipedia/commons/3/3e/Toyota_Innova.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/5/55/Toyota_Innova_interior.jpg"
        ],

        "Toyota Fortuner":[
            "https://upload.wikimedia.org/wikipedia/commons/7/70/Toyota_Fortuner.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/2/2e/Fortuner_interior.jpg"
        ],

        "Toyota Camry":[
            "https://upload.wikimedia.org/wikipedia/commons/8/8c/Toyota_Camry.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/5/56/Toyota_Camry_interior.jpg"
        ],

        "Kia Carnival":[
            "https://upload.wikimedia.org/wikipedia/commons/0/02/Kia_Carnival.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/6/6e/Kia_Carnival_interior.jpg"
        ]
    }

    cols = st.columns(4)

    i = 0
    for car, images in cars.items():

        with cols[i]:

            st.image(images[0])

            if st.button(f"Xem chi tiết {car}"):

                st.subheader(car)

                st.image(images)

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

    st.write("📍 Địa chỉ: 829 Bạch Đằng, Hà Nội")
    st.write("📞 Hotline: 0900 000 000")

    st.subheader("Bản đồ")

    st.components.v1.iframe(
        "https://maps.google.com/maps?q=829%20bach%20dang%20ha%20noi&t=&z=15&ie=UTF8&iwloc=&output=embed",
        height=450
    )

st.divider()
st.caption("© 2026 Dịch vụ cho thuê xe")
