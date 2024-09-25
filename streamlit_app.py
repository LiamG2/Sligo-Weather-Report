import streamlit as st
import gspread
from streamlit_lottie import st_lottie

x = ('https://raw.githubusercontent.com/LiamG2/Sligo-Weather-Report/refs/heads/main/file.json')  # PEP-8 Length N/A

# Set sidebar initial state
st.set_page_config(initial_sidebar_state="expanded")

# Method for adding widgets/lotties to sidebar
with st.sidebar:
    st_lottie(x, height=200, key='x_1')

with st.sidebar:
    st.write('"_Beep, Boop . . . A python-only web-scraping Bot created by CADNurd_"')

# Google API setup and GSheet access
try:
    gApiKey = gspread.service_account("path_to_service_account.json")  # Make sure this is the correct path to your service account
    public_sheet = gApiKey.open_by_url(
        'https://docs.google.com/spreadsheets/d/1pkysi4rP3zsl20GWUp_HFg3CRg44BXdaoJDI0fnqIHA/edit?usp=sharing')
except Exception as e:
    st.error(f"Error accessing the Google Sheet: {e}")
    st.stop()  # Stop execution if the sheet can't be accessed

# String conversion/cleaning function
def clean_gspread_output(data):
    data = str(data).strip("[]'").replace('\\n', '')
    return data

# Applies the function to the relevant data
def create_global_vars():
    global today_Date, today_Wthr, tonight_Wthr, tomorrow_Wthr
    try:
        today_Date = clean_gspread_output(public_sheet.sheet1.get('A4'))
        today_Wthr = clean_gspread_output(public_sheet.sheet1.get('A5'))
        tonight_Wthr = clean_gspread_output(public_sheet.sheet1.get('A8'))
        tomorrow_Wthr = clean_gspread_output(public_sheet.sheet1.get('A11'))
    except Exception as e:
        st.error(f"Error fetching data from the sheet: {e}")
        st.stop()  # Stop if fetching the data fails

create_global_vars()

# Final output to webpage/app
st.title("Sligo Weather Report")
st.write("##### _( Today's weather - for both Sligo and the rest of Connacht )_")
st.write(" ")
st.write(f"### {today_Date}")
st.write(today_Wthr)
st.write(" ")
st.write("### TONIGHT")
st.write(tonight_Wthr)
st.write(" ")
st.write("### TOMORROW")
st.write(tomorrow_Wthr)
