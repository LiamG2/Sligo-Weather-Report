import streamlit as st
import pandas as pd
import requests
import xml.etree.ElementTree as ET

# Define the URL of the XML file
XML_URL = 'https://www.met.ie/Open_Data/xml/county_forecast.xml'

@st.cache_data(ttl=60)
def fetch_and_parse_xml(url):
    """Fetch XML data from the URL and parse it into a DataFrame."""
    response = requests.get(url)
    response.raise_for_status()  # Check for request errors

    # Parse the XML content
    root = ET.fromstring(response.content)

    # Prepare data for DataFrame
    data = []
    for county in root.findall('.//county'):
        # Extract relevant information with checks
        county_name = county.find('name').text if county.find('name') is not None else 'N/A'
        province = county.find('province').text if county.find('province') is not None else 'N/A'
        today_forecast = county.find('today').text if county.find('today') is not None else 'N/A'
        tonight_forecast = county.find('tonight').text if county.find('tonight') is not None else 'N/A'
        tomorrow_forecast = county.find('tomorrow').text if county.find('tomorrow') is not None else 'N/A'

        # Append data to the list
        data.append({
            'County': county_name,
            'Province': province,
            'Today': today_forecast,
            'Tonight': tonight_forecast,
            'Tomorrow': tomorrow_forecast
        })

    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(data)
    return df

# Streamlit app layout
st.title("Irish County Weather Forecast")
st.write("This app fetches and displays the latest weather forecast for Irish counties.")

try:
    # Fetch and display data
    df = fetch_and_parse_xml(XML_URL)
    st.dataframe(df)
except Exception as e:
    st.error(f"Failed to fetch or parse XML data: {e}")
