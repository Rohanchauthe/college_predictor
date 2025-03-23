import streamlit as st

st.title("📞 Contact Us")
st.write("Have any questions? Fill out the form below and we will get back to you.")

# Contact Form
name = st.text_input("Your Name")
email = st.text_input("Your Email")
message = st.text_area("Your Message")

if st.button("Submit"):
    if name and email and message:
        st.success(f"Thank you {name}, we have received your message and will respond to {email} soon!")
    else:
        st.warning("Please fill in all fields before submitting.")
