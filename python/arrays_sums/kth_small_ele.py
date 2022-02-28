l = list(map(int,input().split()))
k = int(input())
d={}
l.sort()
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
f = 0
for i in d:
    f+=d[i]
    if f >= k:
        print('kth minimum element is :' + str(i))
        break
