import pandas as pd  # pip install pandas openpyxl
import streamlit as st  # pip install streamlit
from os import getcwd
print(getcwd())

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")

# ---- READ EXCEL ----
@st.cache
def get_data_from_excel():
    df = pd.read_excel(
        io="Leaderboard.xlsx",
        engine="openpyxl",
        sheet_name="Sheet1",
        skiprows=1,
        usecols="B:F",
        nrows=1000,
    )
    return df

df = get_data_from_excel()
st.write(df)

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)