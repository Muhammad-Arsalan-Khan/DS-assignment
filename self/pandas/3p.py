import pandas as pd
import numpy as np

# data framing

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, np.nan],    
    "City": ["New York", "Los Angeles", "Chicago"],
    "Occupation": ["Engineer", "Doctor", "Artist"],
    "Salary": [70000, 120000, np.nan]
}

# df = pd.DataFrame(data)
# df = pd.DataFrame(data, index=["Row1", "Row2", "Row3"])
# df = pd.DataFrame(data, columns=["Salary" ,"Name", "Age", "City", "Occupation"])
df = pd.DataFrame(data)
print(df)

# data convert to csv, json, excel
df.to_csv("data/outputCsv.csv", index=False)
df.to_excel("outputExcel.xlsx", index=False)
df.to_json("outputJson.json", orient="records")
# df.to_json("outputJson.json", orient="records", lines=True) line = true means each record will be written on a separate line in the JSON file, making it easier to read and process large datasets.

print(df.info())