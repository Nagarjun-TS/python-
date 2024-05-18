
"""MULTI LINE COMMENTS ARE PASSED USING TRIPLE QUOTES. NOW WE WILL FIND OUT THE DIFFERENCE BETWEEN TUPLE AND SET
AND ACCESS ITS VARIOUS FUNCTIONS"""
# WHAT IS A LIST??
# LISTS ARE ONE IF THE 4 BUILTIN DATA TYPES IN PYTHON USED TO STORE COLLECTION OF DATA.
#LISTS ARE CREATED USING SQUARE BRACKETS
#THEY ARE MUTABLE
thislist = ["apple",4,2,51,12,23,1,23,1,31,31,1,14]
print(thislist)
thislist.insert(2,6)
thislist.append(3)
thislist.insert(0,4)
print(thislist)
thislist.remove("apple")
thislist.sort()
print(thislist)
thislist.sort(reverse = True)
print(thislist)
count = thislist.count(1)
print(thislist[::-1])
print(thislist[0:13:2])
thislist[::-1]
print(thislist)
for i in range(count):
    print(thislist[i])
thislist.clear()

"""IN THE ABOVE  SECTION WE LEARNT ABOUT LIST IN PYTHON . NOW WE WILL SEE TUPLE"""
#TUPLE IS A IMMUTABLE LIST WHERE WE CAN perform minimum operations on it
tup1 = (1,2,3,4,4,5,6)
print(tup1.count(4))
print(tup1.index(2))
print(tup1[::-1])






