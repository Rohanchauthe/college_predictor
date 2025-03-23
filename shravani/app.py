import streamlit as st

st.set_page_config(
    page_title="College Admission Predictor 🎓",
    page_icon="🎓",
    layout="wide"
)

st.sidebar.title("Navigation")
st.sidebar.success("Select a page above.")
st.title("Welcome to College Admission Predictor 🎓")
st.write("""
This application helps students find eligible colleges based on their exam scores.
Use the **College Finder** to check eligible colleges or go to **Contact Us** for inquiries.

### Created by:  
👉 **[Your Name]**  
📧 **your.email@example.com**  
📍 **Your Location**
""")
