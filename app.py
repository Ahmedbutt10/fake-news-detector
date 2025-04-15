# -*- coding: utf-8 -*-
"""app

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bey_2AIn7CHSO0WWQHwqZJRQSzH_zK7X
"""

import streamlit as st
import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification

# Load model and tokenizer
@st.cache(allow_output_mutation=True)
def load_model():
    model = DistilBertForSequenceClassification.from_pretrained("Ahmedbutt10/fake-news-model")
    tokenizer = DistilBertTokenizer.from_pretrained("Ahmedbutt10/fake-news-model")
    model.eval()
    return model, tokenizer

model, tokenizer = load_model()

def predict(text):
    inputs = tokenizer(
        text,
        return_tensors='pt',
        truncation=True,
        padding='max_length',
        max_length=512
    )
    with torch.no_grad():
        outputs = model(**inputs)
        prediction = torch.argmax(outputs.logits, dim=1).item()
    return "REAL News" if prediction == 1 else "FAKE News"

# Streamlit UI
st.title("📰 Fake News Detector")
st.write("Paste a news article below and find out if it's real or fake!")

user_input = st.text_area("Enter News Article Here:")

if st.button("Predict"):
    if user_input.strip():
        result = predict(user_input)
        st.success(f"Prediction: **{result}**")
    else:
        st.warning("Please enter some text!")