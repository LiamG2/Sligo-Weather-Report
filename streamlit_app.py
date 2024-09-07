import streamlit as st
import requests
import pandas as pd

# Fetch the JSON data from the URL
url = "https://www.met.ie/Open_Data/json/Connacht.json"
response = requests.get(url)
data = response.json()

# Convert the JSON data to a DataFrame
df = pd.json_normalize(data['connacht'])

# Display the DataFrame in a tabulated format
st.write("Connacht Weather Forecast Data")
st.dataframe(df)
