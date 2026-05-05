import streamlit as st
import requests

st.title("💰 AI FinOps Assistant")

question = st.text_input("Ask your cloud cost question")

if st.button("Ask AI"):
    try:
        response = requests.get(
            "http://backend:8000/ask",
            params={"question": question}
        )

        if response.status_code == 200:
            st.write(response.json()["answer"])
        else:
            st.error("Error from backend API")

    except Exception as e:
        st.error(f"Connection error: {e}")