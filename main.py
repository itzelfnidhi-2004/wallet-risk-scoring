import pandas as pd
import requests
import time

# Load wallet addresses
wallet_df = pd.read_csv("C:/Users/nehag/wallet-risk-scoring/wallets.csv")
wallets = wallet_df['wallet_id'].tolist()

# Compound V3 Subgraph for USDC on Ethereum Mainnet
COMPOUND_V3_URL = "https://api.thegraph.com/subgraphs/name/0xngmi/compound-v3-ethereum"

# GraphQL query template
def create_query(wallet):
    return {
        "query": """
        {
          account(id: "%s") {
            id
            positions {
              id
              market {
                name
              }
              totalDeposited
              totalBorrowed
              totalRepaid
              totalWithdrawn
            }
          }
        }
        """ % wallet.lower()
    }

# Collect data
data_list = []

for wallet in wallets:
    try:
        response = requests.post(COMPOUND_V3_URL, json=create_query(wallet))
        if response.status_code == 200:
            result = response.json()
            acct = result.get('data', {}).get('account')
            if acct:
                for pos in acct['positions']:
                    data_list.append({
                        "wallet_id": wallet,
                        "market": pos['market']['name'],
                        "deposited": float(pos['totalDeposited']),
                        "borrowed": float(pos['totalBorrowed']),
                        "repaid": float(pos['totalRepaid']),
                        "withdrawn": float(pos['totalWithdrawn'])
                    })
        else:
            print(f"Failed for {wallet}: {response.status_code}")
        time.sleep(0.5)  # Respect rate limit
    except Exception as e:
        print(f"Error for {wallet}: {str(e)}")

# Save collected data
df = pd.DataFrame(data_list)
df.to_csv("compound_v3_wallet_data.csv", index=False)
print("✅ Data saved to compound_v3_wallet_data.csv")
