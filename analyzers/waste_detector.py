from typing import Dict, Any, List

class WasteDetector:
    def __init__(self):
        pass

    def scan_all_subscriptions(self) -> Dict[str, Any]:
        """Simulates enterprise scan across multi-cloud subscriptions for unattached resources."""
        orphan_disks = [
            {"id": "/subscriptions/sub-01/resourceGroups/rg-dev/providers/Microsoft.Compute/disks/disk-temp-01", "size_gb": 512, "sku": "Premium_LRS", "cost_usd": 76.80},
            {"id": "/subscriptions/sub-01/resourceGroups/rg-uat/providers/Microsoft.Compute/disks/disk-test-db", "size_gb": 1024, "sku": "Premium_LRS", "cost_usd": 153.60}
        ]
        
        zombie_snapshots = [
            {"id": "snap-backup-2023-01", "age_days": 184, "cost_usd": 24.50},
            {"id": "snap-mig-test-09", "age_days": 120, "cost_usd": 18.00}
        ]
        
        disassociated_ips = [
            {"ip": "20.42.18.99", "allocation": "Static", "cost_usd": 4.50},
            {"ip": "52.149.88.12", "allocation": "Static", "cost_usd": 4.50}
        ]
        
        total_waste = sum(d["cost_usd"] for d in orphan_disks) + sum(s["cost_usd"] for s in zombie_snapshots) + sum(i["cost_usd"] for i in disassociated_ips)
        
        return {
            "orphan_disks_count": len(orphan_disks),
            "zombie_snapshots_count": len(zombie_snapshots),
            "disassociated_ips_count": len(disassociated_ips),
            "monthly_waste_usd": total_waste
        }
