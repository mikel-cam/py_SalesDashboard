# library used in data reading and analyzing
import pandas as pd
import matplotlib.pyplot as plt

# read or import data from excel --> .read_excel
# df is dataframe
df = pd.read_excel("sales_data.xlsx")

# print out first 5 data with headers
# print(df.head())

# get products that is sold the most
total_sales = df.groupby("Product")["Total"].sum()

# total_sales.plot(kind="bar", title="Total Sales by Product", ylabel="Sales ($)")
total_sales.plot(kind="pie", autopct="%1.1f%%", title="Sales Share by Product")
plt.ylabel("")
plt.tight_layout()
plt.show()
