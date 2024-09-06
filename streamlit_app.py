import streamlit as st
from xmltodict import parse
import requests

url = "https://www.met.ie/Open_Data/xml/county_forecast.xml"

data = requests.get(url).text

parsed_data = parse(data)

st.write(parsed_data)
