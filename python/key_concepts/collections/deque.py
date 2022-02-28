from collections import deque

queue = deque(['name','age','DOB'])

#------------------------------------------------|  APPEND  |----------------------------------------------------------------

# append() : appends element from back by default...
queue.append('sonu')

# appendleft() : it appends elemnet from front...
queue.appendleft('monu')

print(queue)

#-----------------------------------------------|   REMOVE  |-----------------------------------------------------------------

# pop() : removes element and returns the element...
x = queue.pop()

print(x)

# popleft() : removes element from start and returns the element...
queue.popleft()

print(queue)