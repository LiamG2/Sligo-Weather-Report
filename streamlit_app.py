import streamlit as st
import pandas as pd
import requests
import xml.etree.ElementTree as ET
from lxml import etree
import xmltodict
from bs4 import BeautifulSoup

# Define the URL of the XML file
XML_URL = 'https://www.met.ie/Open_Data/xml/county_forecast.xml'

@st.cache_data(ttl=60)
def fetch_xml_data(url):
    """Fetch XML data from the URL."""
    response = requests.get(url)
    response.raise_for_status()  # Check for request errors
    return response.content
'''
# Method 1: Using xml.etree.ElementTree
def parse_with_elementtree(xml_data):
    """Parse XML using xml.etree.ElementTree."""
    root = ET.fromstring(xml_data)
    data = []
    for county in root.findall('.//county'):
        county_name = county.find('name').text if county.find('name') is not None else 'N/A'
        province = county.find('province').text if county.find('province') is not None else 'N/A'
        today_forecast = county.find('today').text if county.find('today') is not None else 'N/A'
        tonight_forecast = county.find('tonight').text if county.find('tonight') is not None else 'N/A'
        tomorrow_forecast = county.find('tomorrow').text if county.find('tomorrow') is not None else 'N/A'
        data.append({
            'County': county_name,
            'Province': province,
            'Today': today_forecast,
            'Tonight': tonight_forecast,
            'Tomorrow': tomorrow_forecast
        })
    return pd.DataFrame(data)
'''

# Method 2: Using pandas read_xml
def parse_with_pandas(xml_data):
    """Parse XML using pandas read_xml."""
    try:
        df = pd.read_xml(xml_data)
        return df
    except Exception as e:
        st.error(f"pandas read_xml failed: {e}")
        return pd.DataFrame()

# Method 3: Using lxml
def parse_with_lxml(xml_data):
    """Parse XML using lxml."""
    parser = etree.XMLParser(recover=True)
    root = etree.fromstring(xml_data, parser=parser)
    data = []
    for county in root.xpath('//county'):
        county_name = county.findtext('name', 'N/A')
        province = county.findtext('province', 'N/A')
        today_forecast = county.findtext('today', 'N/A')
        tonight_forecast = county.findtext('tonight', 'N/A')
        tomorrow_forecast = county.findtext('tomorrow', 'N/A')
        data.append({
            'County': county_name,
            'Province': province,
            'Today': today_forecast,
            'Tonight': tonight_forecast,
            'Tomorrow': tomorrow_forecast
        })
    return pd.DataFrame(data)

# Method 4: Using xmltodict
def parse_with_xmltodict(xml_data):
    """Parse XML using xmltodict."""
    try:
        doc = xmltodict.parse(xml_data)
        counties = doc.get('forecast', {}).get('county', [])
        data = []
        for county in counties:
            data.append({
                'County': county.get('name', 'N/A'),
                'Province': county.get('province', 'N/A'),
                'Today': county.get('today', 'N/A'),
                'Tonight': county.get('tonight', 'N/A'),
                'Tomorrow': county.get('tomorrow', 'N/A')
            })
        return pd.DataFrame(data)
    except Exception as e:
        st.error(f"xmltodict failed: {e}")
        return pd.DataFrame()

# Method 5: Using BeautifulSoup
def parse_with_beautifulsoup(xml_data):
    """Parse XML using BeautifulSoup."""
    soup = BeautifulSoup(xml_data, 'xml')
    data = []
    for county in soup.find_all('county'):
        county_name = county.find('name').text if county.find('name') else 'N/A'
        province = county.find('province').text if county.find('province') else 'N/A'
        today_forecast = county.find('today').text if county.find('today') else 'N/A'
        tonight_forecast = county.find('tonight').text if county.find('tonight') else 'N/A'
        tomorrow_forecast = county.find('tomorrow').text if county.find('tomorrow') else 'N/A'
        data.append({
            'County': county_name,
            'Province': province,
            'Today': today_forecast,
            'Tonight': tonight_forecast,
            'Tomorrow': tomorrow_forecast
        })
    return pd.DataFrame(data)

# Fetch XML data
xml_data = fetch_xml_data(XML_URL)

# Streamlit app layout
st.title("Irish County Weather Forecast - Multiple Parsing Methods")

st.subheader("Method 1: xml.etree.ElementTree")
df1 = parse_with_elementtree(xml_data)
st.dataframe(df1)

st.subheader("Method 2: pandas read_xml")
df2 = parse_with_pandas(xml_data)
st.dataframe(df2)

st.subheader("Method 3: lxml")
df3 = parse_with_lxml(xml_data)
st.dataframe(df3)

st.subheader("Method 4: xmltodict")
df4 = parse_with_xmltodict(xml_data)
st.dataframe(df4)

st.subheader("Method 5: BeautifulSoup")
df5 = parse_with_beautifulsoup(xml_data)
st.dataframe(df5)
