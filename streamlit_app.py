import streamlit as st
import gspread
from streamlit_lottie import st_lottie
# import time

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


# link to test GSheet >> https://docs.google.com/spreadsheets/d/1pkysi4rP3zsl20GWUp_HFg3CRg44BXdaoJDI0fnqIHA/edit?usp=sharing

# Following instructions from >> https://docs.gspread.org/en/v6.1.2/oauth2.html#enable-api-access
#   Relevant project set-up on Google Developers Console >> https://console.cloud.google.com/apis/credentials?project=opportune-geode-435020-g8
#   Generated API Key from above project >> AIzaSyDpIvMkGb2WdHQC5xT1MHmefJZ7c3HRmlY

gApiKey = gspread.api_key("AIzaSyDpIvMkGb2WdHQC5xT1MHmefJZ7c3HRmlY")

public_sheet = gApiKey.open_by_url(
    'https://docs.google.com/spreadsheets/d/1pkysi4rP3zsl20GWUp_HFg3CRg44BXdaoJDI0fnqIHA/edit?usp=sharing')

# convert gspread output to plain string
today_Date = str((public_sheet.sheet1.get('A4')))
today_Wthr = str((public_sheet.sheet1.get('A5')))
tonight_Wthr = str((public_sheet.sheet1.get('A8')))
tomorrow_Wthr = str((public_sheet.sheet1.get('A11')))

# remove unnecessary chars [ ] ' from both string's ends
today_Wthr = today_Wthr.strip("[]'")
tonight_Wthr = tonight_Wthr.strip("[]'")
tomorrow_Wthr = tomorrow_Wthr.strip("[]'")

# remove substring '\n' from string - note the extra \ needed in \\n
# SEE >> https://stackoverflow.com/questions/42143302/how-can-i-remove-a-newline-character-in-a-string-in-python
today_Wthr = today_Wthr.replace('\\n', '')
tonight_Wthr = tonight_Wthr.replace('\\n', '')
tomorrow_Wthr = tomorrow_Wthr.replace('\\n', '')

st.title("Sligo Weather Report")
st.write("##### _Today's weather - for both Sligo and the rest of Connacht_")
st.write(" ")
st.write("### today_Date")
st.write(today_Wthr)
st.write(" ")
st.write("### Tonight")
st.write(tonight_Wthr)
st.write(" ")
st.write("### Tomorrow")
st.write(tomorrow_Wthr)

