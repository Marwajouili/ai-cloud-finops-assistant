from fastapi import FastAPI
from rag.advanced_rag import rag_answer

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FinOps AI API is running 🚀"}

@app.get("/ask")
def ask(question: str):
    try:
        response = rag_answer(question)
        return {"question": question, "answer": response}
    except Exception as e:
        return {"error": str(e)}