import streamlit as st
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
import joblib

# Load the trained model
model = joblib.load('Trained model.sav')

# Define the dataset or create a form to allow the user to input data
st.write('Enter the water quality parameters:')
ph = st.number_input('pH')
hardness = st.number_input('Hardness')
solids = st.number_input('Solids')
chloramines = st.number_input('Chloramines')
sulfate = st.number_input('Sulfate')
conductivity = st.number_input('Conductivity')
organic_carbon = st.number_input('Organic Carbon')
trihalomethanes = st.number_input('Trihalomethanes')
turbidity = st.number_input('Turbidity')

# Create a button to generate the prediction
if st.button('Generate prediction'):
    # Create a Pandas DataFrame with the input data
    data = pd.DataFrame({
        'ph': [ph],
        'Hardness': [hardness],
        'Solids': [solids],
        'Chloramines': [chloramines],
        'Sulfate': [sulfate],
        'Conductivity': [conductivity],
        'Organic_carbon': [organic_carbon],
        'Trihalomethanes': [trihalomethanes],
        'Turbidity': [turbidity]
    })

    # Use the trained model to make predictions on the input data
    prediction = model.predict(data)

    # Display the prediction to the user
    if prediction == 0:
        st.write('The water is not potable')
    else: 
        st.write('The water is potable')
