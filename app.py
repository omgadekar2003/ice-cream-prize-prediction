# import streamlit as st
# import joblib
# import numpy as np

# # Load the trained model
# model = joblib.load('Poly_linear_regression.pkl')

# # Title of the Streamlit app
# st.title("Ice Cream Price Prediction App")

# # Description
# st.write("""
# This app predicts the price of ice cream based on the temperature.
# Enter a temperature value (positive or negative), and the app will predict the price of the ice cream.
# """)

# # Input field for temperature
# temperature = st.number_input("Enter Temperature (°C):", value=0.0, step=0.1)

# # Predict button
# if st.button("Predict Price"):
#     try:
#         # Make prediction
#         prediction = model.predict(np.array([[temperature]]))
#         st.success(f"Predicted Ice Cream Price: ${prediction[0]:,.2f}")
#     except Exception as e:
#         st.error(f"Error: {e}")


import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('Poly_linear_regression.pkl')

# Title of the Streamlit app
st.title("Ice Cream Sales Prediction App")

# Description
st.write("""
This app predicts the sales of ice cream (in units) based on the temperature.
Enter a temperature value (positive or negative), and the app will predict the number of ice cream units likely to be sold.
""")

# Input field for temperature
temperature = st.number_input("Enter Temperature (°C):", value=0.0, step=0.1)

# Predict button
if st.button("Predict Sales"):
    try:
        # Make prediction
        prediction = model.predict(np.array([[temperature]]))
        st.success(f"Predicted Ice Cream Sales: {prediction[0]:,.2f} units")
    except Exception as e:
        st.error(f"Error: {e}")

