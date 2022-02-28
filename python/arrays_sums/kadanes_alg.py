def kadane(l,size):
    max_so_far = 0
    cur_max = 0
    start = 0
    end = 0
    s = 0
    for i in range(0,size):
        cur_max += l[i]
        if cur_max < 0:
            cur_max = 0
            s = i + 1
        elif cur_max > max_so_far :
            max_so_far = cur_max
            start = s
            end = i
    print('max sum = ',max_so_far)
    print('indexes : ',start,',',end)


n = int(input())
l = list(map(int,input().split()))
print(kadane(l,n))