import yaml

class DecisionEngine:
    def __init__(self, config_path='config/costs.yaml'):
        with open(config_path, 'r') as f:
            self.cfg = yaml.safe_load(f)['business_params']

    def compute_decision(self, p_churn):
        ltv = self.cfg['avg_customer_lifetime_value']
        cost = self.cfg['retention_offer_cost']
        success = self.cfg['retention_success_rate']
        
        # Expected Loss = Probability * Impact
        expected_loss = p_churn * ltv
        # Expected Gain = (Loss we might save) - Cost of trying
        expected_gain = (expected_loss * success) - cost
        
        return {
            "p_churn": p_churn,
            "expected_gain": round(expected_gain, 2),
            "action": 1 if expected_gain > 0 else 0
        }