x = input()
cro_al = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in cro_al:
    x = x.replace(i, 'a')
print(len(x))