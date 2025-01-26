import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

day_df = pd.read_csv('day.csv')
hour_df = pd.read_csv('hour.csv')

st.sidebar.title("Bike Sharing Dashboard")
visual_option = st.sidebar.selectbox(
    "Pilih Visualisasi", 
    ["Histogram Penggunaan", "Tren Waktu", "Korelasi Heatmap", "Analisis Hari Kerja vs Akhir Pekan"]
)

if visual_option == "Histogram Penggunaan":
    st.header("Distribusi Penggunaan Sepeda")
    plt.figure(figsize=(10, 5))
    plt.hist(day_df['cnt'], bins=30, color='skyblue', edgecolor='black')
    plt.xlabel('Jumlah Sepeda')
    plt.ylabel('Frekuensi')
    plt.title('Histogram Jumlah Penggunaan Sepeda')
    st.pyplot(plt)

elif visual_option == "Tren Waktu":
    st.header("Tren Waktu Penggunaan Sepeda")
    day_df['dteday'] = pd.to_datetime(day_df['dteday'])
    plt.figure(figsize=(12, 6))
    plt.plot(day_df['dteday'], day_df['cnt'], label='Total Pengguna', color='green')
    plt.xlabel('Tanggal')
    plt.ylabel('Jumlah Pengguna')
    plt.title('Tren Penggunaan Sepeda Harian')
    plt.legend()
    st.pyplot(plt)

elif visual_option == "Korelasi Heatmap":
    st.header("Korelasi Antar Fitur")
    corr_matrix = day_df[['temp', 'hum', 'windspeed', 'cnt']].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    st.pyplot(plt)

elif visual_option == "Analisis Hari Kerja vs Akhir Pekan":
    st.header("Perbandingan Hari Kerja dan Akhir Pekan")
    plt.figure(figsize=(8, 5))
    sns.barplot(x="workingday", y="cnt", data=day_df, palette="viridis")
    plt.xticks([0, 1], ['Akhir Pekan', 'Hari Kerja'])
    plt.xlabel('Hari')
    plt.ylabel('Jumlah Pengguna')
    plt.title('Perbandingan Hari Kerja vs Akhir Pekan')
    st.pyplot(plt)

st.sidebar.write("© 2025 Bike Sharing Dashboard")
