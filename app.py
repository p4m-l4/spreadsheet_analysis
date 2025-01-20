
#Before running the file run these commands in your pycharm terminal
#pip install matplotlib

#Issues we faced:
#pycharm - pip command not working as version number not installed (needed pip3)
#needed to install pandas and matplotlib + openpyxl
#replit only allowed two members (one contributor)
#github issue - cloning project to pycharm and pushing project to github so we could all contribute

import pandas as pd
import matplotlib.pyplot as plt
import openpyxl.workbook

# 1. Read the data from the spreadsheet
input_file = "sales.csv"  # Replace with your file name
df = pd.read_csv(input_file)

# 2. Collect all of the sales from each month into a single list
sales_by_month_list = df['sales'].to_list()
sales_by_month = df.groupby('month')['sales'].apply(list).reset_index()

# Convert the result to a dictionary if needed
sales_by_month_dict = sales_by_month.to_dict()

# 3. Output the total sales across all months
total_sales = df['sales'].sum()

# Calculate average sales
average_sales =df['sales']. mean()
# Monthly Sales as Percentage of Total Sales.
df['Sales Percentage (%)'] = (df['sales'] / total_sales) * 100
print("\nMonthly Sales Percentage:")
print(df[['month', 'Sales Percentage (%)']])
# Percentage of changes per month
df['Monthly Change (%)'] =df['sales']. pct_change() * 100
print("\nMonthly Sales Changes Percentage:")
print(df[['month', 'Monthly Change (%)']])
# Identify the months with the highest and lowest sales
highest_sales = df.loc[df['sales'].idxmax()]
lowest_sales = df.loc[df['sales'].idxmin()]


# Prepare findings for export
findings = pd.DataFrame({
    'Metric': ['Sales by Month', 'Total Sales'],
    'Details': [str(sales_by_month['sales'].tolist()), total_sales]
})

# Save findings to an Excel file
output_file = "sales_findings.xlsx"
findings.to_excel(output_file, index=False)

# Create a bar chart for sales by month
plt.figure(figsize=(10, 6))
plt.bar(df['month'], df['sales'], color='skyblue')
plt.title('Sales by Month (2018)', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Sales', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

# Save the chart as an image
chart_file = "sales_by_month_chart.png"
plt.savefig(chart_file)

print('Read the sales data file')
print('Read the sales data file:{}'.format(df.info()))

# print('Answer 2(a)')
# print(sales_by_month)
# print('Answer 2(c)')
print('Sales for each month in a list: {}'.format(sales_by_month_list))
# print('Answer 3')
print('Total sales in a month:{}'.format(total_sales))
# Print the summary

# print("Sales Analysis Summary:\n")
print(f"Average Sales: {average_sales:.2f}")
print(f"Month with Highest Sales: {highest_sales['month']} ({highest_sales['sales']})")
print(f"Month with Lowest Sales: {lowest_sales['month']} ({lowest_sales['sales']})")
print(f"Findings exported to {output_file}")

# Display the chart
plt.show()




