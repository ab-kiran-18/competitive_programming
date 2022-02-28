n = int(input())
mat = []
for _ in range(n):
    mat.append(list(map(int,input().split())))

key = int(input())

flag = 0

for i in range(0,n):
    for j in range(0,len(mat[i])):
        if key == mat[i][j]:
            print(f'element found at position [{i}][{j}]')
            flag = 1
            break

if flag != 1:
    print('element not found..')
