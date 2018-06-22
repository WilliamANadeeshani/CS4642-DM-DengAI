import random

file_object = open('input.txt', 'r')

with open('input.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]


file_output = open('output.txt', 'w')

y = random.randint(-1, 2)

for x in content:
    x = int(x) + y
    file_output.write(str(x)+'\n')
