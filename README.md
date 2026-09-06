# AML Transaction Monitoring Case Study

## Overview

This project demonstrates a **synthetic-data transaction monitoring investigation** from alert generation through case disposition.

The objective is to identify potentially suspicious transaction behaviour, document the red flags, assess the customer's risk, and reach a defensible investigation outcome.

> **Important:** All customer names, identifiers, transactions, and values in this project are fictional and created for portfolio/learning purposes. No confidential or real customer information is used.

## Scenario

A retail customer with an existing **High** customer-risk rating shows a sudden change in transaction behaviour.

During August 2026, the customer receives multiple large incoming payments from unrelated counterparties and then sends substantial funds to foreign jurisdictions within a short period.

The monitoring review focuses on whether the activity is consistent with the customer's expected profile and whether escalation is warranted.

## Key Monitoring Rules

The analysis uses simple rule-based indicators:

1. **Large transaction** — transaction amount above INR 400,000.
2. **Potential structuring** — multiple incoming transactions between INR 450,000 and INR 500,000 within a short period.
3. **Rapid movement of funds** — significant outgoing transfers shortly after multiple incoming credits.
4. **Foreign activity** — international transfers involving selected foreign jurisdictions.
5. **Existing customer risk** — higher-risk customers receive enhanced scrutiny when unusual behaviour occurs.

These rules are illustrative and are **not intended to represent a regulated institution's production thresholds or official policy**.

## Investigation Focus

### Customer under review
- **Customer ID:** CUST-1007
- **Segment:** Retail
- **Existing risk:** High

### Observed red flags
- Multiple high-value incoming credits on the same day.
- Several incoming amounts are close to INR 500,000.
- Funds move out to UAE, Singapore and the UK shortly after credits.
- Transaction behaviour is inconsistent with the surrounding routine activity in the dataset.
- Multiple unrelated counterparties are involved.

## Preliminary Assessment

The combination of **structuring-like incoming activity, rapid movement of funds, multiple counterparties, international transfers, and an existing High-risk rating** creates a material level of suspicion requiring enhanced investigation.

A real investigation would require supporting information such as source of funds, source of wealth, customer occupation/business activity, expected account turnover, counterparty relationships, transaction purpose, and relevant documentary evidence.

## Illustrative Disposition

**Recommended outcome: Escalate for Enhanced Due Diligence / further investigation.**

This portfolio case does not make a real-world SAR/STR determination. The example is designed to demonstrate analytical reasoning and investigation documentation.

## Tools

- Python
- Pandas
- CSV
- Rule-based transaction monitoring
- AML investigation methodology

## Project Structure

```text
aml-transaction-monitoring-case-study/
├── README.md
├── CASE_SUMMARY.md
├── ENHANCED_ANALYSIS.md
├── synthetic_transactions.csv
└── transaction_monitoring.py

## Learning Outcomes

This project demonstrates the ability to:

- Review transactional activity against a customer profile.
- Identify common transaction-monitoring red flags.
- Apply rule-based alert logic.
- Connect multiple indicators rather than relying on a single transaction.
- Document an investigation in a structured manner.
- Form a risk-based recommendation.

