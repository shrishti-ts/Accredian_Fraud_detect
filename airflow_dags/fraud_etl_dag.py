import pandas as pd
import sqlite3

# Simulate Extract
df = pd.read_csv("Fraud.csv")  # adjust path

# Simulate Transform
df = df.dropna()
df['type'] = df['type'].astype('category').cat.codes
df['transaction_velocity'] = df['amount'] / (df['step'] + 1)
df['amount_to_balance_ratio'] = df['amount'] / (df['oldbalanceOrg'] + 1)
df = df.drop(['nameOrig', 'nameDest'], axis=1)

# Simulate Load
conn = sqlite3.connect("fraud_cleaned.db")
df.to_sql("transactions", conn, if_exists="replace", index=False)
conn.close()

print("✅ ETL simulation complete — stored in fraud_cleaned.db")
