import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image


model = tf.keras.models.load_model("mnist_model.h5")

st.title("Handwritten Digit Detection")
st.write("Upload a 28x28 grayscale image of a digit (0-9)")

uploaded_file = st.file_uploader("Upload Image", type=["png", "jpeg", "jpg"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("L")
    image = image.resize((28, 28))

    st.image(image, caption="Uploaded Image", width=150)

    # Pre Processing
    img_array = np.array(image)/255.0
    img_array = img_array.reshape(1, 28, 28, 1)

    # predict
    prediction = model.predict(img_array)
    predicted_class = np.argmax(prediction)

    st.success(f"Predicted Digit: **{predicted_class}**")
