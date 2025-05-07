keys = ['Ten', 'Twenty', 'Thirty']
keys1 = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]


# my_dict = zip(keys, values)
# my_dict = dict(zip(keys, keys1, values))

for key,value, value2 in zip(keys, keys1, values):
    print(key, '', value)

# for item in zip(keys, values):
#     print(item)

# print(my_dict)
