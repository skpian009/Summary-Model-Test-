# app.py
import streamlit as st
from transformers import pipeline

# Load the summarization pipeline with the specified model
pipe = pipeline("summarization", model="Falconsai/medical_summarization")

# Set the title of the app
st.title("Medical Text Summarization")

# Create a text area for user input
input_text = st.text_area("Enter the medical text you want to summarize:", height=200)

# Create a button to trigger the summarization
if st.button("Summarize"):
    if input_text:
        # Generate the summary
        summary = pipe(input_text, max_length=150, min_length=30, do_sample=False)
        
        # Display the summarized text
        st.subheader("Summary:")
        st.write(summary[0]['summary_text'])
    else:
        st.error("Please enter some text to summarize.")
