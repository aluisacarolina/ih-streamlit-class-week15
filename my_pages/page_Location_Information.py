import streamlit as st
import requests
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


if __name__ = '__main__':
    page2()