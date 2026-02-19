import pandas as pd
import matplotlib.pyplot as plt

# 1. Create a sample dataset (Simulating loading a CSV)
data = {
    'Date': ['2025-01-01', '2025-01-15', '2025-02-01', '2025-02-10', '2025-03-05', '2025-03-20'],
    'Product': ['Laptop', 'Mouse', 'Laptop', 'Monitor', 'Mouse', 'Monitor'],
    'Category': ['Electronics', 'Accessories', 'Electronics', 'Electronics', 'Accessories', 'Electronics'],
    'Sales': [1200, 50, 1200, 300, 45, 320]
}
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# 2. Grouping Data
category_totals = df.groupby('Category')['Sales'].sum()
monthly_trends = df.groupby(df['Date'].dt.strftime('%B'))['Sales'].sum()

# 3. Printing Insights
print("--- Sales by Category ---")
print(category_totals)
print("\n--- Monthly Revenue ---")
print(monthly_trends)

# 4. Plotting
category_totals.plot(kind='pie', autopct='%1.1f%%', startangle=140, title='Revenue Share by Category')
plt.ylabel('') # Hides the 'Sales' label on the side
plt.show()
