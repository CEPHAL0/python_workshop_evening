import streamlit as st
import joblib
import numpy as np
import matplotlib.pyplot as plt

model = joblib.load("iris_model.pkl")


st.title("Iris Flower Prediction App")
st.write("Enter flower measurements to predict the species")

# User Inputs
sepal_length = st.slider("Sepal Length", 4.0, 8.0)
sepal_width = st.slider("Sepal Width", 2.0, 4.5)
petal_length = st.slider("Petal Length", 1.0, 7.0)
petal_width = st.slider("Petal Width", 0.1, 2.5)

# Convert inputs to array
input_data  = np.array([[sepal_length, sepal_width, petal_length, petal_width]])


if st.button("Predict"):
    prediction = model.predict(input_data)
    class_names = ["Setosa", "Versicolor", "Virginica"]
    st.success(f"Predicted Species: {class_names[prediction[0]]}")

fig, ax = plt.subplots()
ax.bar(["Sepal L", "Sepal W", "Petal L", "Petal W"], input_data[0])
st.pyplot(fig)