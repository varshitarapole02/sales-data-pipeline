import pandas as pd

# Load data
df = pd.read_csv("sales_data.csv")

# Data Cleaning
df.dropna(inplace=True)

# Transformation
df['Total'] = df['Quantity'] * df['Price']

# Analysis
total_revenue = df['Total'].sum()
top_product = df.groupby('Product')['Total'].sum().idxmax()

print("Total Revenue:", total_revenue)
print("Top Product:", top_product)

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)