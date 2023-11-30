
"""
MILESTONE 2
Nama: Sifra Hilda Juliana Siregar
Batch: HCK-009
// eda.py //
This programme was created for EDA deployment.
"""
import streamlit as st
import pandas as pd

# Function to run in app.py
def run():
    st.title("Explatoratory Data Analysis")

    df = pd.read_csv("winequalityN.csv")

    # The first 10 data
    st.header("The First 10 Entry Data")
    st.table(df.head(10))

   
    # Fixed Acidity
    st.header("Fixed Acidity")
    st.image("FixedAcidity.png", caption="Figure 3")
    st.caption(""" The histogram suggest:
    - The distribution of fixed acidity indicationg a normal-like distribution

    - The majority of wines have a fixed acidity between 6-8

    - The peak frequency occurs near a fixed acidity value of 7""")

    