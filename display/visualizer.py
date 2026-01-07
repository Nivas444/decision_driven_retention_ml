import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

class RetentionVisualizer:
    def __init__(self):
        # Using the new Seaborn objects interface available in 0.13+
        sns.set_theme(style="whitegrid", palette="muted")

    def plot_decision_frontier(self, ltv=1200, cost=150, success_rate=0.6):
        """EXPLAINABILITY LEVEL 2: Shows the financial break-even point."""
        p_range = np.linspace(0, 1, 100)
        gains = [(p * ltv * success_rate) - cost for p in p_range]
        
        plt.figure(figsize=(10, 5))
        plt.plot(p_range, gains, lw=3, color='#2ecc71', label='Expected Gain')
        plt.axhline(0, color='black', linestyle='--', alpha=0.5)
        
        # Shade the profitable zone
        plt.fill_between(p_range, gains, 0, where=(np.array(gains) > 0), 
                         alpha=0.2, color='green', label='Actionable Zone')
        
        plt.title("Decision Logic: When does an intervention become profitable?", fontsize=14)
        plt.xlabel("Churn Probability P(churn)")
        plt.ylabel("Expected Net Gain ($)")
        plt.legend()
        plt.show()

    def plot_business_impact(self, probs, ltv=1200, cost=150, success_rate=0.6):
        """EVALUATION LEVEL 3: Total projected profit for the whole company."""
        thresholds = np.linspace(0, 1, 100)
        total_gains = []
        for t in thresholds:
            # Sum of gains for all customers we decide to act on at this threshold
            gain = sum([(p * ltv * success_rate) - cost for p in probs if p >= t])
            total_gains.append(gain)
            
        plt.figure(figsize=(10, 5))
        sns.lineplot(x=thresholds, y=total_gains, color='royalblue', lw=2)
        plt.axvline(thresholds[np.argmax(total_gains)], color='red', linestyle=':', label='Max ROI Threshold')
        plt.title("System Evaluation: Total Projected Net Saved Value", fontsize=14)
        plt.xlabel("Decision Threshold (Act if P > T)")
        plt.ylabel("Total Portfolio Gain ($)")
        plt.legend()
        plt.show()

# RUN THIS FILE INDEPENDENTLY
if __name__ == "__main__":
    print("--- Starting Standalone Visualization Tool ---")
    viz = RetentionVisualizer()
    
    # Simulate some model output probabilities
    mock_model_probs = np.random.beta(2, 5, 1000) 
    
    # 1. Show the Logic
    viz.plot_decision_frontier()
    
    # 2. Show the Business Impact
    viz.plot_business_impact(mock_model_probs)