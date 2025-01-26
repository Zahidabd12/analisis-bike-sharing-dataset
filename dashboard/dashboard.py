import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
day_df = pd.read_csv('day.csv')
hour_df = pd.read_csv('hour.csv')

# Dashboard Title
st.title('Bike Sharing Data Analysis Dashboard')

# Sidebar
st.sidebar.header('Filter Options')

# Filter by season
season = st.sidebar.selectbox('Select Season:', day_df['season'].unique())
filtered_data = day_df[day_df['season'] == season]

# Overview of Data
st.header('Data Overview')
st.write("Day Dataset:")
st.dataframe(day_df.head())
st.write("Hour Dataset:")
st.dataframe(hour_df.head())

# Line Chart for Daily Rental Trends
st.header('Daily Rental Trends')
plt.figure(figsize=(10, 5))
plt.plot(filtered_data['dteday'], filtered_data['cnt'], marker='o', linestyle='-', color='b')
plt.xlabel('Date')
plt.ylabel('Total Rentals')
plt.title('Total Bike Rentals Over Time')
st.pyplot(plt)

# Hourly Rentals Analysis
st.header('Hourly Rentals Trends')
selected_hour = st.sidebar.slider('Select Hour:', 0, 23, 12)
hour_filtered = hour_df[hour_df['hr'] == selected_hour]
st.bar_chart(hour_filtered[['hr', 'cnt']].set_index('hr'))

# Summary Statistics
st.header('Summary Statistics')
st.write(filtered_data.describe())

# Run the app with: streamlit run script_name.py
