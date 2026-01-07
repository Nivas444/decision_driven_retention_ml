from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from decision_engine.cost_model import DecisionEngine

app = FastAPI(title="Retention System API")

# Initialize the engine with specific business parameters
# This matches the new __init__ in cost_model.py
engine = DecisionEngine(ltv=1200.0, cost=150.0, success_rate=0.6)

# Schema for incoming data (matches Telco dataset features)
class Customer(BaseModel):
    tenure: int
    MonthlyCharges: float
    TotalCharges: float
    # Add other fields as needed

@app.get("/")
def health_check():
    return {"status": "online", "system": "Decision-Driven Retention"}

@app.post("/decide")
def get_decision(customer: Customer):
    try:
        # 1. Simulate Model Prediction (Replace this with your actual model.predict)
        # Higher tenure usually means lower churn probability
        mock_p_churn = 0.75 if customer.tenure < 12 else 0.15
        
        # 2. Compute the Financial Decision
        results = engine.compute(mock_p_churn)
        
        return {
            "recommendation": "ACT" if results['action'] == 1 else "IGNORE",
            "financials": {
                "expected_gain": results['net_gain'],
                "churn_probability": results['p_churn']
            },
            "context": "Decision based on risk-adjusted ROI."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))