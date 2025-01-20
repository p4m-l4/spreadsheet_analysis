# Project Name  : Spreadsheet Analysis
# Created on    : 09/01/2025
# Definition    : Using Python to do very basic data analysis on a spreadsheet.

#Before running the file run these commands in your pycharm terminal
#pip install matplotlib pandas

import pandas as pd
import matplotlib.pyplot as plt
import openpyxl.workbook

# 1. Read the data from the spreadsheet
input_file = "sales.csv"  # Replace with your file name
df = pd.read_csv(input_file)

# 2. Collect all of the sales from each month into a single list
sales_by_month_list = df['sales'].to_list()

# 3. Output the total sales across all months
total_sales = df['sales'].sum()

# Calculate average sales
average_sales =df['sales']. mean()

# Monthly Sales as Percentage of Total Sales.
df['Sales Percentage (%)'] = ((df['sales'] / total_sales) * 100).round(2)

# Percentage of changes per month
df['Monthly Change (%)'] =(df['sales']. pct_change() * 100).round(2)

# Identify the months with the highest and lowest sales
highest_sales = df.loc[df['sales'].idxmax()]
lowest_sales = df.loc[df['sales'].idxmin()]


# Create a bar chart for sales by month
plt.figure(figsize=(10, 6))
plt.bar(df['month'], df['sales'], color='pink')
plt.title('Sales by Month (2018)', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Sales', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

# Save the chart as an image
chart_file = "sales_by_month_chart.png"
plt.savefig(chart_file)

print('Read the sales data file')
print('\nRead the sales data file:{}'.format(df.info()))

# Answer 2(c)
print('\nSales for each month in a list: {}'.format(sales_by_month_list))
# Answer 3
print('\nTotal sales in a month:{}'.format(total_sales))

# Sales Analysis Summary
print(f"\nAverage Sales: {average_sales:.0f}")
print(f"\nMonth with Highest Sales: {highest_sales['month']} ({highest_sales['sales']})")
print(f"\nMonth with Lowest Sales: {lowest_sales['month']} ({lowest_sales['sales']})")
# print(f"\nFindings exported to {output_file}")

print("\nMonthly Sales Percentage:")
print(df[['month', 'Sales Percentage (%)']])


# Display the chart
plt.show()




# Prepare findings for export
# findings = pd.DataFrame({
#     'Metric': ['Sales by Month', 'Total Sales'],
#     'Details': [str(sales_by_month_list['sales'].tolist()), total_sales]
# })

# Save findings to an Excel file
# output_file = "sales_findings.xlsx"
# findings.to_excel(output_file, index=False)





