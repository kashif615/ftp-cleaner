import pandas as pd
import os

# Load the downloaded CSV
if not os.path.exists("original.csv") or os.path.getsize("original.csv") == 0:
    raise ValueError("❌ original.csv is missing or empty!")

df = pd.read_csv("original.csv")

# Clean Quantity column to preserve value as integer without quotes or formatting
def clean(val):
    if pd.isna(val):
        return ""
    try:
        return int(float(val))
    except ValueError:
        return val

if "Quantity" not in df.columns:
    raise ValueError("❌ 'Quantity' column not found in CSV.")

df["Quantity"] = df["Quantity"].apply(clean)

# Save CSV with cleaned Quantity values, no quotes, no extra formatting
df.to_csv("factorywheelwarehouse_INVENTORY.csv", index=False)

print("✅ Quantity column cleaned and preserved as plain number.")
