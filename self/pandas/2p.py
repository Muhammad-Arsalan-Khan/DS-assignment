# read data from a CSV file
import pandas as pd 
data = pd.read_csv("data/sales_data_sample.csv", encoding="latin1")
# print(data)

data2 = pd.read_excel("data/Book1.xlsx", engine="openpyxl")
# print(data2)

data3 = pd.read_json("data/sample_Data.json")
print(data3)


# ya bad main parho ga 

# display the first 5 rows of the DataFrame
print(data.head())
# # display summary statistics of the DataFrame
print(data.describe())
# # filter rows where a specific column's value is greater than a threshold
# filtered_data = data[data['column_name'] > threshold]
# print(filtered_data)    
# # group data by a specific column and calculate the mean of each group
# grouped_data = data.groupby('group_column').mean()
# print(grouped_data)
