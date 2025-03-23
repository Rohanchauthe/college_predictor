import streamlit as st
import pandas as pd

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("college_cutoff_data.csv")  # Replace with your actual file

df = load_data()

st.title("College Admission Predictor 🎓")
st.write("Enter your details to check eligible colleges based on previous cutoff data.")

# User Inputs
exam_type = st.selectbox("Select Exam Type", df['score_type'].unique())
seat_type = st.selectbox("Select Seat Type", df['seat_type'].unique())
branch = st.selectbox("Select Preferred Branch", df['branch'].unique())
student_score = st.number_input("Enter Your Score/Percentile", min_value=0.0, max_value=100.0, step=0.1)

# College Search Filter
search_college = st.text_input("Search College Name (Optional)")

# Filter dataset
filtered_df = df[
    (df['score_type'] == exam_type) &
    (df['seat_type'] == seat_type) &
    (df['branch'] == branch) &
    (df['min'] <= student_score) 
]

# Apply search filter
if search_college:
    filtered_df = filtered_df[filtered_df['college_name'].str.contains(search_college, case=False, na=False)]

# Display Results
st.subheader("Eligible Colleges")
if not filtered_df.empty:
    st.dataframe(filtered_df[['college_name', 'branch', 'score_type', 'seat_type', 'min']])
    
    # Download Option
    csv = filtered_df.to_csv(index=False).encode("utf-8")
    st.download_button(label="Download Results as CSV", data=csv, file_name="eligible_colleges.csv", mime="text/csv")
else:
    st.warning("No eligible colleges found based on your score and preferences.")
