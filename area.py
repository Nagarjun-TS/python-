import math

radius = float(input("enter the radius"))
area = math.pi*radius**2
print("the radius of circle is %f"%(area))

#find the average of three numbers
a,b,c = (int(x) for x in input("enter any three numbers\n").split())
average = (a+b+c)/3
print(average)
print(max(a,b,c))