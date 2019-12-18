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

for name, color, food in zip(names, colors, foods):
    print(name, ' - ', color, ' - ', food)