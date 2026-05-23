import pandas as pd

# Load the big grocery file
df = pd.read_csv("data/Australia_Grocery_2022Sep.csv")

# Make sure price columns are numeric
df["Retail_price"] = pd.to_numeric(df["Retail_price"], errors="coerce")
df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")
df["is_special"] = pd.to_numeric(df["is_special"], errors="coerce")

# 1. Average price by state
state_summary = df.groupby("state").agg(
    avg_retail_price=("Retail_price", "mean"),
    avg_unit_price=("unit_price", "mean"),
    product_count=("Retail_price", "count")
).reset_index()

state_summary.to_csv("data/grocery_state_summary.csv", index=False)

# 2. Average price by category
category_summary = df.groupby("Category").agg(
    avg_retail_price=("Retail_price", "mean"),
    avg_unit_price=("unit_price", "mean"),
    product_count=("Retail_price", "count")
).reset_index()

category_summary.to_csv("data/grocery_category_summary.csv", index=False)

# 3. Specials by category
special_summary = df.groupby("Category").agg(
    percent_on_special=("is_special", "mean"),
    product_count=("is_special", "count")
).reset_index()

special_summary["percent_on_special"] = special_summary["percent_on_special"] * 100
special_summary.to_csv("data/grocery_special_summary.csv", index=False)

print("Done. Summary CSV files created.")