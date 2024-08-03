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

# Home Page
def home():
    """Function that renders the main home page"""
    st.title("Welcome to our first Streamlit APP!")

    st.write(""" 
             # Introduction:
             #### Streamlit is an open-source python package that allows us to create apps in a seamless form
             """)

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

 # Page 2: Get City/Address from Latitude and Longitude
def page2():
    st.title("Get Location Information")
    st.write("Enter the latitude and longitude to get the location information.")

    lat = st.number_input("Latitude", format="%.6f")
    lon = st.number_input("Longitude", format="%.6f")


    if st.button("Get Location"):
        # using API https://www.geonames.org/
        response = requests.get(f"http://api.geonames.org/findNearbyPlaceNameJSON?lat={lat}&lng={lon}&username=gorgias_demand_gen")
        if response.status_code == 200:
            location_info = response.json()
            if location_info['geonames']:
                st.write("Location Information:")
                for loc in location_info['geonames']:
                    st.write(f"Name: {loc['name']}")
                    st.write(f"Country: {loc['countryName']}")
                    st.write(f"Population: {loc['population']}")
                    st.write(f"Info: {location_info['geonames']}")
                    st.write("---")

                 # Store city name in session state
                st.session_state.city_name = loc['name']
            else:
                st.write("No location information found.")
        else:
            st.write("Failed to retrieve location information.")

# Page 3: Get Weather Information
def page3():
    st.title("Get Weather Information")

    # Retrieve city name from session state
    city = st.session_state.get("city_name", None)

    if city:
        st.write(f"City: {city}")
        weather_api_key = "5a68dbd3fe6242678ac130253242505"  # Replace with your actual OpenWeather API key
        url = f'https://api.weatherapi.com/v1/current.json?key={weather_api_key}&q={city}&aqi=no'
        response = requests.get(url)
        if response.status_code == 200:
            weather_info = response.json()
            st.write(f"Weather in {weather_info['location']['name']}, {weather_info['location']['country']}:")
            st.write(f"Temperature: {weather_info['current']['temp_c']}°C")
            st.write(f"Weather: {weather_info['current']['condition']['text']}")
            st.write(f"Humidity: {weather_info['current']['humidity']}%")
            st.write(f"Wind: {weather_info['current']['wind_kph']} kph")
        else:
            st.write("Failed to retrieve weather information.")
    else:
        st.write("No city information available. Please go to Page 2 and get the city information first.")
   

# Sidebar Navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Select a page", ["Home", "Page 1", "Page 2", "Page 3"])

if options == "Home":
    home()
elif options == "Page 1":
    page1()
elif options == "Page 2":
    page2()
elif options == "Page 3":
    page3()