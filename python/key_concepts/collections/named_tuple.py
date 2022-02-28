from collections import namedtuple

#---------------------------------------------------|   DECLARATION    |--------------------------------------------------

student = namedtuple('student',['name','age','DOB'])

#---------------------------------------------------|   ADDING VALUES   |---------------------------------------------------------

S1 = student('kiran','21','18-11-2001')
S2 = student('sk','20','18-11-2002')
S3 = student('chatti','21','18-11-2001')

#---------------------------------------------------|    ACCESSING    |-------------------------------------------------------

# using index
print("the student age using index is:",end='')
print(S1[1])

# using names
print('the student name is:',end='')
print(S2.name)

print(f'the DOB for {S3.name} is:',end='')
print(S3.DOB)

#--------------------------------------------|     CONVERSIONS    |-------------------------------------------------------

list1 = ['bon','con','jon']

# using _make() to return namedtuple()
print ("The namedtuple instance using iterable is  : ")
print (student._make(list1))                # conversion from list to named_tuple...
   
# using _asdict() to return an OrderedDict()
print ("The OrderedDict instance using namedtuple is  : ")
print (S3._asdict())                        # conversion from named_tuple to dictionary...