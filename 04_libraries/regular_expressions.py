# regular expressions
# regular expressions are also used in preprocessing tasks to filter out textual data.

import re

courses = ["artificial intelligence", "data mining", "database", "data structures"]

data_list= []

# among course lits, find course matching specific patterns
for course in courses:
    res = re.findall("data", course)
    if res:
        data_list.append(course)


print(data_list)
