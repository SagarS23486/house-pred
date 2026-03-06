import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# load dataset
data = pd.read_csv("Housing.csv")

# features and target
X = data[['area','bedrooms','bathrooms','stories','parking']]
y = data['price']

# split dataset
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# train model
model = LinearRegression()
model.fit(X_train,y_train)

st.title("🏠 House Price Prediction")

st.write("Enter house details to predict price")

# user inputs
area = st.number_input("Area")
bedrooms = st.number_input("Bedrooms")
bathrooms = st.number_input("Bathrooms")
stories = st.number_input("Stories")
parking = st.number_input("Parking")

if st.button("Predict Price"):
    
    input_data = [[area,bedrooms,bathrooms,stories,parking]]
    prediction = model.predict(input_data)
    
    st.success(f"Predicted House Price: ₹{prediction[0]:,.2f}")