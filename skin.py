import streamlit as st
import altair as alt
import pandas as pd

# Page Setup
st.set_page_config(
    page_title="Skincare",
    page_icon="🧴",
    layout="wide",
    initial_sidebar_state="expanded")
alt.themes.enable("dark")
# --------------

# Read files
dfbodymist = pd.read_csv('bodymistcompanies.csv', encoding='utf-8', sep=',')
dfbodymistglobal = pd.read_csv('bodymistglobalrevenue.csv', encoding='utf-8', sep=',')
# --------------

# Global
def globalcol0():
    st.title("Skincare")

def bodymistcol0():
    st.dataframe(dfbodymistglobal, hide_index=True)

def bodymistcol1():
    st.bar_chart(dfbodymistglobal, x='Year', y='Market Size (USD Billion)')
    st.caption("¹ Global Body Mist Market Report – Market.us. [Access here.](https://market.us/report/global-body-mist-market/)")

def bodymistcol2():
    st.dataframe(dfbodymist, hide_index=True)
    st.caption("¹ Global Body Mist Market Report – Market.us. [Access here.](https://market.us/report/global-body-mist-market/)")


st.title("Skincare Market")
tab1, tab2, tab3 = st.tabs(["Global Skincare", "Brazil", "Body Mist"])

with tab1:
    col = st.columns((1.5, 4.5, 2), gap='medium')
    with col[0]:
        globalcol0()

with tab3:
    col = st.columns((1.5, 4.5, 2), gap='medium')
    with col[0]:
        bodymistcol0()
    with col[1]:
        bodymistcol1()
    with col[2]:
        bodymistcol2()

