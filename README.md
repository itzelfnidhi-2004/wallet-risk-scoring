# 🧠 Wallet Risk Scoring (Compound V3)

This project aims to analyze DeFi user behavior on the **Compound V3 protocol** and assign a **risk score (0–1000)** to each wallet address. The scoring logic is based on historical on-chain activity like borrows, repayments, collateral usage, and protocol interaction frequency.

> 🚀 This assignment was built using Python and real-world DeFi concepts. It includes full data preprocessing, feature extraction, scoring, and bonus visualizations to provide deep wallet-level insights.

---

## 📊 Project Highlights

- ✅ Parses wallet activity from Compound V3
- ✅ Calculates a **risk score** for each wallet (0–1000)
- ✅ Uses on-chain events like:
  - Borrows, Repayments
  - Supplied Collateral
  - Liquidation risk
  - Interaction frequency
- ✅ Generates a final CSV output: `wallet_risk_scores.csv`
- ✅ Includes **interactive visualizations** (bar charts, risk distribution, top risky wallets)

---

## 🧠 Scoring Logic

The scoring is based on a mix of heuristics:

| Feature | Description |
|--------|-------------|
| 📈 Borrow Volume | Higher borrowing = higher risk |
| 💸 Repayment Timeliness | Late repayments = penalty |
| 🏦 Collateral Usage | Low collateral = high liquidation risk |
| 🔁 Activity Frequency | Inactive wallets = penalized |
| 🚨 Liquidation Events | Direct risk indicator |

All features are normalized and combined into a weighted risk scoring formula.

---

## 📂 Project Structure


---

## 🧪 Tech Stack

- 🐍 Python 3.10
- 📡 Compound V3 API
- 📦 Pandas, Requests
- 📈 Matplotlib & Seaborn (Bonus Visuals)

---

## 📊 Sample Output

<p align="center">
  <img src="https://raw.githubusercontent.com/your-username/wallet-risk-scoring/main/sample-output.png" width="70%" />
</p>

---

## 📄 License

This project is licensed for educational and internship assignment use only.
