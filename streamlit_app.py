import streamlit as st
from xmltodict import parse
import requests
import pandas as pd

url = "https://www.met.ie/Open_Data/xml/county_forecast.xml"

data = requests.get(url).text

parsed_data = parse(data)

forecasts = parsed_data.get('forecast', {}).get('county', [])

df = pd.json_normalize(forecasts)

st.write("Weather Forecast Data")
st.dataframe(df)
