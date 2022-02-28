
def right_rotate(l,k):
    sz = len(l)
    while(k!=0):
        x = l.pop()
        l.insert(0,x)
        k-=1
    return l

def left_rotate(l,k):
    sz = len(l)
    while(k!=0):
        x = l.pop(0)
        l.insert(sz-1,x)
        k-=1
    return l

l = list(map(int,input().split()))
k = int(input())
k = k % len(l)
l1 = l
right_l = right_rotate(l1,k)
print(*right_l,sep=',')
left_l = left_rotate(l,k)
print(*left_l,sep=',')