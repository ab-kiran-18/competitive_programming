
# they are immutable....
# sets are unordered ...
# they will randomly pick elements and print them for each print statement...

# func related to sets:
s1 = {'nawab',493,'nyc',8349,932,'wife'}
s2 = {'owe','igloo','tom'}


#----------------------------------------------------------: INSERT :--------------------------------------------------------

s1.add('kat')

# to add items into a set from another set 
s1.update(s2)

# to add items in list to set
l = [8,28,3498,'rej']
s1.update(l)

#----------------------------------------------------------: REMOVE :--------------------------------------------------------

s1.remove('owe')
s1.discard('nyc')
# difference btw remove() and discard() is 
# when item is not present remove() will show error and discard() will not ... 

s1.pop()
# this will remove an item from front..

s2.clear()
# will clear empties the set...

del s1
# this will deletes the set completely..

print(*s1,sep=' ')

# --------------------------------------------------------------: METHODS :-------------------------------------------------

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

# is_disjoint() : Returns whether two sets have a intersection or not
z0 = x.isdisjoint(y)

# issubset() : Returns whether another set contains this set or not
z1 = x.issubset(y)

# issuperset() : Returns whether this set contains another set or not
z2 = y.issuperset(x)

print(z0,z1,z2,sep='  ')

# Union() : returns a set containing elements present in either of the 2 sets...
s3 = s1.union(s2)

# intersection() : returns a set containing elements that are present in both sets as common..
s4 = s1.intersection(s2)
