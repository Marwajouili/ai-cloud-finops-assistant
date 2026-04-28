import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss

df = pd.read_csv("data/cloud_costs.csv")

# Transformer modèle (gratuit)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Créer texte pour chaque ligne
texts = df.apply(lambda row: f"{row['service']} cost {row['cost']} in {row['month']}", axis=1)

# Embeddings
embeddings = model.encode(texts.tolist())

# FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

def search(query):
    query_vec = model.encode([query])

    _, idx = index.search(np.array(query_vec), k=3)

    results = df.iloc[idx[0]]

    return results

def rag_answer(query):
    results = search(query)

    total = results["cost"].sum()

    return f"""
🧠 ADVANCED RAG RESPONSE:

Query: {query}

💰 Estimated cost: {total}

📊 Services involved:
{results.to_string(index=False)}

👉 Insight:
These services contribute to your cloud spending pattern.
"""