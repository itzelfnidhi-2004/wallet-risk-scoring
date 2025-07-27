import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the scored wallet data
df = pd.read_csv("scored_wallets.csv")

# Categorize wallets by risk
def categorize_risk(score):
    if score >= 750:
        return 'Low Risk'
    elif score >= 500:
        return 'Medium Risk'
    else:
        return 'High Risk'

df['risk_category'] = df['credit_score'].apply(categorize_risk)

# -------- 1. Top 10 Credit Scores (Bar Plot) --------
top10 = df.sort_values(by="credit_score", ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(data=top10, x="credit_score", y="wallet_address", palette="viridis")
plt.title("Top 10 Wallets by Credit Score")
plt.xlabel("Credit Score")
plt.ylabel("Wallet Address")
plt.tight_layout()
plt.savefig("top10_wallets.png")
plt.close()

# -------- 2. Credit Score Distribution (Histogram) --------
plt.figure(figsize=(10, 6))
sns.histplot(df['credit_score'], bins=10, kde=True, color="skyblue")
plt.title("Credit Score Distribution")
plt.xlabel("Credit Score")
plt.ylabel("Number of Wallets")
plt.tight_layout()
plt.savefig("score_distribution.png")
plt.close()

# -------- 3. Risk Level Pie Chart --------
risk_counts = df['risk_category'].value_counts()
plt.figure(figsize=(7, 7))
plt.pie(risk_counts, labels=risk_counts.index, autopct='%1.1f%%', colors=["#98FB98", "#FFD700", "#FF6347"])
plt.title("Risk Category Distribution")
plt.tight_layout()
plt.savefig("risk_pie_chart.png")
plt.close()

print("✅ Visualizations saved as: top10_wallets.png, score_distribution.png, risk_pie_chart.png")
