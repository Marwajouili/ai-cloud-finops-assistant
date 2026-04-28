import pandas as pd

df = pd.read_csv("data/cloud_costs.csv")

def search_costs(query):
    query = query.lower()

    if "ec2" in query:
        return df[df["service"] == "EC2"]

    if "s3" in query:
        return df[df["service"] == "S3"]

    if "rds" in query:
        return df[df["service"] == "RDS"]

    return df

def rag_answer(question):
    data = search_costs(question)

    total = data["cost"].sum()

    return f"""
🧠 RAG AI Response:

Query: {question}

💰 Relevant cost: {total}

📊 Insight:
Based on your cloud usage, this service is a key cost driver.
"""