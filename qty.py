import pandas as pd
import os
import csv

# Load the downloaded CSV
if not os.path.exists("original.csv") or os.path.getsize("original.csv") == 0:
    raise ValueError("❌ original.csv is missing or empty!")

df = pd.read_csv("original.csv")

# Clean Quantity column
def clean(val):
    if pd.isna(val):
        return ""
    try:
        return str(int(float(val)))
    except ValueError:
        return str(val)

if "Quantity" not in df.columns:
    raise ValueError("❌ 'Quantity' column not found in CSV.")

df["Quantity"] = df["Quantity"].apply(clean)

# Convert all columns to string, but Quantity will be quoted because it's str
for col in df.columns:
    if col != "Quantity":
        df[col] = df[col].astype(object)

# Save CSV with quoting only non-numeric fields (i.e., Quantity now gets quoted)
df.to_csv("factorywheelwarehouse_INVENTORY.csv", index=False, quoting=csv.QUOTE_NONNUMERIC)

print("✅ Quantity column cleaned and saved as quoted text.")
