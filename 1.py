# print('hello World');

# if(5 > 2):
#  print("5  greater than 2 ");

# x = 10;
# y = 10;
# print(x + y);

# number types

# x = 10;
# y = 10.10;
# z = 5j
# print(type(x));# int
# print(type(y));# float
# print(type(z));# complex

#casting

# x = int(1)
# y = int(1.0)
# z = int("10")
# print(x)
# print(y)
# print(z)


# x = float(1)
# y = float(1.0)
# z = float("10")
# print(x)
# print(y)
# print(z)


# x = str(1)
# y = str(1.0)
# z = str("10")
# print(x)
# print(y)
# print(type(z))

# python string
# a = ' I AM GOVARDHAN   ' 
# print(a[0])
# print(a[0:8])
# print(a)
# x = a.strip()
# print(len(x))
# print(len(a))
# print(x.lower())
# print(x.upper())
# print(x.replace('GOVARDHAN','GOA'))
# b = x.split(",")
# print(b)

# operators
# a = 2.5
# b = 2
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a % b)
# print(a == b)
# print(a != b)
# print( a < b)
# print(a > b)
# print( a <= b)
# print(a >= b)
# print( a > 2  and a < 2)
# print( a > 2  or a < 2)
# print not( a > 2  and a < 2)
# a = ['1','2']
# b = ['1','2']
# c = a
# print(a is b)
# print( a is c)
# print(c is a)
# print(b is c)
# print('3' not in a)
# print('3' in a)

# list of array

# a = ['1','2','3']
# print(a)
# print(a[0])
# a[1] = 'hii'
# print(a)
# for x in a:
#   print(x)
# if '1' in a:
#     print('1 in a')
# print(len(a))
# a.append('hii')
# print(a)
# a.insert(1,'gova')
# print(a)
# a.remove('hii')
# print(a)
# a.pop(1)
# print(a)
# del a[0]
# print(a)
# a.clear()
# print(a)
#  a = list(('1','2','3'))
# print(a)
# a = ['apple', 'banana', 'cherry']

# # b = (1, 4, 5, 9)

# a.reverse()
# print(a)
# a.sort()
# print(a)

#tubles
# collection which is ordered and unchangeable. In Python tuples are written with round brackets.
# a = ('1','2','3')
# # # print(a)
# # # print(a[0])
# # a[1] = '4' // doesn't assign tuble
# # for i in a:
# #   print(i)
# # if '2' in a:
# #     print('yes it is in a')
# # print(len(a))
# b = (('1','2','3','1'))
# print(b)
# x = b.count('1')
# print(x)
# y = b.index('1')
# print(y)

# set
# collection of unordered and unindexed written in curely brackses

# a = {'1','2','3'}
# print(a)
# for x in a:
#     print(x)
# a.add('4')
# print(a)
# a.update(['apple','orange','kiwi'])
# print(a)
# print(len(a)
# a.remove('1')
# print(a)
# a.discard('2')
# print(a)
# a.discard('4')
# print(a)

# a.pop()
# print(a)
#del a
# a.clear()
# print(a)
# a = set(('1','2','3'))
# # print(a)
# # x = a.copy()
# # print(x)
# y = {'1','5','2','3'}
# # x = y.difference(a)
# # print(x)
# # z = a.difference_update(y)
# # print(a)
# # x = a.intersection(y)
# # # print(x)
# # z = a.intersection_update(y)
# # print(a)
# # x = a.isdisjoint(y)
# # print(x)
# x = a.issubset(y)
# print(x)
x = {'1','2','3'}
y = {'4','2' ,'1'}
# z = x.symmetric_difference(y)
# print(z)
# z = x.symmetric_difference_update(y)
# print(x)
# z = x.union(y)
# print(z)
# z = x.update(y)
# print(x)

# dicitionary
# dicitionary is unordered , changeable and indexed