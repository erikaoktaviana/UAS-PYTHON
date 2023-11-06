import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Muat dataset
data = pd.read_csv("salaries.csv")

# Atur judul halaman
st.set_page_config(page_title="Salaries")


st.subheader("Dataset Salaries")
st.write(data)


sns.set_palette("hls")


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
rata_rata_gaji = []  # Membuat list untuk menyimpan rata-rata gaji

for lokasi in lokasi_pilihan:
    gaji_lokasi = filtered_data[filtered_data['company_location'] == lokasi]
    rata_rata = gaji_lokasi['salary'].mean()  
    rata_rata_gaji.append(rata_rata)  
    plt.bar(lokasi, rata_rata, label=lokasi)

plt.xlabel('Lokasi')
plt.ylabel('Rata-Rata Gaji')
plt.title('Perbandingan Gaji Rata-Rata Antar Kota')

# Tambahkan teks rata-rata gaji di atas batang
for i, v in enumerate(rata_rata_gaji):
    ax.text(i, v + 10, f"{v:.2f}", ha='center', va='bottom')
    
st.pyplot(fig)



st.header("")
st.header("")
# ---------------------------------------------------------------
st.subheader("Perbandingan Gaji Antar Jabatan")
# Membuat kolom pilihan jabatan
jabatan_pilihan = st.multiselect("Pilih Jabatan", data['job_title'].unique())

# Membuat grafik perbandingan gaji per jabatan
fig, ax = plt.subplots(figsize=(6, 6))
rata_rata_gaji = []  # Membuat list untuk menyimpan rata-rata gaji

for jabatan in jabatan_pilihan:
    gaji_jabatan = data[data['job_title'] == jabatan]
    rata_rata = gaji_jabatan['salary'].mean()  # Rata-rata gaji untuk jabatan saat ini
    rata_rata_gaji.append(rata_rata)  # Menambahkannya ke list

    plt.bar(jabatan, rata_rata, label=jabatan)

plt.xlabel('Jabatan')
plt.ylabel('Rata-Rata Gaji (USD)')
plt.title('Perbandingan Gaji per Jabatan')
plt.legend()

# Tambahkan teks rata-rata gaji di atas batang
for i, v in enumerate(rata_rata_gaji):
    ax.text(i, v + 10, f"${v:.2f}", ha='center', va='bottom')

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
rata_rata_gaji = []  # Membuat list untuk menyimpan rata-rata gaji

for tingkat in tingkat_pilihan:
    gaji_tingkat = filtered_data[filtered_data['experience_level'] == tingkat]
    rata_rata = gaji_tingkat['salary'].mean()  # Rata-rata gaji untuk tingkat pengalaman saat ini
    rata_rata_gaji.append(rata_rata)  # Menambahkannya ke list

    plt.bar(tingkat, rata_rata, label=tingkat)

plt.xlabel('Tingkat Pengalaman')
plt.ylabel('Rata-Rata Gaji')
plt.title('Perbandingan Gaji Antar Tingkat Pengalaman')
plt.legend()

# Tambahkan teks rata-rata gaji di atas batang
for i, v in enumerate(rata_rata_gaji):
    ax.text(i, v + 10, f"${v:.2f}", ha='center', va='bottom')

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
for i, row in count_per_size.iterrows():
    plt.bar(row['Ukuran Perusahaan'], row['Jumlah Perusahaan'])
    ax.text(i, row['Jumlah Perusahaan'] + 10, str(row['Jumlah Perusahaan']), ha='center', va='bottom')

plt.xlabel('Ukuran Perusahaan')
plt.ylabel('Jumlah Perusahaan')
plt.title('Jumlah Perusahaan Berdasarkan Ukuran')
st.pyplot(fig)




st.header("")
st.header("")
st.subheader("Perbandingan Gaji antara Kantor dan Remote")
# ---------------------------------------------------------------

# Filter data
office = data[data["remote_ratio"] == 0]  # Filter karyawan yang tidak remote
remote = data[data["remote_ratio"] > 0]   # Filter karyawan yang remote

# Hitung rata-rata gaji
office_salary = office["salary_in_usd"].mean()
remote_salary = remote["salary_in_usd"].mean()


# Buat DataFrame untuk grafik batang
bar_data = pd.DataFrame({
    "Lokasi Kerja": ["Kantor", "Remote"],
    "Gaji Rata-rata (USD)": [office_salary, remote_salary]
})
plt.xticks(rotation='horizontal')
# Tampilkan grafik batang
st.bar_chart(bar_data.set_index("Lokasi Kerja"))

# Tampilkan teks pada grafik
st.write("Gaji Rata-rata:")
st.write("Kantor: $", office_salary)
st.write("Remote: $", remote_salary)