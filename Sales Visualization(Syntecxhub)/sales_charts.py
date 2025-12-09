import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")
print("Data loaded")

df["Date"] = pd.to_datetime(df["Date"])

df["Month"] = df["Date"].dt.to_period("M").astype(str)

# Line Chart
monthly_sales = df.groupby("Month")["Total"].sum()

plt.plot(monthly_sales.index, monthly_sales.values, marker="o")
plt.title("Monthly Total Sales")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_sales_line_chart.png")
plt.close()
print("Saved: monthly_sales_line_chart.png")

# Bar Chart
sales_by_product = df.groupby("Product line")["Total"].sum()

plt.bar(sales_by_product.index, sales_by_product.values)
plt.title("Total Sales by Product Line")
plt.xlabel("Product Line")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("sales_by_product_line_bar_chart.png")
plt.close()
print("Saved: sales_by_product_line_bar_chart.png")

# Pie Chart
sales_by_city = df.groupby("City")["Total"].sum()

plt.pie(sales_by_city.values, labels=sales_by_city.index, autopct="%1.1f%%")
plt.title("Sales Share by City")
plt.tight_layout()
plt.savefig("sales_by_city_pie_chart.png")
plt.close()
print("Saved: sales_by_city_pie_chart.png")

print("All charts created successfully!")
