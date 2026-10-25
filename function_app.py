"""
Cloud FinOps Sentinel - Serverless Financial Management Engine
Automates continuous waste identification, rightsizing, and cost attribution across multi-cloud subscriptions.
"""
import logging
from analyzers.waste_detector import WasteDetector
from analyzers.rightsizing import RightsizingEngine
from notifiers.slack_notifier import CostAlertNotifier

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def execute_finops_audit():
    logging.info("Starting Enterprise FinOps Multi-Cloud Cost Audit...")
    
    detector = WasteDetector()
    waste_summary = detector.scan_all_subscriptions()
    
    rightsizing = RightsizingEngine()
    rightsizing_summary = rightsizing.evaluate_compute_utilization()
    
    total_monthly_savings = waste_summary["monthly_waste_usd"] + rightsizing_summary["potential_monthly_savings_usd"]
    annualized_savings = total_monthly_savings * 12
    
    logging.info(f"Audit Complete! Identified ${total_monthly_savings:,.2f}/mo in potential savings (${annualized_savings:,.2f} Annualized).")
    
    notifier = CostAlertNotifier()
    notifier.dispatch_summary(waste_summary, rightsizing_summary, total_monthly_savings)
    
    return {
        "monthly_savings_usd": total_monthly_savings,
        "annualized_savings_usd": annualized_savings,
        "waste_details": waste_summary,
        "rightsizing_details": rightsizing_summary
    }

if __name__ == "__main__":
    result = execute_finops_audit()
    print("\n=== FINOPS AUDIT REPORT ===")
    print(f"Monthly Savings Opportunity:   ${result['monthly_savings_usd']:,.2f}")
    print(f"Annualized Run-Rate Savings:   ${result['annualized_savings_usd']:,.2f}")
