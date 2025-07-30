import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image, ImageOps

# Load model
model = tf.keras.models.load_model("model.h5")

st.title("MNIST Digit Classifier")
st.write("Upload a 28x28 grayscale image of a handwritten digit.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("L")  # convert to grayscale
    image = ImageOps.invert(image)  # MNIST digits are white on black

    # Resize and preprocess
    image = image.resize((28, 28))
    img_array = np.array(image).astype("float32") / 255.0
    img_array = img_array.reshape(1, 28, 28, 1)

    # Show image
    st.image(image, caption="Uploaded Digit", width=150)

    # Predict
    pred = model.predict(img_array)
    predicted_class = np.argmax(pred)

    st.subheader(f"Predicted Digit: {predicted_class}")
