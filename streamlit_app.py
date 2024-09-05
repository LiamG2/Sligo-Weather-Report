import streamlit as st
import pandas as pd
import requests
import xml.etree.ElementTree as ET

# Define the URL of the XML file
XML_URL = 'https://example.com/data.xml'  # Replace with the actual URL

@st.cache_data(ttl=60)
def fetch_and_parse_xml(url):
    """Fetch XML data from the URL and parse it into a DataFrame."""
    response = requests.get(url)
    response.raise_for_status()  # Check for request errors

    # Parse the XML content
    root = ET.fromstring(response.content)

    # Convert XML data to a list of dictionaries
    data = []
    for item in root.findall('.//record'):  # Adjust based on the XML structure
        record = {child.tag: child.text for child in item}
        data.append(record)

    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(data)
    return df

# Streamlit app layout
st.title("Live XML Data Viewer")
st.write("This app fetches and displays data from an external XML source.")

try:
    # Fetch and display data
    df = fetch_and_parse_xml(XML_URL)
    st.dataframe(df)
except Exception as e:
    st.error(f"Failed to fetch or parse XML data: {e}")
