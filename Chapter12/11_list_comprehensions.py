#List comprehensions is an elegant way to create lists based on existing lists.

myList = [1, 2, 9, 5, 3, 5]

# squaredList = []
# for item in myList:
#     squaredList.append(item*item)

#Using list comprehensions
squaredList = [i*i for i in myList]

print(squaredList)