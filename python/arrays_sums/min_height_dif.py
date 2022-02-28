def getMinDiff(arr, n, k):
        arr.sort()
        ans = arr[n-1] - arr[0]
        large = arr[n-1] - k
        small = arr[0] + k
        for i in range(0,n-1):
            maxi = max(large,arr[i]+k)
            mini = min(small,arr[i+1]-k)
            if mini < 0:
                continue
            ans = min(ans, maxi - mini)
        return ans

l = list(map(int,input('input list:').split()))
k = int(input('enter K:'))
print(getMinDiff(l, len(l),k))