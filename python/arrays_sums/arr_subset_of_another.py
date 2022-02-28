
def is_subset(lis1,lis2,n1,n2):
    dic = {}
    for i in lis1:
        try:
            dic[i] += 1
        except:
            dic[i] = 1
    for i in lis2:
        if i not in dic:
            return False
    return True
    


lis1 = list(map(int,input().split(',')))
lis2 = list(map(int,input().split(',')))
n1 = len(lis1)
n2 = len(lis2)

if(is_subset(lis1,lis2,n1,n2)):
    print('Yes')
else:
    print('No')

