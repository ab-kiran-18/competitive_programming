

# Naive Approach:
    # for each element just checking how many elements are
    # greater in their left 
def InverseCount(l,n):
    inv_cnt = 0
    for i in range(n):
        for j in range(i+1,n):
            if l[i] > l[j]:
                inv_cnt += 1
    print(inv_cnt)
# Time Complexity : O(n^2)


# optimized solution:
    # Create a function merge that counts the number of inversions
    # when two halves of the array are merged, create two indices i and j,
    # i is the index for the first half, and j is an index of the second half.
    # if a[i] is greater than a[j], then there are (mid – i) inversions. 
    # because left and right subarrays are sorted, 
    # so all the remaining elements in left-subarray
    # (a[i+1], a[i+2] … a[mid]) will be greater than a[j].

def find_inverseCount(arr, n):
    temp = [0]*n
    return _merge(arr,temp,0,n-1)

def _merge(arr,temp,left,right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += _merge(arr,temp,left,mid)
        inv_count += _merge(arr,temp,mid+1,right)
        inv_count += merge(arr,temp,left,mid,right)
    return inv_count

def merge(arr,temp,left,mid,right):
    i = left
    j = mid + 1
    k = left
    inv_count = 0
    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            k += 1
            i += 1
        else:
            temp[k] = arr[j]
            inv_count += (mid-i + 1)
            k += 1
            j += 1
    while i <= mid :
        temp[k] = arr[i]
        k += 1
        i += 1
    while j <= right:
        temp[k] = arr[j]
        k += 1
        j += 1
    return inv_count
# Time Complexity : O(nlogn)
# Space Complexity : O(n)

l = [1 , 20 , 6 , 4 , 5]
x = find_inverseCount(l,len(l))
print(x)