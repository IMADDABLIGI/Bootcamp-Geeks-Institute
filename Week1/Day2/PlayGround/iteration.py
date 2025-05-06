# --------enumerate--------
# for item in enumerate('abcd'):
#     print(item)


# for (index_count, letter) in enumerate('abcd'):
#     print('At index {} the letter is {}'.format(index_count, letter))


# for letter in 'Leonardo':
#     if letter == 'a':
#         # continue
#         break
#     print(letter, end='') # end='' renders each letter next to the other


# -------ZIP-------
list1 = [1,2,3]
list2 = ['a','b','c']
list3 = [1.1, 2.2, 3.3, 4.4, 5.5]

for item in zip(list1, list2, list3): # only go as far it is possible
    print(item)


# (1, 'a', 1.1)
# (2, 'b', 2.2)
# (3, 'c', 3.3)
