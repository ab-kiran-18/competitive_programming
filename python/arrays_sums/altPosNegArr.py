l = list(map(int,input().split(',')))
k=0
for i in range(0,len(l)):
    if l[i] < 0:
        l[k],l[i] = l[i],l[k]
        k+=2
print(*l,sep=' ')