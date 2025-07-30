import re

courses = ["artificial intelligence", "data mining", "database", "data structures"]

data_list= []

for course in courses:
    res = re.findall("data", course)
    if res:
        data_list.append(course)


print(data_list)
