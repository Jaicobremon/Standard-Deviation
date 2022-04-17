from pandas.core.common import standardize_mapping

import csv
import pandas as pd
import math


df = pd.read_csv("data2.csv")

data = df["Marks"].tolist()

n = len(data)


def mean(data):

  total = 0

  for x in data:
    total += int(x)
  
  mean = total/n

  return mean

squared_list = []

for number in data:
  a = int(number) - mean(data)
  a = a**2
  squared_list.append(a)

sum = 0

for i in squared_list:
  sum = sum + i 

n = len(data)
result = sum/n

standardDeviation = math.sqrt(result)

print(standardDeviation)
print(n)


