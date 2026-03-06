# part 2

import pandas as pd
import numpy as np

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 40],    
    "City": ["New York", "Los Angeles", "Chicago"],
    "Occupation": ["Engineer", "Doctor", "Artist"],
    "Salary": [70000, 120000, 50000]
}

df = pd.DataFrame(data)
print(df)
print("-------------------------------------------------------------------")

# agar mujha farq ni parta ho ky colum kaha add ho raha hain tu ya use karo ga ya last main add kar dega 
df['bonus'] = df['Salary'] * .1

print(df)
print("-------------------------------------------------------------------")

# agar mujah kisi specific jaha pr add karna hain 
# .insert(index,  "column_Name", value)
# df.shape[0] == row count ko return karta hain
df.insert(0, "emp_id", np.arange(0, df.shape[0]))  # emp_id column ko 0 index pr add kar dega
print(df)
print("-------------------------------------------------------------------")

# update
# df.loc[row_index, column_name] = new_value
df.loc[2, 'Age'] = 42
print(df)
print("-------------------------------------------------------------------")

# loc se agar koi column b exist ni karta hain tu wo column create kar dega aur usme value add kar dega
df.loc[0, 'Department'] = "IT"
print(df)
print("-------------------------------------------------------------------")

df.loc[np.arange(0, df.shape[0]), 'yearly_bonus'] = df['Salary'] * .05
print(df)
print("-------------------------------------------------------------------")

df['Salary'] = df['Salary'] * 1.05 # salary column ko update kar dega
print(df)

print("-------------------------------------------------------------------")
# bonus column ko drop kar dega inplace = true ka matlab hain ki original dataframe ko update kar dega
# df.drop(columns=['column1', 'column2', ------ , 'column_N'], inplace=True)
df.drop(columns=['bonus'], inplace=True)
print(df)

print("-------------------------------------------------------------------")
print(None == None)
print(None == np.nan)
print(np.nan == np.nan)

