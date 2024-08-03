import streamlit as st
import pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing
import matplotlib.pyplot as plt
import requests

from my_pages import (
    page_Home as home,
    page_California_Dataset as page1,
    page_Location_Information as page2,
    page_Weather_information as page3)
   

# Sidebar Navigation
st.sidebar.title("Navigation")

page = st.sidebar.selectbox( 
    "Select a page", 
    [ "🏠 Home", "🏡 California Housing Prices", "🌍 Location Information", "☀️ Weather Information", ] )

options = st.sidebar.radio("Select a page", ["Home", "Page 1", "Page 2", "Page 3"]
)

if page == "🏠 Home":
    home.home() #the first home refers to the name of the file (page_Home as home), the last name refers to the name of the function that is inside the file
elif page == "🏡 California Housing Prices":
    page1.page1()
elif page == "🌍 Location Information":
    page2.page2()
else:
    page3.page3()