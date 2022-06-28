import streamlit as st
import pandas as pd


@st.cache
def get_data(name_of_csv):
    return pd.read_csv(f"{name_of_csv}.csv") #use different data here maybe

df = get_data()