all = set(i for i in range(1,10001))
S = set()

for i in range(1,10001):
    for j in str(i):
        i += int(j)
    S.add(i)
for i in sorted(all - S):
    print(i)