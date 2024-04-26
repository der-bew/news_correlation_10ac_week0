#import the required libraries for the EDA
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import streamlit as st

st.title('Solar Radiation Measurement EDA Dashboard')
st.subheader("Wind EDA")

@st.cache_data(persist=True)
def open_data(dataset):
    df = pd.read_csv(os.path.join(dataset))
    return df

df = open_data("../data/clean_data.csv")

menu = ["LinePlot", "Scatterplot"]
choice = st.sidebar.selectbox("Select a visualization", menu)

wind_data = df.groupby(['Timestamp']).mean()[['WS', 'WSgust', 'WSstdev', 'WD','WDstdev']]
wind_data.reset_index(inplace=True)
if choice == "LinePlot":
    wind_line = st.radio('**Show Plot for**: ',('WS', 'WSgust', 'WSstdev', 'WD','WDstdev'))
    if wind_line == "WS":
        fig, ax = plt.subplots()
        plt.plot(wind_data['Timestamp'], wind_data['WS'], color='blue')
        ax.set_title('Wind Speed (WS)')
        ax.set_xlabel('Time')
        ax.set_ylabel('Wind Speed (m/s)')
        st.pyplot(fig)
    elif wind_line == "WSgust":
        fig, ax = plt.subplots()
        plt.plot(wind_data['Timestamp'], wind_data['WSgust'], color='orange')
        ax.set_title('WSgust')
        ax.set_xlabel('Time')
        ax.set_ylabel('WSgust (m/s)')
        st.pyplot(fig)
    elif wind_line == "WSstdev":
        fig, ax = plt.subplots()
        plt.plot(wind_data['Timestamp'], wind_data['WSstdev'], color='green')
        ax.set_title('Wind Speed Standard Deviation (WSstdev)')
        ax.set_xlabel('Time')
        ax.set_ylabel('Wind Speed Std Dev (m/s)')
        st.pyplot(fig)
    elif wind_line == "WD":
        fig, ax = plt.subplots()
        plt.plot(wind_data['Timestamp'], wind_data['WD'], color='red')
        ax.set_title('Wind Direction (WD)')
        ax.set_xlabel('Time')
        ax.set_ylabel('Wind Direction (degrees)')
        st.pyplot(fig)
    else:
        fig, ax = plt.subplots()
        plt.plot(wind_data['Timestamp'], wind_data['WDstdev'], color='purple')
        ax.set_title('Wind Direction Standard Deviation (WDstdev)')
        ax.set_xlabel('Time')
        ax.set_ylabel('Wind Direction Std Dev (degrees)')
        st.pyplot(fig)
else:
    st.title('Wind Speed (WS) vs. Ambient Temperature')
    plot = sns.scatterplot(x='WS', y='Tamb', data=df, color='green')
    st.pyplot(plot.get_figure())
    