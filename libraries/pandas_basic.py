# import pandas library with alias pd
import pandas as pd

"""
Pandas has many reading functions available, including
1. read_csv
2. read_excel
3. read_json
4. read_html
5. read_sql
6. read_xml
and many more.

Different files can be read by pandas, and stored as data frame for analysis, answering questions, exploring data set etc.

For our example, we are reading a csv file, hence the read_csv function.
The read function aceept a file path. We will store the file in a data frame variable named df.
"""
df = pd.read_csv('libraries/train.csv')


"""
df.head(). prints first 5 rows by default. df.head(n) prints first n rows.
df.tail(). prints last 5 rows by default. df.tail(n) prints last n rows.
"""
print(df.head(2))

print(df.tail(3))


"""
To view the summary of the data frame, use the info() function.
it shows, number of columns, column names, non-null value count, data types and memory usage.
lets run it.
""" 
print(df.info())


"""
The describe function displays the stats summary, including mean, std, count, quartiles (25, 50 & 75).
"""
print(df.describe())


# returns list of column names
print(df.columns)


# returns shape, ( no. of rows, no. of columns )
print(df.shape)

