import streamlit as st
import gspread
from streamlit_lottie import st_lottie

# Ignoring PEP 8, 80 char line limit for both comments and URLs

x = ('https://raw.githubusercontent.com/LiamG2/Sligo-Weather-Report/refs/heads/main/file.json')

# set sidebar initial state
st.set_page_config(
    initial_sidebar_state="expanded"
)

# method for adding widgets/lotties to sidebar
with st.sidebar:
    st_lottie(x, height=200, key='x_1')
    # note different 'key' name above, needed when using same animation multiple times

with st.sidebar:
    st.write('"_Beep, Boop . . . A python-only web-scraping bot created by CADNurd_"')


# link to test GSheet >> https://docs.google.com/spreadsheets/d/1pkysi4rP3zsl20GWUp_HFg3CRg44BXdaoJDI0fnqIHA/edit?usp=sharing

# Following instructions from >> https://docs.gspread.org/en/v6.1.2/oauth2.html#enable-api-access
#   Relevant project set-up on Google Developers Console >> https://console.cloud.google.com/apis/credentials?project=opportune-geode-435020-g8
#   Generated API Key from above project >> AIzaSyDpIvMkGb2WdHQC5xT1MHmefJZ7c3HRmlY


gApiKey = gspread.api_key("AIzaSyDpIvMkGb2WdHQC5xT1MHmefJZ7c3HRmlY")

public_sheet = gApiKey.open_by_url(
    'https://docs.google.com/spreadsheets/d/1pkysi4rP3zsl20GWUp_HFg3CRg44BXdaoJDI0fnqIHA/edit?usp=sharing')

# String conversion/cleaning function
#     convert gspread output to plain string
#     remove unnecessary chars [ ] ' from both string's ends
#     remove substring '\n' from string - note the extra \ needed in \\n
#         SEE >> https://stackoverflow.com/questions/42143302/how-can-i-remove-a-newline-character-in-a-string-in-python
def clean_gspread_output(data):
    data = str(data).strip("['").replace('\\n', '')
    return data

# Applies the function to the relevant data
today_Date = clean_gspread_output(public_sheet.sheet1.get('A4'))
tomorrow_Date = clean_gspread_output(public_sheet.sheet1.get('A10'))
today_Wthr = clean_gspread_output(public_sheet.sheet1.get('A5'))
tonight_Wthr = clean_gspread_output(public_sheet.sheet1.get('A8'))
tomorrow_Wthr = clean_gspread_output(public_sheet.sheet1.get('A11'))

# Output to webpage/app
st.title("Sligo Weather Report")
st.write("_Today's weather - for both Sligo and the rest of Connacht_")
st.write(" ")
st.write(f"### {today_Date}")
st.write(today_Wthr)
st.write(" ")
st.write("### TONIGHT")
st.write(tonight_Wthr)
st.write(" ")
st.write(f"### {tomorrow_Date}")
# st.write("### TOMORROW")
st.write(tomorrow_Wthr)
