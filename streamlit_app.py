import streamlit as st
import pandas as pd

st.text("# 🤹 CADNurd's First Web App")
st.write("# 🤹 CADNurd's First Web App")
st.write("I have absolutely no idea what I'm doing . . . but what's the worst that could happen?")

# Title of the app
st.markdown("### Sample App Template")

# Display a dataframe
df = pd.DataFrame({
    'Column A': [1, 2, 3, 4],
    'Column B': ['A', 'B', 'C', 'D']
})
st.write("Here's a simple DataFrame:")
st.dataframe(df)

# Slider example
value = st.slider("Select a value", 0, 100, 25)
st.write("Selected value:", value)

HORIZONTAL_RED = "images/horizontal_red.png"
ICON_RED = "images/icon_red.png"
HORIZONTAL_BLUE = "images/horizontal_blue.png"
ICON_BLUE = "images/icon_blue.png"