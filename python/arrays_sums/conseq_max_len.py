
def long_con(arr,n):
    arr.sort()
    count = 1
    res = 1
    for i in range(0,len(arr)-1):
        if arr[i]==arr[i+1]:
            continue
        elif arr[i+1] - arr[i] == 1:
            count += 1
        else:
            count = 1
        res = max(res,count)
    return res


n = int(input())
lst = list(map(int,input().split()))
ans = long_con(lst,n)
print(ans)