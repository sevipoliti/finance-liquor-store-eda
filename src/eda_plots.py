import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/finance_liquor_sales_2016_2019.csv")
sold_bottles_per_zipcode_df = df[["zip_code", "item_description", "bottles_sold"]]
sold_bottles_per_zipcode_df_grouped = df.groupby(["zip_code", "item_description"])["bottles_sold"].sum().reset_index()
sales_per_store_df = df[["store_number", "sale_dollars"]]
sales_per_store_df_grouped = sales_per_store_df.groupby("store_number")["sale_dollars"].sum().reset_index()
sales_per_store_df_grouped['sales_percentage'] = (sales_per_store_df_grouped['sale_dollars'] /
                                                  sales_per_store_df_grouped['sale_dollars'].sum()) * 100

# ax1 = sns.scatterplot(x=sold_bottles_per_zipcode_df_grouped["zip_code"],
#                      y=sold_bottles_per_zipcode_df_grouped["bottles_sold"],
#                      hue=sold_bottles_per_zipcode_df_grouped["item_description"], legend=False).set(
#     title="Bottles sold per zip_code")
# plt.show()
ax2 = sns.barplot(x=sales_per_store_df_grouped["sales_percentage"], y=sales_per_store_df_grouped["store_number"],
                  orient="h",
                  order=sales_per_store_df_grouped.sort_values('sales_percentage', ascending=False).store_number)

plt.show()

sns.scatterplot(data=sales_per_store_df_grouped, x="store_number", y="sales_percentage", size="sales_percentage", legend=False, sizes=(20, 2000))

# show the graph
plt.show()
