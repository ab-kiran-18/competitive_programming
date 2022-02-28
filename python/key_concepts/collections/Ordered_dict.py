from collections import OrderedDict

# OrderedDict() is like a dictionary but which can also remember the order of inserting of Keys...

#---------------------------------------------------|   DECLARATION  |--------------------------------------------------------

ord_dict = OrderedDict()

#-----------------------------------------------------|   INSERT   |----------------------------------------------------------

ord_dict['a'] = 4
ord_dict['c'] = 5
ord_dict['f'] = 11
ord_dict['a'] += 2
ord_dict['c'] += 13

#-----------------------------------------------------|  ACCESSING  |----------------------------------------------------------

for key, value in ord_dict.items():
    print(key, value)

#------------------------------------------------------|  REMOVE  |-------------------------------------------------------------------

ord_dict.pop('a')

# if we re-insert 'a' order will change acording to insertion...

ord_dict['a'] = 9

print(ord_dict)