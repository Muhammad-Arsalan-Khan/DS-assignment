import pandas as pd
# data reading 
# .head() defaultly starting 5 rows show karta hai
# .tail() defaultly last 5 rows show karta hai
# .head(n) tail(n) n rows show karta hai
# .describe() summary statistics show karta hai 
# .groupby() data ko group karta hai based on a specific column and calculate the mean of each group
# .loc[] specific rows and columns ko access karta hai based on labels
# .iloc[] specific rows and columns ko access karta hai based on integer position
# .to_csv() data ko csv file me convert karta hai
# .to_excel() data ko excel file me convert karta hai
# .to_json() data ko json file me convert karta hai

data = pd.read_csv("data/sales_data_sample.csv", encoding="latin1")
print(data.head())
print(data.tail())
print(data.head(7))
print(data.tail(7))


# info
print(data.info()) #info method se ya sari information mil jati hain 
# number of row and column
# column names
# data types of each column
# memory usage of the DataFrame
# non null values in each column

print(data.info())

# decscribe
print(data.describe())

# shape columns and rows count
print(data.shape)
print("Rows:", data.shape[0])  # asa b row count kar sakte hain
print("Columns:", data.shape[1]) # asa b column count kar sakte hain
print(data.columns)


# filtering on row with condition or multiply condition 
# select a column select multiply column
# selecting columns
# 1- a series
# 2- dataframe multiple columns of data
# column = df ["Column Name"]
# subset = df["olumn1","Column2"," ... "]
# filtering rows
# boolean indexing
#based on a single condition
# filtered_Rows = df[df["Salary"] > 50000]
#combine multiple conditions
# filtered_Rows = df[(df["Column"] > value) & (df["Column2] < 80000)]

# # select single column
print('----------')
print(data["SALES"])
# # select multiply
print('----------')
print(data[["SALES","STATE"]])

# or agar sath row WISE b chahiya 
# # df.loc[row_label, column_name]
print('----------')
print(data.loc[3, "SALES"])  #row 3
print('----------')
print(data.loc[0, "SALES"])  #row 0
print('----------')
print(data.loc[0:10, "SALES"]) # row 0 to 10   print(data.loc[:10, "SALES"])---> same 
print('----------')

# df.iloc[row_index, column_index]
print(data.iloc[5:7])  ##5 se 11 row column dono
print('----------')
print(data.iloc[5:11, [4, 18]]) 
print('----------')  ##5 se 11 ki row or column 4 or 18 
print(data.iloc[5:11, [4, 18, 6]])   ##5 se 11 ki row or column 4 or 18 or 6
print('----------')
QUANTITYORDERED25plus = data[data["QUANTITYORDERED"]>25]
print(QUANTITYORDERED25plus)
print('----------')

QUANTITYORDERED25plusUnder30 = data[(data["QUANTITYORDERED"]>25) & (data["QUANTITYORDERED"]<30)]
print(QUANTITYORDERED25plusUnder30)

