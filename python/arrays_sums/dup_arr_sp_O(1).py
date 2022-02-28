l = list(map(int,input().split()))
l.sort()
for i in range(0,len(l)-1):
    if l[i]==l[i+1]:
        print(l[i])
        break