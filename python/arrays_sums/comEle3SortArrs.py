l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
l3 = list(map(int,input().split()))

n1 = len(l1)
n2 = len(l2)
n3 = len(l3)

i = j = k = 0

res = []

maxi = max( l1[0], l2[0], l3[0])

while( i < n1 and j < n2 and k < n3 ):

    while(l1[i] < maxi and l1[i] < n1):
        i+=1
    while(l2[j] < maxi and l2[j] < n2):
        j+=1
    while(l3[k] < maxi and l3[k] < n3):
        k+=1
    if ( l1[i] == l2[j] and l2[j] == l3[k]):
        if ( res[len(res)-1] != l1[i] or len(res)==0 ):
            res.append(l1[i])
            i+=1
            j+=1
            k+=1
    maxi = max( l1[i], l2[j], l3[k])

print(*res,sep=' ')