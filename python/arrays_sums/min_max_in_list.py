l = list(map(int,input('enter elements in list:').split()))
maxi = mini = l[0]
for i in l:
    if i > maxi:
        maxi = i
    if i < mini:
        mini = i
print('max = ' + str(maxi) + "  " + 'min = ' + str(mini) )