import streamlit as st
import requests
import pandas as pd
import json

# Fetch the JSON data from the URL
url = "https://www.met.ie/Open_Data/json/Connacht.json"
response = requests.get(url)
data = response.json()

# Extract relevant data from the parsed JSON
# Adjust this extraction based on your JSON structure
forecasts = data.get('forecast', [])

# Convert the extracted data into a DataFrame
df = pd.json_normalize(forecasts)

# Display the DataFrame in a tabulated format
st.write("Weather Forecast Data")
st.dataframe(df)
