import pandas as pd

data = {
    'Name': ['Arsalan', 'Asim', 'mazhar', 'Usman'],
    'Age': [21, 20, 19, 21],
    'occupation': ['eng', 'bus', 'bus', 'doctor'],
    'salary': [10000, 20000, 30000, 40000]
}

df = pd.DataFrame(data)
print(df)

avg = df['salary'].mean()
print('avg',avg)
print('max', df['salary'].max())
print('min', df['salary'].min())
print('count', df['salary'].count())
print('sum', df['salary'].sum())
print('std', df['salary'].std())


#  grouping data
group = df.groupby('occupation')['occupation'].count()
print(group)

group2 = df.groupby('Age')['salary'].sum()
print(group2)

group4 = df.groupby('Age')['salary'].mean()
group3 = df.groupby('Age')['salary'].std()
print(group3)
print(group4)

multiple_group = df.groupby(['occupation', 'Age'])['salary'].mean()
print(multiple_group)

