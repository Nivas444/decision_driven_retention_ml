class DecisionExplainer:
    @staticmethod
    def generate_local_explanation(cust_id, decision_metrics):
        p = decision_metrics['p_churn']
        gain = decision_metrics['expected_gain']
        action = "OFFER RETENTION" if decision_metrics['action'] == 1 else "NO ACTION"
        
        return (f"Customer: {cust_id} | Churn Prob: {p:.1%} | "
                f"Expected Gain: ${gain} | Decision: {action}")

def get_global_importance(model, feature_names):
    import pandas as pd
    importance = pd.Series(model.coef_[0], index=feature_names).sort_values()
    print("\n--- GLOBAL DRIVERS ---")
    print(f"Top Churn Reducers: {importance.head(2).index.tolist()}")
    print(f"Top Churn Drivers: {importance.tail(2).index.tolist()}")