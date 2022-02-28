l = list(map(int,input().split()))

# Dictionary to find frequency..
d = {}

# finding counts for 0,1,2
for i in l:
    try:
        d[i] += 1
    except:
        d[i] = 1

# Making a list combining 0's , 1's and 2's lists...
l = [0]*d[0] + [1]*d[1] + [2]*d[2]

print(*l,sep=' ')