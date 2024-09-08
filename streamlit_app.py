# initial source >>> https://github.com/streamlit/gsheets-connection

#   example search for first result only...
# https://www.google.com/search?q=stack+overflow&num=1&start=1
#   then second result only...
# https://www.google.com/search?q=stack+overflow&num=1&start=2

import streamlit as st
from streamlit_gsheets import GSheetsConnection

# number seconds to pause before data refresh
# set to 10 during testing and 300 (5mins) at all other times
pause = 300

url_1 = "https://docs.google.com/spreadsheets/d/1pkysi4rP3zsl20GWUp_HFg3CRg44BXdaoJDI0fnqIHA/edit?usp=sharing"
url_2 = "https://docs.google.com/spreadsheets/d/1f7NJT3M5ANzR0TbiHawhuUCGYSo3MC7HtzoRPq6tV00/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetsConnection)

data_1 = conn.read(spreadsheet=url_1, ttl=pause, usecols=[0])
data_2 = conn.read(spreadsheet=url_2, ttl=pause, usecols=[0])
st.table(data_1)
st.table(data_2)
