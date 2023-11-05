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





st.header("")
st.header("")
# ---------------------------------------------------------------
st.subheader("Perbandingan Gaji Rata-Rata Antar Kota")
# Membuat kolom pilihan lokasi
lokasi_pilihan = st.multiselect("Pilih Lokasi", data['company_location'].unique())

# Filter data berdasarkan lokasi yang dipilih
filtered_data = data[data['company_location'].isin(lokasi_pilihan)]

# Membuat grafik perbandingan gaji berdasarkan lokasi
fig, ax = plt.subplots(figsize=(6, 6))
for lokasi in lokasi_pilihan:
    gaji_lokasi = filtered_data[filtered_data['company_location'] == lokasi]
    plt.bar(lokasi, gaji_lokasi['salary'].mean(), label=lokasi)

plt.xlabel('Lokasi')
plt.ylabel('Rata-Rata Gaji')
plt.title('Perbandingan Gaji Rata-Rata Antar Kota')
plt.legend()
st.pyplot(fig)


st.header("")
st.header("")
# ---------------------------------------------------------------
st.subheader("Perbandingan Gaji Antar Jabatan")
# Membuat kolom pilihan jabatan
jabatan_pilihan = st.multiselect("Pilih Jabatan", data['job_title'].unique())

# Membuat grafik perbandingan gaji per jabatan
fig, ax = plt.subplots(figsize=(6, 6))
for jabatan in jabatan_pilihan:
    gaji_jabatan = data[data['job_title'] == jabatan]
    plt.bar(jabatan, gaji_jabatan['salary'], label=jabatan)

plt.xlabel('Jabatan')
plt.ylabel('Rata-Rata Gaji (USD)')
plt.title('Perbandingan Gaji per Jabatan') # Memutar label jabatan untuk memudahkan pembacaan
plt.legend()
st.pyplot(fig)



st.header("")
st.header("")
# ---------------------------------------------------------------
st.subheader("Perbandingan Gaji Antar Tingkat Pengalaman")
# Membuat kolom pilihan tingkat pengalaman
tingkat_pilihan = st.multiselect("Pilih Tingkat Pengalaman", data['experience_level'].unique())

# Filter data berdasarkan tingkat pengalaman yang dipilih
filtered_data = data[data['experience_level'].isin(tingkat_pilihan)]

# Membuat grafik perbandingan gaji
fig, ax = plt.subplots(figsize=(6, 6))
for tingkat in tingkat_pilihan:
    gaji_tingkat = filtered_data[filtered_data['experience_level'] == tingkat]
    plt.bar(tingkat, gaji_tingkat['salary'].mean(), label=tingkat)

plt.xlabel('Tingkat Pengalaman')
plt.ylabel('Rata-Rata Gaji')
plt.title('Perbandingan Gaji Antar Tingkat Pengalaman')
plt.legend()
st.pyplot(fig)


st.header("")
st.header("")
# ---------------------------------------------------------------
st.subheader("Jumlah Perusahaan Berdasarkan Ukuran")
# Membuat kolom pilihan untuk ukuran perusahaan
ukuran_pilihan = st.multiselect("Pilih Ukuran Perusahaan", data['company_size'].unique(), key="multiselect_ukuran")

# Filter data berdasarkan ukuran perusahaan yang dipilih
filtered_data = data[data['company_size'].isin(ukuran_pilihan)]

# Menghitung jumlah perusahaan per ukuran
count_per_size = filtered_data['company_size'].value_counts().reset_index()
count_per_size.columns = ['Ukuran Perusahaan', 'Jumlah Perusahaan']

# Membuat grafik jumlah perusahaan berdasarkan ukuran
fig, ax = plt.subplots(figsize=(6, 6))
plt.bar(count_per_size['Ukuran Perusahaan'], count_per_size['Jumlah Perusahaan'])
plt.xlabel('Ukuran Perusahaan')
plt.ylabel('Jumlah Perusahaan')
plt.title('Jumlah Perusahaan Berdasarkan Ukuran')
st.pyplot(fig)





