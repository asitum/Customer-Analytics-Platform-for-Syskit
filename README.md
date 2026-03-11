# Syskit Customer Analytics Platform

**Author:** Antoni Šitum  
**Date:** March 2026  
**Company:** Syskit

---

## 📊 Project Overview

Analytics platform developed for the Data Scientist position assignment at **Syskit**.

**Dataset:** 6 months (Jan-Jun 2024)  
**Scope:** 500 customer tenants  
**Data Sources:** Product telemetry, Subscription/Billing, CRM

---

## 🏗️ Architecture

```
syskit-customer-analytics/
├── src/           # Python code
├── notebooks/     # Jupyter notebooks
├── dashboard/     # Interactive dashboard
├── reports/       # PDF reports
├── models/        # ML models
├── data/          # Data files
├── requirements.txt
└── README.md
```

---

## 🎯 Key Results

### Customer Health Distribution
| Health Tier | Customers | Percentage | Total ARR |
|-------------|-----------|------------|-----------|
| **Monitoring** | 301 | 60.2% | $6,518,837 |
| **Healthy** | 103 | 20.6% | - |
| **At-Risk** | 70 | 14.0% | - |
| **Critical** | 26 | 5.2% | - |
| **TOTAL** | **500** | **100%** | **$16,519,686** |

### At-Risk Customers
- **96 customers** (19.2%) at high risk of churn
- **$1,342,696 ARR** at risk
- **46 customers** need immediate attention

### Model Performance (Random Forest)
| Metric | Score |
|--------|-------|
| F1 Score | 0.648 |
| Precision | 80% |
| Recall | 54.5% |
| ROC AUC | 0.923 |

### Top Predictors
1. Usage Decline Rate (31.2%)
2. Contact Recency (24.8%)
3. Active User Ratio (18.5%)

---

## 📈 Recommendations

| Timeline | Action | Impact |
|----------|--------|--------|
| Next 7 days | Contact 26 Critical customers | Prevent $230K loss |
| Next 30 days | Outreach to 70 At-Risk customers | Retain $435K |
| Next 60 days | Upsell campaign | +$186K ARR |
| Next quarter | Health dashboard | Reduce churn 2-3% |

---

## 🚀 Quick Start

```bash
git clone https://github.com/antoni-shitum/syskit-customer-analytics.git
cd syskit-customer-analytics
pip install -r requirements.txt
```

**Dashboard:** `dashboard/dashboard_interactive.html`

---

## 👤 Author

**Antoni Šitum**  
Data Scientist

---

© 2026 Antoni Šitum. All rights reserved.
