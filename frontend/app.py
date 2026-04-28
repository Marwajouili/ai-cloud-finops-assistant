import streamlit as st
import requests

st.title("💰 AI FinOps Assistant")

question = st.text_input("Ask your cloud cost question")

if st.button("Ask AI"):
    response = requests.get(
        "http://127.0.0.1:8000/ask",
        params={"question": question}
    )
    st.write(response.json()["answer"])