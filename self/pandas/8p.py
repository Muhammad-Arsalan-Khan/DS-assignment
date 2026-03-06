import pandas as pd
import numpy as np

# sorting aggregation 

data = {
    "emp_id": [0, 1, 2, 3, 4, 5, 6],
    "Name": ["Charlie","Alice", "Bob", "abbas", "ali", "usman", "mazhar"],
    "Age": [25, 30, 42, 22, 28, 35, 40],
    "City": ["New York", "Los Angeles", "peshawar", "Karachi", "Lahore", "Islamabad", "Multan"],    
    "Occupation": ["Engineer", "Doctor", "Artist", "Teacher", "Lawyer", "Nurse", "Scientist"],
    "Salary": [100000, 126000.0, 52500.0, 45000.0, 60000.0, 75000.0, 90000.0],      
    "bonus": [7000.0, 40000, 5000.0, 3000.0, 4000.0, 6000.0, 8000.0],          
    "Department": ["IT", "Lab", "HR", "Education", "Legal", "Healthcare", "Research"],
    "yearly_bonus": [3500.0, 6000.0, 30000, 2000.0, 3000.0, 5000.0, 7000.0]
}

df = pd.DataFrame(data)
print(df)
print("-------------------------------------------------------------------")

# sorting by name in ascending order
sorted_df = df.sort_values(by='Age', ascending=False)
print(sorted_df)

# df.sort_values(by='Name', ascending=True ,inplace=True) 
# print(df)

sorted_df_two_col = df.sort_values(by=['Age', 'Salary'], ascending=[True, False])
print(sorted_df_two_col)













