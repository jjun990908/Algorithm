import sys
testcases = int(sys.stdin.readline())

tri = [0 for i in range(101)]
tri[1] = 1
tri[2] = 1
tri[3] = 1
for i in range (4, 101):
    tri[i] = tri[i-3] + tri[i-2]

for _ in range(testcases):
    N = int(sys.stdin.readline())
    print(tri[N])