#import the required libraries for the EDA
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title('Solar Radiation Measurement Data Dashboard')
slider_value = st.slider('Select a range', 0.0, 100.0, (25.0, 75.0))
st.write(f'You selected: {slider_value}')