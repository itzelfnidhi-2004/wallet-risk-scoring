import pandas as pd

def calculate_credit_score(row):
    score = 300
    score += min(row['supplied'] / 100, 300)
    score += max(0, 200 - row['borrowed'] / 100)
    score += row['repay_rate'] * 200
    score += row['health_score'] * 100
    return min(score, 1000)

df = pd.read_csv("compound_v3_wallet_data.csv")
df['credit_score'] = df.apply(calculate_credit_score, axis=1)
df.to_csv("scored_wallets.csv", index=False)

print("✅ Credit scores saved to scored_wallets.csv")
