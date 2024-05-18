#IN THIS PROGRAM WE WILL UNDERSTAND THE MEANING OF SET AND DICTIONARY AND ITS USES
#set are initialized with flower brackets they donot support indexing,slicing,repeatation using *3
# we can perform remove and update option but if in case of frozen set this is also unavoidable
s={1,2,3,4,4,15}
s.update([0])
s.remove(15)
print(s)
s1=frozenset(s)

#byte array does not support assignment of values
#in this we will try to use dictionary

dict1 ={1:"john",2:"id 57-73-123",3:"ur welcome"}
print(dict1.items())
v = dict1.values()
for i in v:print(i)

# using dictionary we will map student details where we use list
students={'JOHN':['PYTHON','DJANGO','DRF'],'BOB':['JAVA','SPRING COURSE'],'JIM':['JS','NODE']}
keys = students.keys()
print(keys)
for eachkeys in keys:
    print("courses taken by ",eachkeys,"are:")
    for eachcourse in students[eachkeys]:
        print(eachcourse)
