N = int(input())

room = 1
depth = 1

while N>room:
    room += 6 * depth
    depth += 1

print(depth)
