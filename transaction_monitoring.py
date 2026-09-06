import pandas as pd

# AML Transaction Monitoring — Enhanced Synthetic Case Study
# All thresholds are illustrative and for portfolio learning only.

df = pd.read_csv("synthetic_transactions.csv")
df["Date"] = pd.to_datetime(df["Date"])

# 1. Transaction-level indicators
df["Large_Transaction_Flag"] = df["Amount_INR"] > 400000

df["Structuring_Indicator"] = (
    (df["Direction"] == "Credit")
    & df["Amount_INR"].between(450000, 500000)
)

df["Foreign_Activity_Flag"] = df["Counterparty_Country"] != "India"

# 2. Establish a pre-alert customer baseline.
# This avoids letting the suspicious period inflate the benchmark.
first_alert_date = (
    df[df["Large_Transaction_Flag"] | df["Structuring_Indicator"]]
    .groupby("Customer_ID")["Date"]
    .min()
    .rename("First_Alert_Date")
)

df = df.merge(first_alert_date, on="Customer_ID", how="left")

baseline = (
    df[df["First_Alert_Date"].isna() | (df["Date"] < df["First_Alert_Date"])]
    .groupby("Customer_ID")
    .agg(
        Baseline_Avg_INR=("Amount_INR", "mean"),
        Baseline_Max_INR=("Amount_INR", "max"),
        Baseline_Transactions=("Transaction_ID", "count"),
    )
    .reset_index()
)

df = df.merge(baseline, on="Customer_ID", how="left")

# 3. Transaction velocity
daily = (
    df.groupby(["Customer_ID", "Date"])
    .size()
    .reset_index(name="Transactions_Per_Day")
)

df = df.merge(daily, on=["Customer_ID", "Date"], how="left")
df["High_Velocity_Flag"] = df["Transactions_Per_Day"] >= 3

# 4. Deviation from the customer's own baseline
df["Baseline_Deviation_Flag"] = (
    df["Baseline_Avg_INR"].notna()
    & (df["Amount_INR"] > df["Baseline_Avg_INR"] * 5)
)

# 5. Same-day incoming funds followed by foreign movement
credits = (
    df[df["Direction"] == "Credit"]
    .groupby(["Customer_ID", "Date"])["Amount_INR"]
    .sum()
    .rename("Same_Day_Credit_Value_INR")
    .reset_index()
)

df = df.merge(credits, on=["Customer_ID", "Date"], how="left")

df["Rapid_Foreign_Movement_Flag"] = (
    (df["Direction"] == "Debit")
    & df["Foreign_Activity_Flag"]
    & (df["Same_Day_Credit_Value_INR"].fillna(0) > 0)
)

# 6. Illustrative weighted score
df["Risk_Score"] = (
    df["Large_Transaction_Flag"].astype(int) * 1
    + df["Structuring_Indicator"].astype(int) * 2
    + df["Foreign_Activity_Flag"].astype(int) * 1
    + df["High_Velocity_Flag"].astype(int) * 1
    + df["Baseline_Deviation_Flag"].astype(int) * 2
    + df["Rapid_Foreign_Movement_Flag"].astype(int) * 2
)

def risk_band(score):
    if score >= 5:
        return "High"
    if score >= 3:
        return "Medium"
    return "Low"

df["Risk_Band"] = df["Risk_Score"].apply(risk_band)

# 7. Produce alerts
alerts = df[df["Risk_Score"] >= 3].copy()

alerts.to_csv("enhanced_transaction_analysis.csv", index=False)

print("\n=== ENHANCED ALERTS ===")
print(alerts[
    [
        "Transaction_ID", "Date", "Customer_ID", "Direction",
        "Amount_INR", "Counterparty_Country",
        "Transactions_Per_Day", "Risk_Score", "Risk_Band"
    ]
].to_string(index=False))

print("\n=== FOCAL CASE: CUST-1007 ===")
print(alerts[alerts["Customer_ID"] == "CUST-1007"][
    [
        "Transaction_ID", "Date", "Direction", "Amount_INR",
        "Counterparty_Country", "Transactions_Per_Day",
        "Same_Day_Credit_Value_INR", "Risk_Score", "Risk_Band"
    ]
].to_string(index=False))

print(
    "\nRecommended next step: Enhanced Due Diligence / "
    "further investigation based on the combined indicators."
)
