import pandas as pd

customers = {
    'CustomerID': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],

}
customers_df = pd.DataFrame(customers)

orders = {
    'OrderID': [101, 102, 103, 104, 105],
    'CustomerID': [1, 2, 3, 6, 7],
    'Product': ['Laptop', 'Phone', 'Tablet', 'Monitor', 'Keyboard'],    
    'Amount': [1200, 800, 600, 300, 150]
}

orders_df = pd.DataFrame(orders)

# Merge the DataFrames on 'CustomerID'
merged_df_inner = pd.merge(customers_df, orders_df, on='CustomerID', how='inner')
print("Inner Join:")
print(merged_df_inner)

merged_df_outer = pd.merge(customers_df, orders_df, on='CustomerID', how='outer')
print("outer Join:")
print(merged_df_outer)

merged_df_left = pd.merge(customers_df, orders_df, on='CustomerID', how='left')
print("left join:")
print(merged_df_left)

merged_df_right = pd.merge(customers_df, orders_df, on='CustomerID', how='right')
print("right join:")
print(merged_df_right)

merged_df_cross = pd.merge(customers_df, orders_df,  how='cross')
print("cross join:")
print(merged_df_cross)


df_concatenated = pd.concat([customers_df, orders_df], axis=0, ignore_index=True)
print("Concatenated DataFrame:")    
print(df_concatenated)

df_concatenated_horizintal = pd.concat([customers_df, orders_df], axis=1, ignore_index=True)
print("Concatenated DataFrame:")    
print(df_concatenated_horizintal)