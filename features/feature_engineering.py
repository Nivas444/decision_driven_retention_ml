import pandas as pd
from sklearn.preprocessing import StandardScaler

class FeatureEngineer:
    def __init__(self):
        self.scaler = StandardScaler()
        self.num_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
        self.final_columns = None

    def fit_transform(self, df):
        X = df.drop('Churn', axis=1)
        X = pd.get_dummies(X, drop_first=True)
        X[self.num_cols] = self.scaler.fit_transform(X[self.num_cols])
        self.final_columns = X.columns
        return X

    def transform(self, df):
        X = pd.get_dummies(df, drop_first=True)
        X = X.reindex(columns=self.final_columns, fill_value=0)
        X[self.num_cols] = self.scaler.transform(X[self.num_cols])
        return X