""" IN THIS PYTHON PROGRAM WE WILL LEARN LOGICAL OPERATORS AND PRINT() FUNCTIONS"""
a=10
b=20
print("a==b:",a==b)
print("a>b:",a>b)
print("a!=b:",a!=b)
print("a<b:",a<b)
print(a,b,sep=' & ')
#HERE SEP IS USED TO ASSIGN THINGS B/W 2 OPERANDS THE THING THAT HAS TO BE ASSIGNED IN A SINGLE QUOTE
name = "NAGARJUN"
marks = 98.42
print("name :",name,"and marks achived=",marks)
print("name is %s and marks secured = %f"%(name,marks))
print("name is {} and marks secured = {}".format(name,marks))
#we use %() func to assign values to %op  %op and we have format function to pass arguements to flower brackets
# INPUT FUNCTION IS USED TO PASS ARGUEMENTS DURING RUN TIME WE CAN USE THEM IN FOLLOWING WAY

S = input("enter ur name \n")
print(S)

# the input function takes the value in string format and it can be typecasted

s = int(input("number\n"))
print(s)

lst =[x for x in input("enter three numbers seperated by comma: ").split(',')]
print(lst)