# Enhanced AML Transaction Monitoring Analysis

## Why this version is stronger

The model now considers customer behaviour rather than relying only on transaction size.

### Indicators

1. **Large transaction** — amount above INR 400,000.
2. **Potential structuring indicator** — incoming amount between INR 450,000 and INR 500,000.
3. **Transaction velocity** — 3 or more transactions by the same customer on one day.
4. **Customer baseline deviation** — transaction above five times the customer's pre-alert average.
5. **Foreign activity** — counterparty outside India.
6. **Rapid foreign movement** — foreign debit on a day when the customer also received credits.

## Illustrative scoring

| Indicator | Weight |
|---|---:|
| Large transaction | 1 |
| Potential structuring | 2 |
| Foreign activity | 1 |
| High velocity | 1 |
| Baseline deviation | 2 |
| Rapid foreign movement | 2 |

**Risk bands:** 5+ = High, 3–4 = Medium, below 3 = Low.

> These thresholds and weights are fictional and are used only for portfolio demonstration. They are not regulatory thresholds or a financial institution's production methodology.

## Focal case — CUST-1007

CUST-1007 is a High-risk retail customer. Earlier activity is small and routine. The account then shows:

- Three large incoming credits on 18 August.
- Credits clustered around INR 4.5–5.0 lakh.
- A foreign debit to the UAE on 18 August.
- A foreign debit to Singapore on 19 August.
- Two further large incoming credits on 20 August.
- A ₹960,000 foreign debit to the UK on 20 August.

The combined pattern warrants **Enhanced Due Diligence / further investigation**.

This is not a conclusion that money laundering occurred. A real review would consider KYC, expected activity, source of funds/wealth, transaction purpose, counterparties, sanctions/PEP screening, adverse media and applicable internal procedures.

## Data handling

All data in the underlying dataset is synthetic and created for learning/portfolio purposes.
