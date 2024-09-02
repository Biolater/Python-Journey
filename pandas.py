# -*- coding: utf-8 -*-
"""Pandas.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rAJMi_Ohr5nF9QiMSNflD323IP2gMk4w

Importing pandas
"""

import pandas as pd

from sklearn.datasets import load_iris

iris_dataset = load_iris()

print(iris_dataset)

type(iris_dataset.data)

iris_df = pd.DataFrame(iris_dataset.data, columns=iris_dataset.feature_names)

iris_df.head()

iris_df.shape

"""From csv to pandas df"""

diabetes_df = pd.read_csv("/content/diabetes.csv")

diabetes_df.head()

diabetes_df.info()

diabetes_df.describe()

"""Loading the data from excel file to a pandas DataFrame



```
# This is formatted as code
pd.read_excel("file_path")
```

Exporting a DataFrame to a csv file
"""

iris_df.to_csv("iris_dataset.csv")

iris_df_csv = pd.read_csv("iris_dataset.csv")

iris_df_csv.head()

