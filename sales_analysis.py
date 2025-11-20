#  Sales Data Analysis (Python Script)
# Author: Your Name
# Task: Data Analysis on CSV Files
# Tools: Pandas, Matplotlib

import pandas as pd
import matplotlib.pyplot as plt
import os

file_name = "sales.csv"   

if not os.path.exists(file_name):
    print("❌ File not found! Place 'sales.csv' in the same folder.")
    exit()

df = pd.read_csv(file_name)
print("\n✅ File loaded successfully!\n")

print(" DATA INFO:")
print(df.info())
print("\n FIRST 5 ROWS:")
print(df.head())

print("\n🔍 MISSING VALUES:")
print(df.isnull().sum())

df = df.dropna()

total_sales = df["Sales"].sum()
print(f"\n TOTAL SALES = {total_sales}")

sales_by_product = df.groupby("Product")["Sales"].sum()
print("\n SALES BY PRODUCT:")
print(sales_by_product)

plt.figure(figsize=(10,5))
sales_by_product.plot(kind="bar")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.grid(True)
plt.savefig("sales_by_product.png")
plt.close()
print(" Saved: sales_by_product.png")

df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month

sales_by_month = df.groupby("Month")["Sales"].sum()
print("\n SALES BY MONTH:")
print(sales_by_month)

plt.figure(figsize=(10,5))
sales_by_month.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.savefig("sales_by_month.png")
plt.close()
print(" Saved: sales_by_month.png")

sales_by_region = df.groupby("Region")["Sales"].sum()
print("\n SALES BY REGION:")
print(sales_by_region)

plt.figure(figsize=(6,6))
sales_by_region.plot(kind="pie", autopct="%1.1f%%")
plt.title("Sales by Region")
plt.ylabel("")
plt.savefig("sales_by_region.png")
plt.close()
print(" Saved: sales_by_region.png")

best_product = sales_by_product.idxmax()
worst_product = sales_by_product.idxmin()

print("\n🏆 Best Selling Product:", best_product)
print(" Worst Selling Product:", worst_product)

print("\n🎉 ANALYSIS COMPLETE!")
print("Charts saved in the current folder.")
