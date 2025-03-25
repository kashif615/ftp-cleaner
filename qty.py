import pandas as pd

df = pd.read_csv("original.csv")

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
df.to_csv("factorywheelwarehouse_INVENTORY.csv", index=False)
print("✅ Cleaned CSV saved.")
