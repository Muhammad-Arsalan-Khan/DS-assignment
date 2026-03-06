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



for column in df.columns:
    if df[column].dtype == "string" or df[column].dtype == "object":
        df[column] = df[column].fillna('Unknown')
    elif df[column].dtype in ['float64', 'int64']:
        df[column] = df[column].replace([np.inf, -np.inf], np.nan)
        df[column] = df[column].fillna(df[column].mean())

print(df)

data2 = {
    "stock" : [10, 20, None, 40, 50, None, None, 80, None, 100]
}

df2 = pd.DataFrame(data2)
print(df2)

# methods = ['linear', 'time', 'index', 'nearest', 'zero', 'slinear', 'quadratic', 'cubic']
df2['stock'] = df2.interpolate(method='linear')
print(df2)