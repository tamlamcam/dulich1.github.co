import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dịch vụ cho thuê xe", page_icon="🚗", layout="wide")

# CSS giao diện
st.markdown("""
<style>
.main-title{
    font-size:40px;
    font-weight:bold;
    text-align:center;
}
.subtitle{
    text-align:center;
    font-size:18px;
}
.card{
    padding:10px;
    border-radius:10px;
    box-shadow:0px 0px 10px #ccc;
}
</style>
""", unsafe_allow_html=True)

# HEADER
st.markdown('<p class="main-title">🚗 DỊCH VỤ CHO THUÊ XE DU LỊCH</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Đưa đón sân bay • Công tác • Du lịch • Sự kiện</p>', unsafe_allow_html=True)

st.divider()

# MENU
menu = st.radio(
    "Menu",
    ["Trang chủ", "Giới thiệu xe", "Bảng giá", "Đặt xe"],
    horizontal=True
)

# =========================
# TRANG CHỦ
# =========================

if menu == "Trang chủ":

    st.header("Các dòng xe phổ biến")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("https://upload.wikimedia.org/wikipedia/commons/3/3e/Toyota_Innova.jpg")
        st.subheader("Toyota Innova")

    with col2:
        st.image("https://upload.wikimedia.org/wikipedia/commons/7/70/Toyota_Fortuner.jpg")
        st.subheader("Toyota Fortuner")

    with col3:
        st.image("https://upload.wikimedia.org/wikipedia/commons/0/02/Kia_Carnival.jpg")
        st.subheader("Kia Carnival")

    st.info("Bấm vào mục **Giới thiệu xe** để xem chi tiết nội thất và ngoại thất.")

# =========================
# GALLERY XE
# =========================

elif menu == "Giới thiệu xe":

    st.header("Gallery xe")

    car = st.selectbox(
        "Chọn mẫu xe",
        ["Toyota Innova", "Toyota Fortuner", "Toyota Camry", "Kia Carnival"]
    )

    if car == "Toyota Innova":

        st.subheader("Toyota Innova")

        col1, col2 = st.columns(2)

        with col1:
            st.image("https://upload.wikimedia.org/wikipedia/commons/3/3e/Toyota_Innova.jpg", caption="Ngoại thất")

        with col2:
            st.image("https://upload.wikimedia.org/wikipedia/commons/5/55/Toyota_Innova_interior.jpg", caption="Nội thất")

        st.write("Xe 7 chỗ rộng rãi, phù hợp đưa đón sân bay và du lịch gia đình.")

    elif car == "Toyota Fortuner":

        st.subheader("Toyota Fortuner")

        col1, col2 = st.columns(2)

        with col1:
            st.image("https://upload.wikimedia.org/wikipedia/commons/7/70/Toyota_Fortuner.jpg", caption="Ngoại thất")

        with col2:
            st.image("https://upload.wikimedia.org/wikipedia/commons/2/2e/Fortuner_interior.jpg", caption="Nội thất")

        st.write("SUV 7 chỗ mạnh mẽ, phù hợp đi tỉnh và công tác.")

    elif car == "Toyota Camry":

        st.subheader("Toyota Camry")

        col1, col2 = st.columns(2)

        with col1:
            st.image("https://upload.wikimedia.org/wikipedia/commons/8/8c/Toyota_Camry.jpg", caption="Ngoại thất")

        with col2:
            st.image("https://upload.wikimedia.org/wikipedia/commons/5/56/Toyota_Camry_interior.jpg", caption="Nội thất")

        st.write("Sedan cao cấp cho khách VIP và doanh nhân.")

    elif car == "Kia Carnival":

        st.subheader("Kia Carnival")

        col1, col2 = st.columns(2)

        with col1:
            st.image("https://upload.wikimedia.org/wikipedia/commons/0/02/Kia_Carnival.jpg", caption="Ngoại thất")

        with col2:
            st.image("https://upload.wikimedia.org/wikipedia/commons/6/6e/Kia_Carnival_interior.jpg", caption="Nội thất")

        st.write("MPV cao cấp 7-8 chỗ, nội thất rộng rãi.")

# =========================
# BẢNG GIÁ
# =========================

elif menu == "Bảng giá":

    st.header("Bảng giá thuê xe")

    if st.button("⚡ Báo giá nhanh"):

        try:
            df = pd.read_excel("khung_bao_gia.xlsx")
            st.dataframe(df)

        except:
            st.error("Không tìm thấy file Excel báo giá")

# =========================
# FORM ĐẶT XE
# =========================

elif menu == "Đặt xe":

    st.header("Form đặt xe")

    name = st.text_input("Tên khách hàng")
    phone = st.text_input("Số điện thoại")

    car = st.selectbox(
        "Chọn xe",
        ["Toyota Innova", "Toyota Fortuner", "Toyota Camry", "Kia Carnival"]
    )

    date = st.date_input("Ngày thuê xe")

    note = st.text_area("Yêu cầu thêm")

    if st.button("Gửi yêu cầu đặt xe"):

        if name and phone:
            st.success("Yêu cầu đã được gửi. Chúng tôi sẽ liên hệ lại!")
        else:
            st.warning("Vui lòng nhập tên và số điện thoại")

st.divider()

st.caption("© 2026 Dịch vụ cho thuê xe du lịch")
