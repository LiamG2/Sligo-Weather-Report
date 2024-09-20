import streamlit as st
import gspread
# import time

# set sidebar initial state + dummy placeholder content
st.set_page_config(
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)


# link to test GSheet >> https://docs.google.com/spreadsheets/d/1pkysi4rP3zsl20GWUp_HFg3CRg44BXdaoJDI0fnqIHA/edit?usp=sharing

# Following instructions from >> https://docs.gspread.org/en/v6.1.2/oauth2.html#enable-api-access
#   Relevant project set-up on Google Developers Console >> https://console.cloud.google.com/apis/credentials?project=opportune-geode-435020-g8
#   Generated API Key from above project >> AIzaSyDpIvMkGb2WdHQC5xT1MHmefJZ7c3HRmlY

gApiKey = gspread.api_key("AIzaSyDpIvMkGb2WdHQC5xT1MHmefJZ7c3HRmlY")

public_sheet = gApiKey.open_by_url(
    'https://docs.google.com/spreadsheets/d/1pkysi4rP3zsl20GWUp_HFg3CRg44BXdaoJDI0fnqIHA/edit?usp=sharing')

# convert gspread output to plain string
cellContents = str((public_sheet.sheet1.get('A5')))

# remove unnecessary chars [ ] ' from both string's ends
cellContents = cellContents.strip("[]'")

# remove substring '\n' from string - note the extra \ needed in \\n
# SEE >> https://stackoverflow.com/questions/42143302/how-can-i-remove-a-newline-character-in-a-string-in-python
cellContents = cellContents.replace('\\n', '')

st.title("Web App Title")

st.write(cellContents)
