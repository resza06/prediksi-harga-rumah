import streamlit as st
import joblib

model = joblib.load('model_prediksi_harga_rumah.pkl')

def format_rupiah_auto(nominal):
    if nominal >= 1_000_000_000:
        return f"Rp {nominal / 1_000_000_000:.2f} miliar"
    elif nominal >= 1_000_000:
        return f"Rp {nominal / 1_000_000:.2f} juta"
    else:
        return f"Rp {nominal:,.2f}"

st.title("Prediksi Harga Rumah")

floorarea = st.number_input("Luas Bangunan (m²)", min_value=0.0, format="%.2f")
bed = st.number_input("Jumlah Kamar Tidur", min_value=0)

if st.button("Prediksi"):
    data = [[floorarea, bed]]
    prediction = model.predict(data)
    harga = prediction[0]

    harga_format = format_rupiah_auto(harga)

    st.success(f"Estimasi harga rumah: {harga_format}")
   
