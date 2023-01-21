line = str(input())
cut = line.split("-")
answer = sum(map(int,cut[0].split("+")))

for n in cut[1:]:
    answer -= sum(map(int,n.split("+")))
print(answer)