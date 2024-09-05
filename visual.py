import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns

data = pd.read_csv("edited.csv")
# print(data)


#Creating dataframe

df = pd.DataFrame(data)

#Top 10 Customers By Quantity

# customers = df.groupby("CustomerID")["Quantity"].sum()
# sorting = customers.sort_values(ascending=False)
# top_10_customers = sorting.head(10)
# print(top_10_customers)

#Bar plot

# sorting.head(10).plot(kind="bar", color = "Blue")
# plt.legend()
# plt.show()


#Top 10 Product Description

top_10_description = df["Description"].value_counts().nlargest(10)

sns.barplot(x=top_10_description.index, y=top_10_description.values)
plt.xlabel("Description")
plt.ylabel("Count")
plt.title("Top 10 Product Description")
plt.xticks(rotation = 45)
plt.show()

#Top 10 countries by quantity

# countries_total = df.groupby("Country")["Quantity"].sum()
# sorting = countries_total.sort_values(ascending=False)
# top_10_countries = sorting.head(10)
# print(top_10_countries)

# sorting.head(10).plot(kind="pie")
# plt.title("Top 10 countries by quantity")

# plt.legend(sorting.head(10))

# plt.legend()
# plt.show()

#Top 10 countries with highest cost price

# countries = df.groupby("Country")["Cost"].sum()
# sorting_countries = countries.sort_values(ascending=False).round()
# top10_countries_with_highest_cost = sorting_countries.head(10)
# print(top10_countries_with_highest_cost)

# top10_df = top10_countries_with_highest_cost.reset_index()

# Rename the columns for better readability
# top10_df.columns = ['Country', 'Total Cost']
# x_data = top10_df["Country"]
# y_data = top10_df["Total Cost"]

# Print the resulting DataFrame
# print(top10_df)

# plt.figure(figsize=(10,6))
# sns.barplot(x= x_data, y= y_data, data=top10_df, orient="h")
# plt.title("Top 10countries with highest cost price")
# plt.xlabel("Country")
# plt.ylabel("Total cost")
# plt.show()


#Year with most sales

# year_sales = df.groupby("Year")["Cost"].sum()

# #Creating a dataframe
# year_df = year_sales.reset_index()

# Assigning values to the column
# year_df.columns = ['Year', 'Total Sales']
# x_data = year_df["Year"]
# y_data = year_df["Total Sales"]
# # print(year_df)

# plt.figure(figsize=(6,4))
# bar_plot = sns.barplot(x=x_data, y=y_data, data=df, color="Orange")
# plt.xlabel("Year")
# plt.ylabel("Total Sales")
# plt.title("Total Sales by Year")

# Adding labels on top of each bar
# for index, value in enumerate(y_data):
#     bar_plot.text(index, value, f'{value / 1e6:,.2f}M', ha='center', va='bottom')

# # Add annotation text to indicate the values are in millions
# plt.text(x=len(x_data) - 1, y=max(y_data), s='Values in Millions', 
#          ha='right', va='top', fontsize=12, color='black')

# plt.show()

#Sales in every month

# month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
# sales_by_month = df.groupby("Month_name_year_wise")["Cost"].sum()
# sorted_sales_by_month = sales_by_month.reindex(month_order)

# sns.barplot(x=sorted_sales_by_month.index,y=sorted_sales_by_month.values, color="Brown")
# plt.title("Sales by month")
# plt.xticks(rotation =  45)
# plt.xlabel("Months")
# plt.ylabel("Sales")
# plt.show()

#Sales in week

# weeks = ['Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
# week_sales = df.groupby("Day_name")["Cost"].sum()
# sorted_week_sales = week_sales.reindex(weeks)

# sns.lineplot(x=sorted_week_sales.index, y=sorted_week_sales.values, color="LightGreen", marker="*")
# plt.title("Sales in week")
# plt.xticks(rotation = 45)
# plt.xlabel("Weeks")
# plt.ylabel("Sales")
# plt.show()

#'Countries which used retail shopping more'

# country_counts = df["Country"].value_counts()
# # print(country_counts)
# df= pd.DataFrame(country_counts)
# plt.figure(figsize=(10,6))
# sns.barplot(data=country_counts, orient="h")
# plt.xlabel('Count')
# plt.ylabel('Countries')
# plt.xticks(rotation = 90)
# plt.title('Countries which used retail shopping more')
# plt.tight_layout()
# plt.show()


#Highest number stock codes present in description

# stocks =  df["StockCode"].value_counts()
# print(a)

# stock_code = df.groupby("Description")["StockCode"].value_counts()
# sorting = stock_code.sort_values(ascending=False)
# top_10_stock_codes = sorting.head(10)

# top_df = top_10_stock_codes.reset_index()
# top_df.columns = ["Product", "Codes", "Total"]
# x_data = top_df["Codes"]
# y_data = top_df["Total"]
# z_data = top_df["Product"]
# print(top_10_stock_codes)  #In panda series
# print(top_df)              #Not in pandas series. Its in column

# plt.figure(figsize=(13,8))
# sns.barplot(x=x_data, y=y_data, hue=z_data, palette = "viridis")
# plt.title("Highest number StockCodes present in Description")
# plt.xlabel("Description")
# plt.ylabel("Total number of StockCodes")
# plt.show()


# Top 10 Description by maxmimum quantity

# Description = df.groupby("Description")["Quantity"].max()
# sorted = Description.sort_values(ascending=False).head(10)  #used to find the top 10 highest quantities for each unique description in your DataFrame.
# top_10_df = sorted.reset_index()
# top_10_df.columns = ["Product", "Quantities count"]
# top_10_df["Product"] = top_10_df["Product"].str.upper()
# x_data = top_10_df["Product"]
# y_data = top_10_df["Quantities count"]


# print(top_10_df)

# top_10_df.set_index('Product')['Quantities count'].plot(kind='pie', autopct='%1.1f%%', figsize=(8, 8), title='Top 10 Highest Quantities')
# plt.show()


#Finding how many quantities count in Description

# quantity = df.groupby("Description")["Quantity"].value_counts().head(30)
# # print(quantity)

# top_10_df = quantity.reset_index()
# top_10_df.columns = ["Products", "Quantities", "Q_Count"]
# x_data = top_10_df["Products"]
# y_data = top_10_df["Quantities"]
# z_data = top_10_df["Q_Count"]
# # print(top_10_df)
# sns.violinplot(x=x_data,y=z_data)
# plt.xticks(rotation=45)
# plt.title("Finding how many quantities count in Description")
# plt.show()

# First 10 Unit price with most counts

# unit_price = df["UnitPrice"].value_counts().head(10)
# # unit_price.name = "Quantities_Count"
# # print(unit_price)

# colors = ['red', 'green', 'blue', 'pink', 'black', 'grey', 'yellow', 'cyan', 'brown', 'purple']
# df_1 = unit_price.reset_index()
# df_1.columns = ['Price', 'Total']
# x_data = df_1['Price']
# y_data = df_1['Total']
# # print(df_1)
# plt.scatter(x=x_data, y=y_data, c=colors, marker='D')
# plt.title("First 10 Unit price with most counts")
# plt.xlabel("Unit_Price")
# plt.ylabel("Unit_counts")
# plt.show()