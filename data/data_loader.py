import pandas as pd

def load_telco_data():
    url = "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv"
    df = pd.read_csv(url)
    # Data Cleaning
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce').fillna(0)
    df['Churn'] = df['Churn'].apply(lambda x: 1 if x == 'Yes' else 0)
    return df.set_index('customerID')