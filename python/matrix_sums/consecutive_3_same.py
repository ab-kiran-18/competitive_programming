n = int(input())
lst = []
for i in range(n):
    lst.append([int(i) for i in input().split()])
m = n + 1       # given in question
result = []
for i in range(n):
    for j in range(m):
        if i < n and j < m - 2 :
            if lst[i][j] == lst[i][j+1] == lst[i][j+2]:
                result.append(lst[i][j])
        if i < n - 2 and j < m:
            if lst[i][j] == lst[i+1][j] == lst[i+2][j]:
                result.append(lst[i][j])
        if i < n - 2 and j < m - 2:
            if lst[i][j] == lst[i+1][j+1] == lst[i+2][j+2]:
                result.append(lst[i][j])
print(min(result))