
def top(lst):
    return lst.pop()

def merge_Intervals(arr,n):
    arr.sort(key = lambda x: x[0])
    s = []
    for i in range(n):
        a = arr[i]
        if i!=0:
            t = top(s)
        if i==0:
            s.append(a)
        elif t[1] < a[0]:
            s.append(a)
        elif t[1] <= a[1]:
            t[1] = a[1]
            s.pop()
            s.append(t)
    for i in s:
        print(f'{s[0]} : {s[1]}')

if __name__ == '__main__':
    l = [[1,3],[2,6],[8,10],[15,18],[21,23],[9,12]]
    merge_Intervals(l,len(l))
    
