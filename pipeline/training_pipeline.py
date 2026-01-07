from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_recall_curve, auc

def train_model(X, y):
    # Use class_weight='balanced' to handle churn imbalance
    model = LogisticRegression(class_weight='balanced', max_iter=1000)
    model.fit(X, y)
    
    probs = model.predict_proba(X)[:, 1]
    p, r, _ = precision_recall_curve(y, probs)
    print(f"Model Training Metrics: PR-AUC = {auc(r, p):.3f}")
    return model