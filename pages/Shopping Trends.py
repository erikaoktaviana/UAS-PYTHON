import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Muat dataset
data = pd.read_csv("shopping_trends.csv")

# Atur judul halaman
st.set_page_config(page_title="Shopping Trends")


st.subheader("Dataset Shopping Trends")
st.write(data)

st.header("")
st.header("")
st.subheader("Analisis Kualitas Produk")
# ---------------------------------------------------------------

# Pilih item yang ingin dianalisis
selected_item = st.selectbox("Pilih Item Purchased untuk Analisis", data["Item Purchased"].unique())

# Filter data berdasarkan item yang dipilih
filtered_data = data[data["Item Purchased"] == selected_item]

# Hitung statistik rating
max_rating = filtered_data["Review Rating"].max()
min_rating = filtered_data["Review Rating"].min()
avg_rating = filtered_data["Review Rating"].mean()

# Hitung warna yang paling sering dibeli
most_common_color = filtered_data["Color"].mode().values[0]

# Menemukan kategori untuk item yang dipilih
item_category = filtered_data["Category"].values[0]

# Tampilkan hasil analisis
st.write(f"Analisis untuk item {selected_item}:")
st.write(f"Rating Tertinggi: {max_rating}")
st.write(f"Rating Terendah: {min_rating}")
st.write(f"Rata-Rata Rating: {avg_rating}")
st.write(f"Warna Paling Sering Dibeli: {most_common_color}")
st.write(f"{selected_item} termasuk dalam kategori: {item_category}")




st.header("")
st.header("")
st.subheader("Menampilkan Distribusi Umur Pelanggan")
# ---------------------------------------------------------------
# Membuat histogram umur pelanggan
fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(data['Age'], bins=10, edgecolor='k', rwidth=0.8, color='skyblue')
ax.set_xlabel('Umur')
ax.set_ylabel('Jumlah Pelanggan')
ax.set_title('Distribusi Umur Pelanggan')

# Anotasi teks untuk jumlah orang pada setiap batang
bin_counts, bin_edges, _ = plt.hist(data['Age'], bins=10, rwidth=0.8)
for count, x in zip(bin_counts, bin_edges):
    if count > 0:
        ax.annotate(str(int(count)), xy=(x, count), xytext=(25, 5), textcoords='offset points', ha='center', va='bottom')

# Menampilkan grafik menggunakan st.pyplot() dengan objek gambar (figure)
st.pyplot(fig)



st.header("")
st.header("")
st.subheader("Menampilkan Distribusi Kategori Pembelian")
# ---------------------------------------------------------------
# Membuat histogram Kategori 
fig, ax = plt.subplots(figsize=(6, 6))
ax.hist(data['Category'], bins=10, edgecolor='k', rwidth=0.3, color='skyblue')
ax.set_xlabel('Category')
ax.set_ylabel('Jumlah Pelanggan')
ax.set_title('Distribusi Kategori Pembelian')

# Anotasi teks untuk jumlah orang pada setiap batang
bin_counts, bin_edges, _ = plt.hist(data['Category'], bins=10)
for count, x in zip(bin_counts, bin_edges):
    if count > 0:
        ax.annotate(str(int(count)), xy=(x, count), xytext=(15, 0), textcoords='offset points', ha='center', va='bottom')

# Menampilkan grafik menggunakan st.pyplot() dengan objek gambar (figure)
st.pyplot(fig)




st.header("")
st.header("")
st.subheader("Menampilkan Metode Pembayaran yang Populer")
# ---------------------------------------------------------------
# Membuat pie chart untuk metode pembayaran yang disukai
fig, ax = plt.subplots(figsize=(6, 6))
payment_counts = data['Preferred Payment Method'].value_counts()
plt.pie(payment_counts, labels=payment_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Pie Chart Metode Pembayaran yang Populer')
plt.show()
st.pyplot(fig)




st.header("")
st.header("")
st.subheader("Pengaruh Diskon terhadap Pembelian")
# ---------------------------------------------------------------
# Menghitung rata-rata pembelian per tingkat diskon
average_purchase_by_discount = data.groupby('Discount Applied')['Purchase Amount (USD)'].mean().reset_index()

# Membuat grafik line chart
fig, ax = plt.subplots()
ax.plot(average_purchase_by_discount['Discount Applied'], average_purchase_by_discount['Purchase Amount (USD)'], marker='o')
ax.set_xlabel('Discount Applied (%)')
ax.set_ylabel('Average Purchase Amount (USD)')
ax.set_title('Pengaruh Diskon terhadap Pembelian')

for i, v in enumerate(average_purchase_by_discount['Purchase Amount (USD)']):
    ax.text(average_purchase_by_discount['Discount Applied'][i], v, f"{v:.2f}", ha='right', va='bottom')

# Tampilkan grafik menggunakan st.pyplot()
st.pyplot(fig)




st.header("")
st.header("")
st.subheader("Statistik Deskriptif untuk Rating Ulasan (Review Rating)")
# ---------------------------------------------------------------
rating_stats = data["Review Rating"].describe()
st.write(rating_stats)













