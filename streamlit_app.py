# example/st_app.py
# source >>> https://github.com/streamlit/gsheets-connection

import streamlit as st
from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/1pkysi4rP3zsl20GWUp_HFg3CRg44BXdaoJDI0fnqIHA/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url, usecols=[0, 1])
st.dataframe(data, width=300)
