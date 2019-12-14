# divmod(5, 2)

# import decimal
# decimal.getcontext().prec=4
# a = decimal.Decimal(1)/decimal.Decimal(7)
# print(a)
#
# from fractions import Fraction
# Fraction(1,3)

# x = set('abcde')
# y = set('bdxyz')
# z = x.intersection(y)
# z.add('spam')
# z.update(set(['x', 'y']))
# z.remove('b')
# print(z)

# import string
#
# t = string.Template('$num=$title')
# t.substitute(num=7, title='string')
# print(t)

# L = list(range(-4, 4))
# len(L)
# for x in L : print(x, end=' ')
# L.append(4)
# L.extend([5, 6, 7])
# L.insert(2, 10)
# L.index(0)
# L.count(1)
# L.sort()
# L.reverse()
# L.pop(0)
# L.remove(5)
# del L[0]
# del L[0 :2]
# L[0 :2] = []
# L1 = [x ** 2 for x in range(5)]
# L2 = [pow(x, 2) for x in range(5)]
# print(L2)

# S = 'ABC'
# S = S[: :-1]
# print(S)
# print(type(S))
# S1 = list(map(abs, [-1, -2, 0, 1, 2]))
# print(S1)
#
# D = dict(name='Bob', age=40)
# D1 = dict([('name', 'Bob'), ('age', 40)])
# print('age' in D)
# D.keys()
# D.values()
# D.items()
# D.copy()
# D.clear()
# D.update(D1)
# D.get('age', 50)
# D.pop('year', 50)
# D.setdefault('age', 40)
# len(D)
# D['age'] = 42
# list(D.keys())
# D2 = {x : x ** 2 for x in range(10)}

# Matrix = {}
# Matrix[(2, 3, 4)] = 88
# Matrix[(7, 8, 9)] = 99
# try :
#     print(Matrix[2, 3, 6])
# except KeyError :
#     print(0)
#
# print(Matrix.get((2, 3, 4), 0))
# print(Matrix.get((2, 3, 6), 0))
# print(dict.fromkeys(['a', 'b'], 0))
# print({k : 0 for k in ['a', 'b']})
#
# D3 = dict(zip(['a', 'b', 'c'], [1, 2, 3]))
# D4 = {c.lower() : c + '!' for c in ['SPAM', 'EGGS']}
# print(D3, D4)

# D5 = dict(a=1, b=2, c=3)
# print(D5.keys())
# print(list(D5.keys()))
# print(list(D5.values()))
# print(list(D5.items()))
# for k in D5.keys() : print(k)
# for key in D5 : print(key)
# Ks = D5.keys()
# for k in Ks : print(k, D5[k])
# for k in sorted(D5) : print(k, D5[k])
# print('c' in D5)
# print(D5.get('c'))
# print(D5.get('x'))
# if D5.get('c') != None : print('present', D5['c'])

# import math
# num = 5
# print("{} is a number".format(num))
# print(math.floor(3.7))
# print(round(3.5))

# import csv
# import os
#
# print(os.getcwd())
# rdr = csv.reader(open('test.txt'))
# for row in rdr : print(row)

# input = open('test.txt', 'r')
# aString = input.readline()
# print(aString)
# aString1 = input.read(0)
# print(aString1)
# aList = input.readline()
# print(aList)
# input.close()

# input = open('test.txt', 'w')
# s1 = 'starbucks'
# input.write((s1+'\n')*3)
# input.close()

# import pickle
# help(pickle)

# import json

# with open('test.txt') as myfile:
#     for line in myfile:
#         print(line)

# D={}
# D[1]='a'
# D[2]='b'
# D[(1,2,3)]='c'
# print(D)

# file = open('test.txt')
# text = file.read()
# if 'star' in text:
#     print(text)
#
# file.close()

# a = 'a'
# print(a.isdigit())
# print(a.isalpha())
#
# a,b,c,d = 'spam'
# print(a)

# L = [1, 2, 3, 4]
# while L :
#     front, L = L[0], L[1 :]
#     print(front, L)
# while L :
#     front = L.pop(0)
#     print(front, L)
# while L:
#     front, *L = L
#     print(front, L)

# a, *b = 'spam'
# print(b)

# x = 'spam'
# y = 99
# z = ['egg']
# print(x,y,z)
# print(x,y,z, sep=',')
# print(x,y,z, end='!!\n')
# print(x,y,z,sep='...', file=open('test.txt', 'a'))
# print(open('test.txt').read())

# print('%s: %-.4f, %05d' % ('Result', 3.14159, 42))

# import sys
#
# temp = sys.stdout
# sys.stdout = open('test.txt', 'a')
# print(1, 2, 3)
# print('starbucks')
# print('add more...')
# sys.stdout.close()
# sys.stdout = temp
# print(open('test.txt').read())

# log = open('log.txt', 'w')
# print(1,2,3, file=log)
# print(4,5,6, file=log)
# print(7,8,9, file=log)
# log.close()
# print(open('log.txt').read())

# branch = {'spam' : 1.99,
#           'ham' : 0.99,
#           'egg' : 1.25}
#
# print(branch.get('bacon', 'Bad choice'))
#
# choice = 'bacon'
# if choice in branch :
#     print(branch[choice])
# else :
#     print('Bad choice!')
#
# try:
#     print(branch[choice])
# except KeyError:
#     print('Bad choice!!')


# A = 't' if 'spam' else 'f'
# print(A)
#
# B = 't' if '' else 'f'
# print(B)
#
# C = ['t','f'][bool('1')]
# print(C)
#
# L = [1,0,2,0,[],'spam']
# list1 = list(filter(bool,L))
# print(list1)
# print([x for x in L if x])

# x = 10
#
# while x :
#     x = x - 1
#     if x % 2 != 0 : continue
#     print(x)


# L = [1, 2, 3, 4, 5]
# # for i in range(len(L)) :
# #     L[i] *= 2
# # print(L)
# #
# # i = 0
# # while i < len(L) :
# #     L[i] += 1
# #     i += 1
# # print(L)
# #
# # print([ x+1 for x in L])


# keys = ['spam', 'egg', 'toast']
# values = [1, 3, 5]
# D1 = dict(zip (keys, values))
# print(D1)
# dict = {k : v for (k, v) in zip(keys, values)}
# print(dict)


# S = 'spam'
# for (i, c) in enumerate(S):
#     print(c, 'appears at offset', i)

# f = open('test.txt')
# print(f.__next__())
# print(iter(f) is f)
#
# L = [1,2,3]
# print(iter(L) is L)
# I = iter(L)
# print(I.__next__())
# print(next(I))
#
# for X in L:
#     print(X**2, end=' ')

# E = enumerate('spam')
# I = iter(E)
# print(next(I))
# I1 = iter('spam')
# print(next(I1))


# L = [line.upper() for line in open('test.txt')]
# L1 = [line.rstrip() for line in open('test.txt')]
# print(L)
# print(L1)
# L2 = [line.rstrip() for line in open('test.txt') if line[0] == 's']
# print(L2)
# L3 = [line.rstrip() for line in open('test.txt') if line.rstrip()[-1].isdigit()]
# print(L3)
# L4 = list(filter(bool, open('test.txt')))  # nonempty=true
# print(L4)
# S1 = {ix : line for (ix, line) in enumerate(open('test.txt')) if line[0] == 's'}
# print(S1)

print(sum([1,2,3,4,5]))
print(any(['spam','','ham']))
print(all(['spam','','ham']))
print(max([1,2,3,4,5]))
print(min([1,2,3,4,5]))
print(list(filter(bool,['spam','','ni'])))


