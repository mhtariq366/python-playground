# Naive bayes using sklearn, pandas, and more.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv('ds-ai-ml/IMDB Dataset.csv')

# print(df.groupby('sentiment').describe())

df['label'] = df['sentiment'].apply(lambda x: 1 if 'positive' in x else 0)

# print(df.head())

train_x, test_x, train_y, test_y = train_test_split(df.review, df.label, test_size=0.2)

vect = CountVectorizer()
train_x_count = vect.fit_transform(train_x.values)

print(train_x_count.toarray()[45:50])
