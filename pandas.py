import pandas as pd


"Creating a pandas dataframe"

data = {
    'Name': ['Tom', 'nick', 'krish', 'jack'],
    'Age': [20, 21, 19, 18]
}

df = pd.DataFrame(data)
print(df)