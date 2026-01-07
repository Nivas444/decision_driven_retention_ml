# Decision-Driven Customer Retention System

## Decision Logic
Unlike standard classifiers, this system uses a **Financial Utility Function**. We only intervene if the cost of the retention offer is less than the risk-adjusted value of the customer.

## Evaluation Levels
1. **Model:** We optimize for PR-AUC to ensure we rank high-risk customers correctly.
2. **Decision:** We track 'Action Rate'—how often the system recommends spending money.
3. **Business:** We track 'Net Gain', which is the predicted dollars saved minus marketing spend.

## Limitations
- Assumes a fixed LTV for all customers.
- Success rate of the retention action is a heuristic and should be validated via A/B testing.