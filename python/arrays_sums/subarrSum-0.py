def subArrayExists(arr,n):
    nth_sum = 0
    s = set()
    for i in range(n):
        nth_sum += arr[i]
        if nth_sum == 0 or nth_sum in s:
            return True
        s.add(nth_sum)
    return False
l = list(map(int,input().split()))
x = subArrayExists(l,len(l))
print(x)