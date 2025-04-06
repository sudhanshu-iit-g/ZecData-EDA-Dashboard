# utils/loader.py

import pandas as pd
import streamlit as st

@st.cache_data
def load_data(file):
    try:
        return pd.read_csv(file, encoding='utf-8')
    except:
        return pd.read_csv(file, encoding='ISO-8859-1')
