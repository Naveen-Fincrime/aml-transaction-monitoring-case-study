import pandas as pd

# Load synthetic transaction data
df = pd.read_csv("synthetic_transactions.csv")
df["Date"] = pd.to_datetime(df["Date"])

# Rule 1: large transactions
df["Large_Transaction_Flag"] = df["Amount_INR"] > 400000

# Rule 2: potentially structured incoming payments
df["Structuring_Flag"] = (
    (df["Direction"] == "Credit")
    & (df["Amount_INR"].between(450000, 500000))
)

# Rule 3: foreign activity
df["Foreign_Activity_Flag"] = df["Counterparty_Country"] != "India"

# Combined alert score (illustrative only)
flag_columns = [
    "Large_Transaction_Flag",
    "Structuring_Flag",
    "Foreign_Activity_Flag",
]
df["Alert_Score"] = df[flag_columns].sum(axis=1)

# Show transactions with at least one indicator
alerts = df[df["Alert_Score"] > 0].copy()

print("\n=== TRANSACTION MONITORING ALERTS ===")
print(alerts[
    [
        "Transaction_ID", "Date", "Customer_ID", "Direction",
        "Amount_INR", "Counterparty_Country", "Alert_Score"
    ]
].to_string(index=False))

# Customer-level summary
summary = (
    alerts.groupby("Customer_ID")
    .agg(
        Alerted_Transactions=("Transaction_ID", "count"),
        Total_Alerted_Amount_INR=("Amount_INR", "sum"),
        Max_Alert_Score=("Alert_Score", "max"),
    )
    .sort_values("Alerted_Transactions", ascending=False)
)

print("\n=== CUSTOMER-LEVEL ALERT SUMMARY ===")
print(summary.to_string())

# Highlight focal customer
focal = alerts[alerts["Customer_ID"] == "CUST-1007"]

print("\n=== FOCAL CASE: CUST-1007 ===")
print(focal[
    [
        "Transaction_ID", "Date", "Direction", "Amount_INR",
        "Counterparty_Country", "Alert_Score"
    ]
].to_string(index=False))

print("\nRecommended next step: Enhanced Due Diligence / further investigation.")
