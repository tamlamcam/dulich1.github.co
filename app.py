import streamlit as st

st.title("DỊCH VỤ CHO THUÊ XE DU LỊCH")

st.write("Chuyên cho thuê xe du lịch, đưa đón sân bay, công tác.")

st.header("Danh sách xe")

cars = {
    "Toyota Innova": "1.200.000 VND/ngày",
    "Ford Everest": "1.800.000 VND/ngày",
    "Kia Carnival": "2.500.000 VND/ngày",
    "Toyota Fortuner": "1.700.000 VND/ngày"
}

for car, price in cars.items():
    st.subheader(car)
    st.write("Giá thuê:", price)

st.header("Liên hệ")

name = st.text_input("Tên khách")
phone = st.text_input("Số điện thoại")

if st.button("Gửi yêu cầu"):
    st.success("Chúng tôi sẽ liên hệ lại!")
