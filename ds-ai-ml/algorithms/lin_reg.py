import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_csv('ds-ai-ml/lin_reg.csv')

lin_reg = linear_model.LinearRegression()

lin_reg.fit(df[['area']], df.price)

# predict price of a specific area
print(f"Automatically Calculated: {lin_reg.predict([[3000]])}")

# since linear regression uses y= mx + c . so lets manually perform these and check if calculations are correct.

# get value of m
m = lin_reg.coef_

# get value of c
c = lin_reg.intercept_

x = 3000

y = m * x + c

print(f"Manually Calculated: {y}")

plt.scatter(df.area, df.price)
plt.xlabel('Area')
plt.ylabel('Price')
plt.plot(df.area, lin_reg.predict(df[['area']]), color='green')
plt.show()

