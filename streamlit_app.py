import streamlit as st
import gspread
from streamlit_lottie import st_lottie

x = ('https://raw.githubusercontent.com/LiamG2/Sligo-Weather-Report/refs/heads/main/file.json') # PEP-8 Length N/A

# set sidebar initial state
st.set_page_config(
    initial_sidebar_state="expanded"
)

# method for adding widgets/lotties to sidebar
with st.sidebar:
    st_lottie(x, height=200, key='x_1')
    # note different 'key' name above, needed when using same animation
    # \multiple times

with st.sidebar:
    st.write('"_Beep, Boop . . . A python-only web-scraping Bot created by CADNurd_"')

# link to test GSheet >> https://docs.google.com/spreadsheets/d/1pkysi4rP3zsl20GWUp_HFg3CRg44BXdaoJDI0fnqIHA/edit?usp=sharing

# Following instructions from >> https://docs.gspread.org/en/v6.1.2/oauth2.html#enable-api-access
#   Relevant project set-up on Google Developers Console >> https://console.cloud.google.com/apis/credentials?project=opportune-geode-435020-g8
#   Generated API Key from above project >> AIzaSyDpIvMkGb2WdHQC5xT1MHmefJZ7c3HRmlY

# gApiKey = gspread.api_key("AIzaSyDpIvMkGb2WdHQC5xT1MHmefJZ7c3HRmlY")

# public_sheet = gApiKey.open_by_url(
#     'https://docs.google.com/spreadsheets/d/1pkysi4rP3zsl20GWUp_HFg3CRg44BXdaoJDI0fnqIHA/edit?usp=sharing')

# String conversion/cleaning function, which combines...
# # convert gspread output to plain string
# # remove unnecessary chars [ ] ' from both string's ends
# # remove newline \n chars - note double \\ needed - SEE >> https://stackoverflow.com/questions/42143302/how-can-i-remove-a-newline-character-in-a-string-in-python
def clean_gspread_output(data):
    data = str(data).strip("[]'").replace('\\n', '')
    return data

# Function to fetch data from Google Sheets and cache it
@st.cache_resource(ttl=3600)  # Cache the data for 1 hour (ttl in seconds)
def fetch_weather_part_1():
    gApiKey = gspread.service_account("path_to_service_account.json")  # Use your service account path
    public_sheet = gApiKey.open_by_url(
        'https://docs.google.com/spreadsheets/d/1pkysi4rP3zsl20GWUp_HFg3CRg44BXdaoJDI0fnqIHA/edit?usp=sharing')

@st.cache_resource(ttl=3600)  # Cache the data for 1 hour (ttl in seconds)
def fetch_weather_part_2():
    # Fetch the data from the sheet
    today_Date = clean_gspread_output(public_sheet.sheet1.get('A4'))
    today_Wthr = clean_gspread_output(public_sheet.sheet1.get('A5'))
    tonight_Wthr = clean_gspread_output(public_sheet.sheet1.get('A8'))
    tomorrow_Wthr = clean_gspread_output(public_sheet.sheet1.get('A11'))

    return today_Date, today_Wthr, tonight_Wthr, tomorrow_Wthr

# Fetch the weather data (this will be cached)
fetch_weather_part_1()
today_Date, today_Wthr, tonight_Wthr, tomorrow_Wthr = fetch_weather_part_2()

# Final output to webpage/app
st.title("Sligo Weather Report")
st.write("##### _( Today's weather - for both Sligo and the rest of Connacht )_")
st.write(" ")
# st.write("### + today_Date")
st.write(f"### {today_Date}")
st.write(today_Wthr)
st.write(" ")
st.write("### TONIGHT")
st.write(tonight_Wthr)
st.write(" ")
st.write("### TOMORROW")
st.write(tomorrow_Wthr)
