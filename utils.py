import streamlit as st

def header():
    st.title("💻 AI Code Reviewer")
    st.caption("Review your code using Gemini AI, LangChain, and Streamlit.")

    st.markdown(
        """
        Welcome! 👋

        Paste your code, choose the programming language and review type,
        then click **Review Code** to receive AI-powered feedback on:
        - ✅ Syntax Errors
        - ✅ Logic Errors
        - ✅ Performance Improvements
        - ✅ Security Issues
        - ✅ Best Practices
        - ✅ Optimized Code
        """
    )