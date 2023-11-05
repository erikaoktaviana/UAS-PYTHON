import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Muat dataset
data = pd.read_csv("salaries.csv")

# Atur judul halaman
st.set_page_config(page_title="Salaries")


st.subheader("Dataset Salaries")
st.write(data)


st.header("")
st.header("")
# ---------------------------------------------------------------
st.subheader("Menampilkan Gaji di Setiap Kota Berdasarkan Jabatan Tertentu")
# Menentukan pilihan jabatan
jabatan_tertentu = st.selectbox("Pilih Jabatan", data['job_title'].unique())

# Filter data berdasarkan jabatan yang dipilih
data_tertentu = data[data['job_title'] == jabatan_tertentu]

# Filter data hanya untuk menampilkan informasi kota dan gaji
data_tabel = data_tertentu[['company_location', 'salary','salary_in_usd']]

# Tampilkan tabel data
st.subheader(f"Detail Gaji {jabatan_tertentu} per Kota")
st.write(data_tabel)




