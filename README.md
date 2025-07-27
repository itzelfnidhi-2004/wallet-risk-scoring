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

```bash
wallet-risk-scoring/
│
├── main.py                 # Extracts wallet activity & saves CSV
├── score_wallets.py        # Scores wallets based on logic
├── visualize_scores.py     # Plots graphs from final scores
├── config.py               # Configurations for weightage & thresholds
├── utils/                  # Utility functions (parsing, formatting, etc.)
│
├── real_wallets.csv        # Raw input wallet list
├── compound_v3_wallet_data.csv  # Cleaned dataset
├── wallet_scores.csv       # Final output with scores
│
├── sample-output.png       # Screenshot of score visualizations
├── README.md               # You’re reading it 😊
├── LICENSE
└── requirements.txt


---

## 🧪 Tech Stack

- 🐍 Python 3.10
- 📡 Compound V3 API
- 📦 Pandas, Requests
- 📈 Matplotlib & Seaborn (Bonus Visuals)

---



---

## 📄 License

This project is licensed for educational and internship assignment use only.
