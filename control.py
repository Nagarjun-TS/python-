x = int(input("enter a number:"))
if x%2 == 0:
    print(x,"is even")
else:print(x,"is odd")

# we use elif for multiple if else conditions
x = int(input("enter a number"))
if x==0:
    print("entered 2 number")
elif x%2 == 0:
    print("entered an even number")
else:print("odd number")

if x%2==0 and x%3==0:
    print("nice")
else:print("ok")