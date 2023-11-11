"""
MILESTONE 2
Nama: Sifra Hilda Juliana Siregar
Batch: HCK-009
// model.py //
This programme was created for model prediction.
"""
import streamlit as st
import pandas as pd
import joblib

# Function to run in app.py
def run():
    st.title("Find your wine type!")
   
   
    # User input for prediction
    fixed_acidity = st.number_input("Fixed Acidity", min_value=0.0)
    volatile_acidity = st.number_input("Volatile Acidity", min_value=0.0)
    citric_acid = st.number_input("Citric Acid", min_value=0.0)
    residual_sugar = st.number_input("Residual Sugar", min_value=0.0)
    chlorides = st.number_input("Chlorides", min_value=0.0)
    free_sulfur_dioxide = st.number_input("Free Sulfur Dioxide", min_value=0.0)
    total_sulfur_dioxide = st.number_input("Total Sulfur Dioxide", min_value=0.0)
    density = st.number_input("Density", min_value=0.0)
    pH = st.slider("pH", min_value = 0.00, max_value=14.00, step=0.01)
    sulphates = st.number_input("Sulphates", min_value=0.0)
    alcohol = st.number_input("Alcohol", min_value=0.0)
    quality = st.number_input("Quality", min_value=0, max_value=10)

    data_prediction = pd.DataFrame({
        'fixed_acidity': [fixed_acidity],  
        'volatile_acidity': [volatile_acidity], 
        'citric_acid': [citric_acid], 
        'residual_sugar': [residual_sugar],  
        'chlorides': [chlorides], 
        'free_sulfur_dioxide': [free_sulfur_dioxide], 
        'total_sulfur_dioxide': [total_sulfur_dioxide],
        'density': [density],
        'pH': [pH],
        'sulphates': [sulphates],
        'alcohol': [alcohol],
        'quality': [quality],
    })

    
    st.header("This is your wine characteristics!")
    st.table(data_prediction)

    # Initating the prediction
    if st.button(label="Predict"):
        model = joblib.load("best_model.joblib")
        pred = model.predict(data_prediction)
        if pred == 0:
            st.write("Red Wine")
        else:
            st.write("White Wine")

    
    