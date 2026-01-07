from data.data_loader import load_telco_data
from features.feature_engineering import FeatureEngineer
from pipeline.training_pipeline import train_model
from decision_engine.cost_model import DecisionEngine
from explainability.decision_explain import DecisionExplainer, get_global_importance
import pandas as pd

def run_system():
    # 1. DATA & FEATURES
    df = load_telco_data()
    fe = FeatureEngineer()
    X = fe.fit_transform(df)
    y = df['Churn']

    # 2. MODELING
    model = train_model(X, y)
    get_global_importance(model, X.columns)

    # 3. DECISION ENGINE
    engine = DecisionEngine()
    explainer = DecisionExplainer()
    probs = model.predict_proba(X)[:, 1]

    # 4. EXECUTION & EVALUATION
    results = []
    print("\n--- SAMPLE DECISIONS ---")
    for i in range(20): # Preview first 20
        cust_id = X.index[i]
        metrics = engine.compute_decision(probs[i])
        print(explainer.generate_local_explanation(cust_id, metrics))
        results.append(metrics)

    # 5. BUSINESS METRICS
    res_df = pd.DataFrame(results)
    total_gain = res_df[res_df['action'] == 1]['expected_gain'].sum()
    action_rate = res_df['action'].mean()
    
    print("\n--- SYSTEM SUMMARY ---")
    print(f"Retention Action Rate: {action_rate:.1%}")
    print(f"Projected Net Gain (Sample): ${total_gain:,.2f}")

if __name__ == "__main__":
    run_system()