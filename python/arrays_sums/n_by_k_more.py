from collections import Counter

lst = list(map(int,input().split(',')))

k = int(input())

n = len(lst)

x = n//k

mp = Counter(lst)

res = []

for i in mp:
    if mp[i] > x:
        res.append(i)

print(*res,sep=',')