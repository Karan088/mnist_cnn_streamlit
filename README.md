# MNIST Digit Classifier with CNN & Streamlit

This project uses a Convolutional Neural Network (CNN) to classify handwritten digits (0–9) from the MNIST dataset.  
It includes a Streamlit app that lets users upload their own digit image and get instant predictions.

---

## Results

- Achieved **~99% validation accuracy**
- Performs well on unseen test images
- Live prediction demo available via Streamlit app

---
## Folder Structure
```
mnist_cnn_streamlit/
├── app.py                                 ← Streamlit code
├── model.h5                               ← Model to classify the image
├── digit-image-classification.ipynb       ← Python Notebook with methodlogy
└── requirements.txt                       ← packages needed to run the app
```
---
## How to Use the App

1. Download the project folder inlcluding trained model (`model.h5`) & python script (`app.py`)
2. In terminal, run:
```streamlit run app.py```


