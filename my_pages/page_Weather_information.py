import streamlit as slt
import requests 

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


if __name__ = '__main__':
    page3()