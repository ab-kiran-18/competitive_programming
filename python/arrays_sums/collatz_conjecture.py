def Collatz(n):
    res = []
    while n != 1:
        res.append(n)
        if n & 1:
            n = 3 * n + 1
        else:
            n = n // 2
    res.append(n)
    return res

num = int(input())
seq  = Collatz(num)
print(*seq,sep=',')   