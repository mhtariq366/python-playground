import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_csv('ds-ai-ml/lin_reg.csv')

lin_reg = linear_model.LinearRegression()

lin_reg.fit(df[['area']], df.price)

# predict price of a specific area
print(lin_reg.predict([[3000]]))


