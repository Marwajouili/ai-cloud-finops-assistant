import pandas as pd

df = pd.read_csv("data/cloud_costs.csv")

def total_cost():
    return df.groupby("service")["cost"].sum()

def explain_costs():
    totals = total_cost()

    most_expensive = totals.idxmax()
    value = totals.max()

    return f"""
💰 Cloud Cost Analysis:

- Most expensive service: {most_expensive}
- Cost: {value}

Recommendation:
👉 Optimize {most_expensive} usage to reduce costs.
"""

def ask_question(question):
    question = question.lower()

    if "most" in question or "expensive" in question:
        return explain_costs()

    if "total" in question:
        return str(total_cost())

    return "❌ I can only answer cost-related questions for now."