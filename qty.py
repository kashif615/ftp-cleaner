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

# Save all columns as text but ensure Quantity values are quoted
# Export using QUOTE_ALL to force quotes around everything
# Then remove quotes from other columns manually if needed

# Save to temporary file with all quotes
df.to_csv("_temp_inventory.csv", index=False, quoting=csv.QUOTE_ALL)

# Read back and rewrite with only Quantity quoted
with open("_temp_inventory.csv", "r") as infile, open("factorywheelwarehouse_INVENTORY.csv", "w") as outfile:
    header = infile.readline()
    outfile.write(header)
    for line in infile:
        parts = line.strip().split(",")
        cleaned = []
        for i, col in enumerate(df.columns):
            val = parts[i].strip('"')
            if col == "Quantity":
                cleaned.append(f'"{val}"')
            else:
                cleaned.append(val)
        outfile.write(",".join(cleaned) + "\n")

print("✅ Quantity column cleaned and saved as quoted text only.")
