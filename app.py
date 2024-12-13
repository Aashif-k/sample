# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MidMg0rjwBnV_3SSbwQon7KXi1JNuWWP
"""

import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load the trained model
RFC = joblib.load('churn_model.pkl')  # Ensure the file is in the same directory
# creating an list for state value
place=['IL','AL','AK','TX','DE','VA','CT','NM','OR','VT','HI','SC','IN','IA','NE','LA','KS','DC','KY','NH','GA','ME','WI','UT','MA','MS','RI','MN','ND','CO','WY','NJ','NC','WA','NV','OH','OK','AR','PA','WV','FL','CA','TN','ID','MI','NY','MT','SD','MD','MO','AZ']
# Set up the Streamlit app
st.title("Customer Churn Prediction")
st.write("This application predicts whether a customer will churn based on their features.")

# Input features for prediction
st.header("Customer Details")
page_bg_img = '''
<style>
body {
background-image: url(photo-1542281286-9e0a16bb7366);
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)
inp=st.sidebar.selectbox("select state",options=place)
for inp in place:
    state=place.index(inp)
ac=st.sidebar.selectbox("area code",options=['415','408','510'])
if ac==415:
    area_code=1
elif ac==408:
    area_code=2
else:
    area_code=0
account_length = st.sidebar.number_input("Account Length (in days)", min_value=0, max_value=500, value=100)
Text=st.sidebar.selectbox("voice.plan",options=['Yes','No'])
if Text =='Yes':
    voice_plan=1
else:
    voice_plan=0
voice_messages = st.sidebar.number_input("Number of Voice Messages", min_value=0, max_value=50, value=10)
intp=st.sidebar.selectbox("intl.plan",options=['Yes','No'])
if intp == 'Yes':
    intl_plan=1
else:
    intl_plan=0
intl_mins = st.sidebar.number_input("International Minutes", min_value=0.0, max_value=100.0, value=10.0)
intl_calls = st.sidebar.number_input("International Calls", min_value=0, max_value=20, value=5)
intl_charge = st.sidebar.number_input("International Charges", min_value=0.0, max_value=50.0, value=5.0)
day_mins = st.sidebar.number_input("Day Minutes", min_value=0.0, max_value=500.0, value=100.0)
day_calls = st.sidebar.number_input("Day Calls", min_value=0, max_value=200, value=50)
day_charge = st.sidebar.number_input("Day Charge", min_value=0.0, max_value=100.0, value=10.0)
eve_mins = st.sidebar.number_input("Evening Minutes", min_value=0.0, max_value=500.0, value=100.0)
eve_calls = st.sidebar.number_input("Evening Calls", min_value=0, max_value=200, value=50)
eve_charge = st.sidebar.number_input("Evening Charge", min_value=0.0, max_value=100.0, value=10.0)
night_mins = st.sidebar.number_input("Night Minutes", min_value=0.0, max_value=500.0, value=100.0)
night_calls = st.sidebar.number_input("Night Calls", min_value=0, max_value=200, value=50)
night_charge = st.sidebar.number_input("Night Charge", min_value=0.0, max_value=100.0, value=10.0)
customer_calls = st.sidebar.number_input("Number of Customer Service Calls", min_value=0, max_value=20, value=1)

# Prediction button
if st.sidebar.button("Predict Churn"):
    # Prepare the input array
    input_data = np.array([state,area_code,
        account_length,voice_plan, voice_messages,intl_plan, intl_mins, intl_calls, intl_charge,
        day_mins, day_calls, day_charge, eve_mins, eve_calls, eve_charge,
        night_mins, night_calls, night_charge, customer_calls
    ]).reshape(1, -1)

    # Make the prediction
    prediction = RFC.predict(input_data)
    prediction_prob = RFC.predict_proba(input_data)[0][1]  # Probability of churn

    # Display the result
    if prediction[0] == 1:
        st.error(f"Prediction: The customer is likely to churn. (Probability: {prediction_prob:.2f})")
    else:
        st.success(f"Prediction: The customer is likely to stay. (Probability: {1 - prediction_prob:.2f})")
