import pandas as pd
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s)

# Access elements
print(s['a']) 

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['Delhi', 'Mumbai', 'Chennai']
}

df = pd.DataFrame(data)
print(df)