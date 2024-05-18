n = int(input("Enter the number of employees: "))
employee = {}
for i in range(n):
    name = input("Enter employee name: ")
    salary = input("Enter employee salary: ")
    employee[name] = salary

while True:
    name = input('Enter the name to get employee details: ')
    salary = employee.get(name, -1)
    if salary == -1:
        print("No employee exists in the name of: ", name)
    else:
        print(name, " gets ", salary, " rupees as salary")
    choice = input("Enter yes to continue and no to break: ")
    if choice== 'no' or choice == 'NO':
        break