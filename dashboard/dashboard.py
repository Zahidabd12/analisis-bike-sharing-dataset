import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

main_data = pd.read_csv('main_data (1).csv')

st.sidebar.title("Bike Sharing Dashboard")
visual_option = st.sidebar.selectbox(
    "Pilih Visualisasi",
    [
        "Histogram Penggunaan",
        "Tren Waktu Harian",
        "Korelasi Heatmap",
    ],
)

# Visualisasi
if visual_option == "Histogram Penggunaan":
    st.header("Distribusi Penggunaan Sepeda")
    plt.figure(figsize=(10, 5))
    plt.hist(main_data['cnt'], bins=30, color='skyblue', edgecolor='black')
    plt.xlabel('Jumlah Sepeda')
    plt.ylabel('Frekuensi')
    plt.title('Histogram Jumlah Penggunaan Sepeda')
    st.pyplot(plt)

elif visual_option == "Tren Waktu Harian":
    st.header("Tren Waktu Penggunaan Sepeda Harian")
    main_data['dteday'] = pd.to_datetime(main_data['dteday'])
    plt.figure(figsize=(12, 6))
    plt.plot(main_data['dteday'], main_data['cnt'], label='Total Pengguna', color='green')
    plt.xlabel('Tanggal')
    plt.ylabel('Jumlah Pengguna')
    plt.title('Tren Penggunaan Sepeda Harian')
    plt.legend()
    st.pyplot(plt)

elif visual_option == "Korelasi Heatmap":
    st.header("Korelasi Antar Fitur")
    corr_matrix = main_data[['temp', 'hum', 'windspeed', 'cnt']].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Heatmap Korelasi Antar Fitur')
    st.pyplot(plt)

# Footer
st.sidebar.write("© 2025 Bike Sharing Dashboard")
