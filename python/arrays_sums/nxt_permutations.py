
def NextPermutation(l,n):
    k = l
    k = sorted(k,reverse=True)
    if l == k:
        return l[::-1]
    else:
        i=n-1
        while i>0:
            if l[i-1] < l[i]:
                tmp = l[i]
                l[i] = l[i-1]
                l[i-1] = tmp
                return l
            else:
                mini = min(mini,l[i])
            i-=1

l = list(map(int,input().split()))
x = NextPermutation(l,len(l))
print(*x,sep=' ')