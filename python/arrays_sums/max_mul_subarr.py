def max_mul_subarr(arr,n):
    mini = 1
    maxi = 1
    max_so_far = 0
    flag = 0
    for i in range(n):
        if arr[i] > 0:
            maxi = maxi * arr[i]
            mini = min(mini * arr[i], 1)
            flag = 1
        elif arr[i] == 0:
            maxi = 1
            mini = 1
        else:
            temp = maxi
            maxi = max(mini * arr[i], 1)
            mini = temp * arr[i]
            max_so_far = max(maxi,max_so_far)
    if flag==0 or max_so_far==0:
        return 0
    return max_so_far

l = list(map(int,input().split(',')))
print(max_mul_subarr(l,len(l)))