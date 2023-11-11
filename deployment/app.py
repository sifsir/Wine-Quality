"""
MILESTONE 2
Nama: Sifra Hilda Juliana Siregar
Batch: HCK-009
// app.py //
This programme was created for the model deployment as the main interface.
"""

import streamlit as st
import eda
import model


page = st.sidebar.selectbox(label='Select Page:', options=['Home Page', 'Exploration Data Analysis', 'Model Prediction'])

if page == 'Home Page':
    st.header('Hello Wine Lovers!') 
    st.write('')
    st.write('MILESTONE 2')
    st.write('Nama      : Sifra Siregar')
    st.write('Batch     : hck-009')
    st.write('Objectives    : Develop a machine learning framework that not only classifies wines into their respective white or red categories but also elucidates the influence of physicochemical properties on the quality of the wines, thereby providing educational insights for consumers.')
    st.write('')
    st.caption('Please choose the menu on the sidebar!')
    st.write('')
    st.write('')
    with st.expander("Background"):
        st.caption('The Wine Quality dataset is a collection of data that helps us understand what makes a good wine. It includes detailed info like how acidic or sweet wines are and how strong they are. This info is used to teach computers to predict good wines, which can make choosing wine easier and more fun for everyone.')
        st.image('redwhite.jpg', caption='(Fhg, 2022)')

    with st.expander("Problem Statement"):
            st.caption('Develop an intelligent platform that classifies wines into white or red categories, recommends wines based on customer preferences, and educates them about the key physicochemical factors influencing wine quality.')

    with st.expander("Conclusion"):
        st.caption('The data for this project is already in good shape, so all the machine learning models are having a good scores. But to improve them even more, they need fine-tuning, which is done through something called GridSearch for hyperparameter tuning. F1 scores is set as the main metric of evaluation because provides a balance between precision and recall. ')
elif page == 'Exploration Data Analysis':
    eda.run()
else:
    model.run()