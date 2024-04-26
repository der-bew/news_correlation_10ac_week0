#import the required libraries for the EDA
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import streamlit as st

st.title('Solar Radiation Measurement EDA Dashboard')
st.subheader("Temprature EDA")
fig, ax= plt.subplots()
@st.cache_data(persist=True)
def open_data(dataset):
    df = pd.read_csv(os.path.join(dataset))
    return df

df = open_data("../data/clean_data.csv")

menu = ["Boxplot", "Heatmap"]
choice = st.sidebar.selectbox("Select a visualization", menu)

if choice == "Boxplot":
    fig, ax= plt.subplots()
    sns.boxplot(data=df[['Tamb', 'TModA', 'TModB']], ax=ax)
    ax.set_title('Temperature Boxplot')
    st.pyplot(fig) 
else:
    st.title("Temperature Heatmap")
    plot = sns.heatmap(df[['Tamb', 'TModA', 'TModB']].corr(), annot=True)
    st.pyplot(plot.get_figure())
    