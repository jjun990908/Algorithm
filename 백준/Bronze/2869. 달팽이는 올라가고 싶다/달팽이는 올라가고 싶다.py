import math

n = input()
list = n.split()
a = int(list[0])
b = int(list[1])
v = int(list[2])

answer = (v-b)/(a-b)
print (math.ceil(answer))