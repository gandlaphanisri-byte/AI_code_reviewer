import streamlit as st
from utils import header
from code_reviewer import review_code

# Page Configuration
st.set_page_config(
    page_title="AI Code Reviewer",
    page_icon="💻",
    layout="wide"
)

# Display Header
header()

# User Inputs
language = st.selectbox(
    "Programming Language",
    ["Python", "Java", "JavaScript", "C", "C++", "SQL"]
)

review_type = st.radio(
    "Review Type",
    ["Basic", "Detailed", "Security"]
)

temperature = st.slider(
    "Temperature",
    min_value=0.0,
    max_value=1.0,
    value=0.2,
    step=0.1
)

code = st.text_area(
    "Paste Your Code",
    height=300,
    placeholder="Paste your source code here..."
)

# Review Button
if st.button("Review Code", use_container_width=True):

    if not code.strip():
        st.warning("⚠ Please paste some code.")
    else:
        with st.spinner("🔍 Reviewing your code..."):
            result = review_code(
                language,
                review_type,
                code,
                temperature
            )

        st.success("✅ Review Completed")
        st.markdown(result)