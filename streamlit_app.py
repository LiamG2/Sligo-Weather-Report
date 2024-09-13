# initial source >>> https://github.com/streamlit/gsheets-connection

import streamlit as st
from streamlit_gsheets import GSheetsConnection


# number seconds to pause before spreadsheet data refresh
# set to 10 during testing and 600 (10mins) at all other times
pause = 600

url_1 = "https://docs.google.com/spreadsheets/d/1pkysi4rP3zsl20GWUp_HFg3CRg44BXdaoJDI0fnqIHA/edit?usp=sharing"
url_2 = "https://docs.google.com/spreadsheets/d/1f7NJT3M5ANzR0TbiHawhuUCGYSo3MC7HtzoRPq6tV00/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetsConnection)

data_1 = conn.read(spreadsheet=url_1, ttl=pause, usecols=[0])
data_2 = conn.read(spreadsheet=url_2, ttl=pause, usecols=[0])
st.header("Connaught")
st.table(data_1)
st.header("Ulster")
st.table(data_2)
st.write(data_1)
