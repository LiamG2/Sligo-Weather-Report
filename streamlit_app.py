# initial source >>> https://github.com/streamlit/gsheets-connection

#   example search for first result only...
# https://www.google.com/search?q=stack+overflow&num=1&start=1
#   then second result only...
# https://www.google.com/search?q=stack+overflow&num=1&start=2

import streamlit as st
from streamlit_gsheets import GSheetsConnection


url = "https://docs.google.com/spreadsheets/d/1pkysi4rP3zsl20GWUp_HFg3CRg44BXdaoJDI0fnqIHA/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url, ttl=10, usecols=[0])
st.table(data) # , width=300, height=500)
