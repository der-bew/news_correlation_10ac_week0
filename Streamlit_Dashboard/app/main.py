#import the required libraries for the EDA
import pandas as pd
import numpy as np
import os
import streamlit as st

st.title('Solar Radiation Measurement EDA Dashboard')
st.subheader("Dataset Overview")

@st.cache_data(persist=True)
def open_data(dataset):
    df = pd.read_csv(os.path.join(dataset))
    return df

df = open_data("../data/clean_data.csv")


if st.button("Head"):
	st.write(df.head())
elif st.button("Tail"):
	st.write(df.tail())
elif st.button("Sample"):
    st.write(df.sample(10))
elif st.button("Shape"):
    st.write(df.shape)
elif st.button("Column Names"):
    st.write(df.columns)
else:
	st.write(df.sample(2))

st.markdown("## Show Summary of Dataset")
if st.button("Describe"):
	st.write(df.describe())
elif st.button("Info"):
    st.markdown("## INFO")
    st.write(df.info())





 
