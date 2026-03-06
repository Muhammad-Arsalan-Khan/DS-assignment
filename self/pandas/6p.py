import pandas as pd
import numpy as np

data = {
    "emp_id": [0, 1, 2],
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 42],
    "City": ["New York", "Los Angeles", None],    
    "Occupation": ["Engineer", "Doctor", "Artist"],
    "Salary": [np.inf, 126000.0, 52500.0],      
    "bonus": [7000.0, -np.inf, 5000.0],          
    "Department": ["IT", None, None],
    "yearly_bonus": [3500.0, 6000.0, np.nan]     
}

df = pd.DataFrame(data)
print(df)
print("-------------------------------------------------------------------")

print(df.isnull())  # check for null values in the DataFrame
print("-------------------------------------------------------------------")


print(df.isnull().sum())  # count of null values in each column
print("-------------------------------------------------------------------")

# handling missing values
# agar mane yaha inplace true use kiya tu df update hoga ab os main 1 row he hogi jis ki waja se dropna axis 1 pr b same output aye ga
# df.dropna(axis=0, inplace= True) original main change
df_clean = df.dropna(axis=0)  # drop rows with any null values  
print(df_clean) 
print("-------------------------------------------------------------------")
# df.dropna(axis=1, inplace= True) # original main change
df_clean2 = df.dropna(axis=1)  # drop columns with any null values
print(df_clean2)  # ye b dekh sakte hain ki konsa column drop hua hain jis main null value thi

print("-------------------------------------------------------------------")
df.dropna(inplace=True)  # drop rows with any null values
print(df)
