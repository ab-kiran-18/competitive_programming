from collections import Counter

# Counter() is a object used mostly when we want to find frequency of elements...
# it usually ordered by elements having more frequency... 

# we can use Counter() in below formats:

# with iterables..
l1 = [1,2,3,1,3,1,2,3,1,2,3,4,3,2,4,5,5,3,2,1,3,4,5,5,4,2,6]
print(Counter(l1))

# with dictionaries having Keys and counts(usually Values)
d1 = { 1 : 3,
       2 : 4,
       5 : 9 }
print(Counter(d1))

# we can also create a empty Counter()..
empty_count = Counter()

# we can update Counter()
empty_count.update(l1)