# Finance liquor store - eda.py

####Steps:

######Data exploration:
- Index and columns dtypes
- Null values
- Memory usage
- Descriptive statistics include those that summarize the central tendency, dispersion and shape of a dataset’s distribution

######Sold bottles per zipcode dataset 
Creates a dataframe containing the zip_code, item_description and bottles_sold columns.
Then groups rows based on zip_code and item_description and calculates
the sum of bottles_sold for each group.

######Sales per store percentage dataset
Creates a dataframe containing the store_number and sale_dollars columns.
Then groups rows based on store_number and calculates
the sum of sale_dollars for each group. Finally creates a new column 
containing the percentages of sales per store.

######Scatter plot
Creates a scatter plot of the sold bottles per zip code.
Then saves it in the plots folder.

######Bar plot
Creates a barplot of the percentages of sales per store in descending order
and a barplot of the top five percentages of sales per store.
Then saves it in the plots folder.
