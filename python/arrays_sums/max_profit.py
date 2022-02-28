lst = list(map(int,input().split(',')))
n = len(lst)
profit = 0
for i in range(0,len(lst)):
    sub = lst[i] -  lst[i-1]
    if sub > 0:
        profit += sub
print(profit)