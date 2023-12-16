import sys
input = sys.stdin.readline

N = int(input())
company = {}
for _ in range(N):
    person, state = input().rstrip().split()
    if state == 'enter':
        company[person] = True
    else:
        del company[person]

print("\n".join(sorted(company.keys(), reverse=True)))