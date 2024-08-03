import streamlit as st
import pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing
import matplotlib.pyplot as plt
import requests

# Load the California housing dataset
@st.cache_data #streamlit python decorator that caches the data so that we don't need to always run the below function
def load_data():
    cali = fetch_california_housing()
    data = pd.DataFrame(cali.data, columns=cali.feature_names)
    data['MedHouseVal'] = cali.target
    data.columns = [col_.lower() for col_ in data.columns]
    return data
data = load_data()


# Page 1: DataFrame and Interactive Plots
def page1():
    st.title("California Housing Prices")
    st.write("## DataFrame")
    st.dataframe(data)

    st.write("## Interactive Plots")
    
    # Map plot
    st.write("## Map of California Housing Prices")
    st.map(data[['latitude', 'longitude']])


    # Scatter plot
    x_axis = st.selectbox("Choose a variable for the x-axis", data.columns)
    y_axis = st.selectbox("Choose a variable for the y-axis", data.columns, index=1)

    plt.figure(figsize=(10, 6))
    plt.scatter(data[x_axis], data[y_axis], alpha=0.5)
    plt.title(f'Scatter plot of {x_axis} vs {y_axis}')
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    st.pyplot(plt)

if __name__ = '__main__':
    page1()