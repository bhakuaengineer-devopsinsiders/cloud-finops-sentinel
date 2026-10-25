import json
from typing import Dict, Any

class CostAlertNotifier:
    def __init__(self):
        pass

    def dispatch_summary(self, waste: Dict[str, Any], rightsizing: Dict[str, Any], total_savings: float):
        message = {
            "title": "💰 Cloud FinOps Sentinel - Weekly Optimization Digest",
            "total_monthly_opportunity": f"${total_savings:,.2f}",
            "annualized_run_rate": f"${total_savings * 12:,.2f}",
            "details": {
                "orphan_disks": waste["orphan_disks_count"],
                "zombie_snapshots": waste["zombie_snapshots_count"],
                "disassociated_ips": waste["disassociated_ips_count"],
                "rightsizing_candidates": rightsizing["candidates_count"]
            }
        }
        print("\n[Slack / Teams Interactive Card Payload]:")
        print(json.dumps(message, indent=2))
