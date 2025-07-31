
#1

import pandas as pd

df = pd.read_csv("task/sales_data.csv")

# Task 1


category_stats = df.groupby("Category").agg({
    "Quantity": ["sum", "max"],
    "Price": "mean"
})
print("#1\n", category_stats)

# Task 2

top_products = df.groupby(["Category", "Product"])["Quantity"].sum().reset_index()
top_products = top_products.sort_values(["Category", "Quantity"], ascending=[True, False])
top_per_category = top_products.groupby("Category").first()
print("\n#2\n", top_per_category)

# Task 3

df["Total"] = df["Quantity"] * df["Price"]
sales_per_day = df.groupby("Date")["Total"].sum()
max_sales_date = sales_per_day.idxmax()
print("\n#3\nDate with highest total sales:", max_sales_date)






# 2


df = pd.read_csv("task/customer_orders.csv")

# Task 1
order_counts = df.groupby("CustomerID")["OrderID"].count()
frequent_customers = order_counts[order_counts >= 20]
print("#1\nCustomers with 20+ orders:\n", frequent_customers)

# Task 2
avg_price_per_customer = df.groupby("CustomerID")["Price"].mean()
high_spenders = avg_price_per_customer[avg_price_per_customer > 120]
print("\n#2\nCustomers with avg price > 120:\n", high_spenders)

# Task 3
product_stats = df.groupby("Product").agg({
    "Quantity": "sum",
    "Price": "sum"
})
filtered_products = product_stats[product_stats["Quantity"] >= 5]
print("\n#3\nProducts with total quantity ≥ 5:\n", filtered_products)
