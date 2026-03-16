import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Dịch vụ thuê xe", page_icon="🚗", layout="wide")

# ===== CSS =====
st.markdown("""
<style>

/* Ẩn sidebar */
section[data-testid="stSidebar"]{
    display:none;
}

/* MENU */
.top-menu{
    position:fixed;
    top:0;
    left:0;
    right:0;
    background:#6ccf8f;
    padding:10px 40px;
    display:flex;
    align-items:center;
    gap:40px;
    z-index:999;
}

/* logo */
.logo{
    height:40px;
}

/* menu link */
.top-menu a{
    color:white;
    text-decoration:none;
    font-size:18px;
    font-weight:bold;
}

.top-menu a:hover{
    color:#eafff0;
}

/* đẩy nội dung xuống */
.main{
    margin-top:90px;
}

/* khung ảnh xe */
.car-card{
    width:100%;
    height:250px;
    overflow:hidden;
    border-radius:8px;
}

.car-card img{
    width:100%;
    height:100%;
    object-fit:cover;
}

</style>
""", unsafe_allow_html=True)

# ===== MENU =====
menu = st.query_params.get("menu","Trang chủ")

st.markdown("""
<div class="top-menu">

<a href="?menu=Trang chủ">
<img src="logo.png" class="logo">
</a>

<a href="?menu=Trang chủ">Trang chủ</a>
<a href="?menu=Bảng giá">Bảng giá</a>
<a href="?menu=Đặt xe">Đặt xe</a>
<a href="?menu=Liên hệ">Liên hệ</a>

</div>
""", unsafe_allow_html=True)

st.markdown('<div class="main">', unsafe_allow_html=True)

# ===== HEADER =====
st.title("Chauffeur & Limousine")
st.write("Đưa đón sân bay • Công tác • Du lịch • Sự kiện")

st.divider()

# ======================
# TRANG CHỦ
# ======================
if menu == "Trang chủ":

    st.header("Các dòng xe của chúng tôi")

    cars = {

        "Toyota Innova":[
            "Toyota Innova.jpg",
            "Toyota Innova3.jpg",
            "Toyota Innova4.jpg"
        ],

        "Toyota Fortuner":[
            "Toyota Fortuner.jpg",
            "Toyota Fortuner3.jpg",
            "Toyota Fortuner4.jpg"
        ],

        "Toyota Camry":[
            "Toyota Camry.jpg",
            "Toyota Camry3.jpg",
            "Toyota Camry4.jpg"
        ],

        "Kia Carnival":[
            "Kia Carnival.jpg",
            "Kia Carnival3.jpg",
            "Kia Carnival4.jpg"
        ]
    }

    cols = st.columns(4)

    for i,(car,images) in enumerate(cars.items()):

        with cols[i]:

            st.markdown('<div class="car-card">', unsafe_allow_html=True)

            if os.path.exists(images[0]):
                st.image(images[0], use_container_width=True)
            else:
                st.warning(f"Không tìm thấy ảnh {images[0]}")

            st.markdown('</div>', unsafe_allow_html=True)

            if st.button(car, key=car):

                st.subheader(car)

                for img in images:

                    if os.path.exists(img):
                        st.image(img, use_container_width=True)
                    else:
                        st.warning(f"Thiếu ảnh {img}")

# ======================
# BẢNG GIÁ
# ======================
elif menu == "Bảng giá":

    st.header("Bảng giá thuê xe")

    if st.button("⚡ Báo giá nhanh"):

        try:
            df = pd.read_excel("khung_bao_gia.xlsx")
            st.dataframe(df)

        except:
            st.error("Không tìm thấy file Excel báo giá")

# ======================
# FORM ĐẶT XE
# ======================
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

# ======================
# LIÊN HỆ
# ======================
elif menu == "Liên hệ":

    st.header("Thông tin liên hệ")

    st.write("Ha Noi Tourist and Trading")
    st.write("📍 Head office: 49 Hai Ba Trung, Hoan Kiem, Hanoi")
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

st.markdown("</div>", unsafe_allow_html=True)
