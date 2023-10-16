import pandas as pd
import matplotlib.pyplot as plt

# a fix to increase chunk size in order to avoid exceeded cell block limit error
plt.rcParams['agg.path.chunksize'] = 10000

# 1: Find the store with the maximum sale recorded
# Read CSV files
store_df = pd.read_csv('store.csv')
train_df = pd.read_csv('train.csv')

# Merge store and train DataFrames
merged_df = train_df.merge(store_df, on='Store')

# Find Maximum Sale
max_sale_index = merged_df['Sales'].idxmax()

# Extract and Print Information
max_sale_store_id = merged_df.at[max_sale_index, 'Store']
max_sale_date = merged_df.at[max_sale_index, 'Date']
max_sale_value = merged_df.at[max_sale_index, 'Sales']

print("Task 1: Store with the maximum sale recorded")
print(f"Store ID: {max_sale_store_id}")
print(f"Date: {max_sale_date}")
print(f"Sales: {max_sale_value}\n")

# 2: Find the store(s) with the least and maximum competition distances
store_df = pd.read_csv('store.csv')

# Find the store(s) with the least competition distance
store_with_least_competition = store_df[store_df['CompetitionDistance'] == store_df['CompetitionDistance'].min()]
print("Task 2: Store(s) with the least competition distance")
print(store_with_least_competition[['Store', 'CompetitionDistance']])

# Find the store(s) with the maximum competition distance
store_with_maximum_competition = store_df[store_df['CompetitionDistance'] == store_df['CompetitionDistance'].max()]
print("\nTask 2: Store(s) with the maximum competition distance")
print(store_with_maximum_competition[['Store', 'CompetitionDistance']])

# 3: Check for missing values and output the number of missing values per column
missing_values = merged_df.isnull().sum()
print("\nTask 3: Number of missing values per column")
print(missing_values)

# 4: Plot the monthly mean of sales across all stores
# Convert the date to a datetime object
merged_df['Date'] = pd.to_datetime(merged_df['Date'])

# Group by month and calculate the mean sales
monthly_mean_sales = merged_df.groupby(merged_df['Date'].dt.strftime('%Y-%m'))['Sales'].mean()

# Plot the monthly mean sales
plt.figure(figsize=(10, 6))
monthly_mean_sales.plot(kind='bar', color='green')
plt.xlabel('Month')
plt.ylabel('Monthly Mean Sales')
plt.title('Monthly Mean Sales Across All Stores')
plt.xticks(rotation=50)
plt.grid(True)

# 5: Find which store type ('a', 'b', etc.) has had the most sales
store_type_sales = merged_df.groupby('StoreType')['Sales'].sum().idxmax()
print("\nTask 5: Store type with the most sales")
print(f"Store Type: {store_type_sales}")

# 6: Calculate the difference in the mean of sales with and without Promo
mean_sales_with_promo = merged_df[merged_df['Promo'] == 1]['Sales'].mean()
mean_sales_without_promo = merged_df[merged_df['Promo'] == 0]['Sales'].mean()
difference_in_mean_sales = mean_sales_with_promo - mean_sales_without_promo

# Plot the difference in mean sales
promo_labels = ['With Promo', 'Without Promo']
promo_values = [mean_sales_with_promo, mean_sales_without_promo]
plt.figure(figsize=(10, 6))
plt.bar(promo_labels, promo_values, color=['blue', 'yellow'])
plt.xlabel('Promo')
plt.ylabel('Mean Sales')
plt.title('Difference in Mean Sales (Promo vs. No Promo)')
plt.grid(True)

# 7: Plot the mean sales per day of the week for Store_ID 1 in a pie chart
store_id_1 = merged_df[merged_df['Store'] == 1]
mean_sales_per_day_store_1 = store_id_1.groupby('DayOfWeek')['Sales'].mean()
day_labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
plt.figure(figsize=(8, 6))
plt.pie(mean_sales_per_day_store_1, labels=day_labels, autopct='%1.1f%%', startangle=140)
plt.title('Mean Sales per Day of the Week for Store ID 1')
plt.axis('equal')
plt.grid(True)

# 8: Plot the mean sales per day of the week across all stores
mean_sales_per_day_all_stores = merged_df.groupby('DayOfWeek')['Sales'].mean()
plt.figure(figsize=(8, 6))
mean_sales_per_day_all_stores.plot(kind='bar', color='green')
plt.xlabel('Day of the Week')
plt.ylabel('Mean Sales')
plt.title('Mean Sales per Day of the Week Across All Stores')
plt.xticks(rotation=0)
plt.grid(True)

# Task 9: Draw boxplots of sales for the first 10 stores
first_10_store_ids = merged_df['Store'].unique()[:10]
sales_data_first_10_stores = [merged_df[merged_df['Store'] == store_id]['Sales'] for store_id in first_10_store_ids]
plt.figure(figsize=(10, 6))
plt.boxplot(sales_data_first_10_stores, labels=first_10_store_ids)
plt.xlabel('Store ID')
plt.ylabel('Sales')
plt.title('Boxplots of Sales for the First 10 Stores')
plt.grid(True)

plt.show()
