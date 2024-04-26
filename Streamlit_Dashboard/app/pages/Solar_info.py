#import the required libraries for the EDA
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import streamlit as st

st.title('Solar Radiation Measurement EDA Dashboard')
st.subheader("Solar Radation EDA")

# read csv file
@st.cache_data(persist=True)
def open_data(dataset):
    df = pd.read_csv(os.path.join(dataset))
    return df

df = open_data("../data/clean_data.csv")

menu = ["LinePlot", "Histograms", "Boxplot", "Heatmap"]
choice = st.sidebar.selectbox("Select a visualization", menu)

# group data by Timestamp column for Timeseries plot
grouped_df = df.groupby(['Timestamp']).mean()[['GHI', 'DNI', 'DHI', 'Tamb']]
grouped_df.reset_index(inplace=True)
if choice == "LinePlot":
    cols = ['GHI', 'DNI', 'DHI', 'Tamb']
    colors = ['b', 'g', 'r', 'm'] # blue, green, red, magenta
    fig, ax= plt.subplots()
    for col, color in zip(cols, colors):
        plt.plot(grouped_df['Timestamp'], grouped_df[col], label=col, color=color)
    st.title('Time Series Plot of GHI, DNI, DHI, and Tamb')
    ax.set_xlabel('Timestamp', fontsize=15)
    ax.set_ylabel('GHI, DNI, DHI, and Tamb Values', fontsize=15)
    plt.xticks(rotation=30)
    plt.legend()
    st.pyplot(fig)
elif choice == "Histograms":
    solar_hist = st.radio('**Show Plot for**: ',('GHI', 'DNI', 'DHI'))
    if solar_hist == "GHI":
        fig, ax = plt.subplots()
        sns.histplot(grouped_df['GHI'], bins=20, kde=True, color='blue', ax=ax)
        ax.set_title('Global Horizontal Irradiance (GHI) Histogram')
        st.pyplot(fig)
    elif solar_hist == "DNI":
        fig, ax = plt.subplots()
        sns.histplot(grouped_df['DNI'], bins=20, kde=True, color='orange', ax=ax)
        ax.set_title('Direct Normal Irradiance (DNI) Histogram')
        st.pyplot(fig)
    else:
        fig, ax = plt.subplots()
        sns.histplot(grouped_df['DHI'], bins=20, kde=True, color='green', ax=ax)
        ax.set_title('Diffuse Horizontal Irradiance (DHI) Histogram')
        st.pyplot(fig)
elif choice == "Boxplot":
    fig, ax = plt.subplots()
    sns.boxplot(data=df[['GHI', 'DNI', 'DHI']], ax=ax)
    ax.set_title('Solar Radiation Boxplot')
    st.pyplot(fig)
elif choice == "Heatmap":
    st.title("Solar Radation Heatmap")
    plot = sns.heatmap(df[['GHI', 'DNI', 'DHI']].corr(), annot=True)
    st.pyplot(plot.get_figure())