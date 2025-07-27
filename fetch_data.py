

import requests
import pandas as pd
from config import DEBANK_API_URL, DEBANK_API_KEY

def fetch_wallet_data(csv_file):
    df = pd.read_csv(csv_file)
    wallet_data = []

    for idx, row in df.iterrows():
        wallet_id = row['wallet_id']
        print(f"🔍 Fetching data for wallet {wallet_id}...")

        try:
            response = requests.get(
                DEBANK_API_URL,
                params={"id": wallet_id},
                headers={"AccessKey": DEBANK_API_KEY}
            )
            response.raise_for_status()
            data = response.json()

            total_usd = data.get("total_usd_value", 0)
            chains = data.get("chain_list", [])
            active_chains = len(chains)

            wallet_data.append({
                "wallet_id": wallet_id,
                "total_usd_value": total_usd,
                "active_chains": active_chains,
            })

        except Exception as e:
            print(f"❌ Error fetching data for {wallet_id}: {e}")

    return wallet_data
