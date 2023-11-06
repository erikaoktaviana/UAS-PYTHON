import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Muat dataset
data = pd.read_csv("customer_shopping_data.csv")

# Atur judul halaman
st.set_page_config(page_title="Customer Shopping")

# Tampilkan data pelanggan
st.subheader("Dataset Customer Shopping")
st.write(data)

# Hitung dan tampilkan total jumlah customer
total_customer = data.shape[0]  # Menghitung jumlah baris dalam DataFrame
st.subheader('Total Customer:')
st.write(f'Total: {total_customer}')




st.header("")
st.header("")
st.subheader('Menampilkan Grafik Jumlah Pembelian per Shopping Mall')
# ---------------------------------------------------------------
# Hitung jumlah pembelian di setiap pusat perbelanjaan
jumlah_pembelian_per_shopping_mall = data['shopping_mall'].value_counts()


fig, ax = plt.subplots(figsize=(12, 6))
sns.countplot(x='shopping_mall', data=data, ax=ax)
plt.xticks(rotation='horizontal')
st.pyplot(fig)

# Tampilkan jumlah pembelian di setiap pusat perbelanjaan
st.subheader('Jumlah Pembelian per Shopping Mall:')
st.write(jumlah_pembelian_per_shopping_mall)





st.header("")
st.header("")
st.subheader("Visualisasi Data Pembelian per Category di Setiap Mall")
# ---------------------------------------------------------------

# Buat pilihan (select) untuk filter berdasarkan kategori produk
selected_category = st.selectbox("Pilih Kategori Produk:", data['category'].unique())

# Filter data berdasarkan kategori produk yang dipilih
filtered_data = data[data['category'] == selected_category]
st.subheader(f"Data Pembelian Untuk Kategori Produk: {selected_category}")

# Hitung jumlah pembelian per pusat perbelanjaan
jumlah_pembelian_per_mall = filtered_data['shopping_mall'].value_counts().reset_index()
jumlah_pembelian_per_mall.columns = ['Shopping Mall', 'Jumlah Pembelian']

# Grafik jumlah pembelian per pusat perbelanjaan
fig, ax = plt.subplots(figsize=(16, 6))
sns.barplot(x='Shopping Mall', y='Jumlah Pembelian', data=jumlah_pembelian_per_mall, ax=ax)
plt.xticks(rotation='horizontal')

# Tambahkan teks jumlah pembelian di atas batang
for i, v in enumerate(jumlah_pembelian_per_mall['Jumlah Pembelian']):
    ax.text(i, v + 10, str(v), ha='center', va='bottom')

st.pyplot(fig)




st.header("")
st.header("")
st.subheader("Menampilkan Distribusi Umur Pelanggan")
# ---------------------------------------------------------------
# Membuat histogram umur pelanggan
fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(data['age'], bins=10, edgecolor='k', rwidth=0.8, color='skyblue')
ax.set_xlabel('Umur')
ax.set_ylabel('Jumlah Pelanggan')
ax.set_title('Distribusi Umur Pelanggan')

# Anotasi teks untuk jumlah orang pada setiap batang
bin_counts, bin_edges, _ = plt.hist(data['age'], bins=10, rwidth=0.8)
for count, x in zip(bin_counts, bin_edges):
    if count > 0:
        ax.annotate(str(int(count)), xy=(x, count), xytext=(25, 5), textcoords='offset points', ha='center', va='bottom')

# Menampilkan grafik menggunakan st.pyplot() dengan objek gambar (figure)
st.pyplot(fig)





st.header("")
st.header("")
st.subheader("Menampilkan Jumlah Pembayaran per Metode")
# ---------------------------------------------------------------

# Hitung jumlah pembayaran per metode
jumlah_per_metode = data['payment_method'].value_counts()

# Tampilkan grafik pie
fig, ax = plt.subplots(figsize=(8, 8))
jumlah_per_metode.plot(kind='pie', autopct='%1.1f%%', startangle=140)
ax.set_ylabel('')  
st.pyplot(fig)



st.header("")
st.header("")
st.subheader('Menampilkan Grafik Jumlah Invoice per Tahun')
# ---------------------------------------------------------------
# Konversi kolom 'invoice_date' ke tipe datetime
data['invoice_date'] = pd.to_datetime(data['invoice_date'], format="%d/%m/%Y", dayfirst=True)
data['tahun'] = data['invoice_date'].dt.year

# Hitung jumlah invoice per tahun
jumlah_invoice_pertahun = data.groupby('tahun')['invoice_date'].count()


fig, ax = plt.subplots(figsize=(10, 6))
jumlah_invoice_pertahun.plot(kind='bar', ax=ax)
plt.xlabel('Tahun')
plt.ylabel('Jumlah Invoice')
plt.xticks(rotation='horizontal')

# Anotasi teks untuk jumlah pembelian pada setiap batang
for i, v in enumerate(jumlah_invoice_pertahun):
    ax.text(i, v + 10, str(v), ha='center', va='bottom')

st.pyplot(fig)







