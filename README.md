# 💰 Cloud FinOps Sentinel
### Event-Driven Multi-Cloud Cost Optimization & Automated Waste Elimination Engine

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FinOps](https://img.shields.io/badge/Standard-FinOps_Foundation-3498DB?style=for-the-badge)](https://finops.org)
[![Azure](https://img.shields.io/badge/Cloud-Multi_Cloud_Audit-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white)](https://azure.microsoft.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

---

## 💡 Overview

**Cloud FinOps Sentinel** is an automated cloud financial management framework. It runs continuous serverless audits across enterprise Azure and AWS subscriptions to detect idle compute, eliminate orphan storage, enforce rightsizing based on 30-day utilization percentiles, and deliver up to **32% cloud OPEX reductions**.

```
[ Scheduled FinOps Audit Trigger ]
               │
               ▼
+─────────────────────────────────────────────────────────────+
|               Multi-Cloud Resource Discovery Engine         |
+──────────────────────────────┬──────────────────────────────+
                               │
         ┌─────────────────────┼─────────────────────┐
         ▼                     ▼                     ▼
[ Orphan Disks & Snaps ] [ Idle Public IPs ]   [ 30-Day VM Rightsizing ]
         │                     │                     │
         └─────────────────────┼─────────────────────┘
                               │
                               ▼
               [ Interactive Slack / Teams Digest ]
               "Identified $18,450/month in cloud waste.
                Approve Auto-Cleanup Runbook? [Approve] / [Reject]"
```

## ⚡ Core Capabilities

1. **Unattached Storage Cleanup:** Detects unattached Azure Managed Disks and AWS EBS volumes; calculates waste and dispatches purge approvals.
2. **Zombie Snapshot Pruning:** Identifies snapshots older than 90 days with no parent volume.
3. **P95 Rightsizing Engine:** Analyzes 30-day CPU and Memory telemetry to recommend downgrading over-provisioned instances to modern generation SKUs.
4. **Predictive Infracost CI/CD Gating:** Pre-merge validation stopping runaway resource scale in pull requests.

## 🚀 Quickstart

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Execute Local Audit:**
   ```bash
   python function_app.py
   ```
