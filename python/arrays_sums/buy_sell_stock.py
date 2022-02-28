l = list(map(int,input().split()))
mini = prf = max_prf = 0
for i in l:
    if mini > i:
        mini = i
    prf = i - mini 
    max_prf = max(prf,max_prf)
print(max_prf)
