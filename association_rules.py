# -*- coding: utf-8 -*-
"""Association Rules.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14api11xZ-Ibz6-3126la1G0jJBmtrnaW
"""

import pandas as pd

from mlxtend.frequent_patterns import apriori,association_rules
from mlxtend.preprocessing import TransactionEncoder

from google.colab import drive
drive.mount('/content/drive')

file_name="/content/Titanic csv.csv"

titanic = pd.read_csv("/content/Titanic csv.csv")
titanic

"""Pre-Processing"""

df=pd.get_dummies(titanic)
df.head()

frequent_itemsets = apriori(df, min_support=0.1,use_colnames=True)
frequent_itemsets

rules=association_rules(frequent_itemsets, metric="lift",min_threshold=0.7)
rules

rules.sort_values('lift',ascending = False)[0:20]

