# Online-Retail-Sales
This project focuses on the Exploratory Data Analysis (EDA) of an online retail sales dataset. The goal is to uncover valuable insights from the data through various visualizations and analysis techniques. 
Key Visualizations and Findings
Step 1: Understanding the data.
Step2:  Data Collection – By reading the data set,
 df = pd.read_csv(“Online Retail.csv”)
Step3: Data Cleaning
1.	Using describe() to knowing mean, median, max, min, standard deviation of the datas.
2.	df.info() used to knowing the complete information of the column types and information.
3.	Using dtype() to knowing the data’s type.
4.	Using isnull().any() to find out any null values in the data set/
5.	After finding the null values, I want to know the total number of null values in data set.
6.	After knowing the total number of null values, have to delete the null values, dropna() used to remove those null values.
7.	After removing the null values, just want to clarify whether its deletes or not. So, once again using the isnull().sum().
8.	Using df[df["Quantity"] < 0]. We’ll know how many negative values are there. 
9.	The negative values maybe indicate return or refund. Have to convert those negative values by using df[“Quantity”].abs().
10.	Similarly, in Unitprice has also some negative values. The process is same as how the Quantity negative values are found and converted into positive values.
11.	Finding how many countries are repeated by using df[“Country’].values_count().
12.	After knowing the values count of countries, found some Unspecified name is mentioned in the data set. Deleting those unspecified value by df[df[“Country’] != “Unspecified”].
13.	Finding any duplicate values in df.duplicated().sum().
14.	After that, deleting the duplicates by using df.drop_duplicates(inplace=True).

#Visualization

1. Top 10 Customers by Quantity
Visualizing the top 10 customers in terms of the total quantity of products purchased. This analysis helps in identifying high-value customers and potential targets for loyalty programs or marketing campaigns.

2. Top 10 Product Descriptions
Displaying the 10 most popular product descriptions based on the total quantities sold. This helps businesses understand which products are the most in demand and can inform inventory stocking decisions.

3. Top 10 Countries by Quantity
A comparison of the top 10 countries based on the total quantity of items purchased, which provides insights into geographic regions where demand is highest.

4. Top 10 Countries with Highest Cost Price
Analyzing the countries that contribute the most to revenue by considering the cost price. This helps identify key markets where the business generates the most value.

5. Year with Most Sales
Examining the year with the highest sales figures, providing a historical perspective on the company's performance over time. This analysis can help track growth and identify seasonal trends.

6. Monthly Sales Analysis
A breakdown of sales across each month to understand the company's sales performance month-by-month. This helps identify periods of peak sales and can inform marketing and stocking strategies for high-demand seasons.

7. Weekly Sales Analysis
Visualizing sales on a weekly basis to uncover any patterns or trends in customer behavior during specific weeks of the year. This can highlight which weeks tend to generate more sales and may help inform future sales campaigns.

8. Countries with Highest Retail Shopping Usage
Identifying the countries where retail shopping is used most frequently, providing insights into potential expansion markets and customer preferences.

9. Highest Number of Stock Codes Present in Descriptions
Investigating the number of stock codes mentioned in product descriptions to analyze how they are being used across various products. This helps understand product variety and manage stock more efficiently.

10. Top 10 Descriptions by Maximum Quantity
Visualizing the top 10 product descriptions based on the maximum quantity of items sold. This helps in identifying fast-moving products and stock optimization.

11. Quantity Count in Descriptions
Analyzing how many quantities are associated with product descriptions to understand the relationship between product offerings and sales.

Tools and Libraries Used
Python: For data manipulation and analysis.
Pandas: For data cleaning and preprocessing.
Matplotlib & Seaborn: For data visualization.
