import streamlit as st
import joblib
model = joblib.load('model_prediksi_harga_rumah.pkl')

st.title("Prediksi Harga Rumah")

floorarea = st.number_input("Luas Bangunan (m2)", min_value=0.0)
bed = st.number_input("Jumlah Kamar Tidur", min_value=0)

if st.button("Prediksi"):
    data = [[floorarea, bed]]
    prediction = model.predict(data)
    st.success(f"Harga rumah diprediksi: Rp {prediction[0]:,.2f}")
