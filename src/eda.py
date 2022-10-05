import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import DataFrame


def scatter_plot(df: DataFrame, x: str, y: str, hue: str, title: str):
    ax = sns.scatterplot(x=df[x],
                         y=df[y],
                         hue=df[hue], legend=False).set(title=title)
    plt.show()


def bar_plot(df: DataFrame, x: str, y: str, order_by: str):
    ax = sns.barplot(x=df[x], y=df[y],
                     orient="h",
                     order=df.sort_values(order_by, ascending=False).store_number)
    plt.show()


# sns.scatterplot(data=sales_per_store_df_grouped, x="store_number", y="sales_percentage", size="sales_percentage",
#                 legend=False, sizes=(20, 2000))

# show the graph
# plt.show()


def main():
    # Read the csv file that contains the finance_liquor_sales data
    df = pd.read_csv("data/finance_liquor_sales_2016_2019.csv")
    # Create a df containing the zip_code, item_description, bottles_sold
    sold_bottles_per_zipcode_df = df[["zip_code", "item_description", "bottles_sold"]]
    # Group by zip_code and item_description and sum the bottles sold for each group
    sold_bottles_per_zipcode_df_grouped = sold_bottles_per_zipcode_df.groupby(["zip_code", "item_description"])[
        "bottles_sold"].sum().reset_index()
    # Create a df containing the store_number, sale_dollars
    sales_per_store_df = df[["store_number", "sale_dollars"]]
    # Group by store_number and sum the sale_dollars for each group
    sales_per_store_df_grouped = sales_per_store_df.groupby("store_number")["sale_dollars"].sum().reset_index()
    # Add new column containing the sales percentage for each store
    sales_per_store_df_grouped['sales_percentage'] = (sales_per_store_df_grouped['sale_dollars'] /
                                                      sales_per_store_df_grouped['sale_dollars'].sum()) * 100
    # Create a scatter plot that shows the bottles sold per zip code
    scatter_plot(sold_bottles_per_zipcode_df_grouped, "zip_code", "bottles_sold", "item_description",
                 "Bottles sold per zip_code")
    # Create a barplot with the sales percentages in descending order
    bar_plot(sales_per_store_df_grouped, "sales_percentage", "store_number", "sales_percentage")


if __name__ == "__main__":
    main()
