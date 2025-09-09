import pandas as pd
import sqlite3

def run_etl(file_path: str, db_name: str = "fraud_cleaned.db"):
    # Define column names in case headers are missing
    col_names = [
        "step", "type", "amount", "nameOrig", "oldbalanceOrg", "newbalanceOrig",
        "nameDest", "oldbalanceDest", "newbalanceDest", "isFraud", "isFlaggedFraud"
    ]
    
    # Extract
    try:
        df = pd.read_csv(file_path, names=col_names, skiprows=1)  # force column names
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return
    
    # Transform
    df = df.dropna()
    if "type" in df.columns:
        df["type"] = df["type"].astype("category").cat.codes
    else:
        print("⚠️ Warning: 'type' column not found")
    
    df["transaction_velocity"] = df["amount"] / (df["step"] + 1)
    df["amount_to_balance_ratio"] = df["amount"] / (df["oldbalanceOrg"] + 1)
    df = df.drop(["nameOrig", "nameDest"], axis=1, errors="ignore")
    
    # Load
    conn = sqlite3.connect(db_name)
    df.to_sql("transactions", conn, if_exists="replace", index=False)
    conn.close()
    
    print(f"✅ ETL complete — data stored in {db_name}")
    return df  # optional: return cleaned dataframe
  #**RUN**
df_cleaned = run_etl("Fraud.csv")

