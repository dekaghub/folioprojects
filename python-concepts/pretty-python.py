# Borrowed from Raymond Hettinger's talk
# https://www.youtube.com/watch?v=OSGv2VnC0go

# Every list is iterable

# simple reverse iteration of for loop
colors = ['red', 'green', 'blue', 'yellow']

for color in reversed(colors):
    print(color)

# keep track of indices 
for i, color in enumerate(colors):
    print(i, '-->', color)

# print multiple lists together
names = ['Jon', 'Kate', 'Defie']
foods = ['cheese', 'sauce', 'chips', 'guac']

# behaves like an inner join i.e. smallest of all the lists
for name, color, food in zip(names, colors, foods):
    print(name, ' - ', color, ' - ', food)

# general find function
def find(seq, target):
    for i, value in enumerate(seq):
        if value == target:
            break
    else:
        return -1
    return i

print(find(colors, 'purple'))
print(find(colors, 'yellow'))

# lambda functions
g = lambda x: x**2
print(g(2))

# dictionary

# create dictionary from lists
d = dict(zip(names, colors))

for k,v in d.items():
    print(k, ' - ', v)

# Be Explicit with function calls for good readability
# Name the parameters to avoid bouncy reading
def favoriteFood(name, food):
    favorite = name + ' ' + food
    return favorite

import random
print(favoriteFood(name = names[random.randint(0, len(names)-1)], food = foods[random.randint(0,len(foods)-1)]))

import collections
def test(a,b):
    tupleResult = collections.namedtuple('testResult', ['a','b'])
    testResult = tupleResult(a,b)
    return testResult

t = test(a='first', b='second')
print(t)

# One Line variable inits
a,b,c, = 1,2,3
print('a : ', a,' b : ', b, ' c : ', c)
x = [5,6,7]
a,b,c = x
print('a : ', a,' b : ', b, ' c : ', c)