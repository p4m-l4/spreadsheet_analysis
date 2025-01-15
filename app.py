
#Before running the file run these commands in your pycharm terminal
#pip install matplotlib

#Issues we faced:
#pycharm - pip command not working as version number not installed (needed pip3)
#needed to install pandas and matplotlib + openpyxl
#replit only allowed two members (one contributor)
#github issue - cloning project to pycharm and pushing project to github so we could all contribute
#hi

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
print(df.info())

# print('Answer 2(a)')
# print(sales_by_month)
# print('Answer 2(b)')
# print(sales_by_month_dict)
print('Answer 2(c)')
print(sales_by_month_list)
print('Answer 3')
print(total_sales)
print(f"Findings exported to {output_file}")

# Display the chart
plt.show()