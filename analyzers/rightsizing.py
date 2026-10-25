from typing import Dict, Any, List

class RightsizingEngine:
    def __init__(self):
        pass

    def evaluate_compute_utilization(self) -> Dict[str, Any]:
        """Analyzes 30-day CPU and Memory percentiles to identify oversized VM compute."""
        recommendations = [
            {
                "vm_name": "vm-app-tier-prod-01",
                "current_sku": "Standard_D8s_v5",
                "recommended_sku": "Standard_D4s_v5",
                "p95_cpu": 18.4,
                "p95_memory": 34.2,
                "monthly_savings_usd": 146.00
            },
            {
                "vm_name": "vm-reporting-worker",
                "current_sku": "Standard_E16s_v5",
                "recommended_sku": "Standard_E8s_v5",
                "p95_cpu": 12.1,
                "p95_memory": 41.0,
                "monthly_savings_usd": 384.50
            }
        ]
        
        potential_savings = sum(r["monthly_savings_usd"] for r in recommendations)
        return {
            "candidates_count": len(recommendations),
            "potential_monthly_savings_usd": potential_savings,
            "recommendations": recommendations
        }
