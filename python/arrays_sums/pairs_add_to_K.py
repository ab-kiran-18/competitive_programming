def Pairs_to_k(arr,n,k):
        d = {}
        count = 0
        for i in arr:
            # try and except block for finding frequency using dict 
            try:
                d[i]+=1
            except:
                d[i]=1
        for i in range(0,len(arr)):
            try:
                count += d[k - arr[i]]          # we are counting each pair 2 times...
            except:
                d[k - arr[i]] = 0
            if k - arr[i] == arr[i]:
                count -= 1
        print(int(count/2))                 # so here we are dividing by 2 get half count...

l = [1 , 5 , 1 , 7]
Pairs_to_k(l,len(l),6)

# output :
#  1 + 5 : 6
#  5 + 1 : 6
#  so count is 2