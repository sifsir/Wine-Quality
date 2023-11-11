
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

    # The last 10 data
    st.header("Data Description")
    st.table(df.describe())

    # Wine Types
    st.header("Wine Types")
    st.image("winetype.png", caption="Figure 1")
    st.caption(""" This is a visualisation of the ratio of the two types of wine (white and red).

    1. White wine: 74.5%
    2. Red wine: 25.5% """)

    # Wine pH by Type
    st.header("Wine pH by Type")
    st.image("winepH.png", caption="Figure 2")
    st.caption(""" This is a visualisation of a boxplot comparing the pH levels of two types of wine (white and red).

    1. White wine: 

    - Wider range of pH values than red wine
    - The distribution is more spread out (the lower and higher ends have several outliers)

    - The median pH values is around the center of the box

    2. Red wine:

    - Have more concentrated range of pH values

    - Only have few outliers

    - The median pH appears to be slightly lower than white wine.""")

    # Fixed Acidity
    st.header("Fixed Acidity")
    st.image("FixedAcidity.png", caption="Figure 3")
    st.caption(""" The histogram suggest:
    - The distribution of fixed acidity indicationg a normal-like distribution

    - The majority of wines have a fixed acidity between 6-8

    - The peak frequency occurs near a fixed acidity value of 7""")

    