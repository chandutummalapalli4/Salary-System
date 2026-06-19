salary=float(input("Enter Salary Amount:"))
print("Basic Salary=",salary)
hra=salary*0.20
print("HRA:",hra)
da=salary*0.10
print("DA:",da)
Grosssalary=salary+hra+da
print("Gross Salary:",Grosssalary)
if Grosssalary>50000:
    tax=Grosssalary*0.10
    print("Tax:",tax)
    Netsalary=Grosssalary-tax
    print("Net Salary:",Netsalary)
else:
    tax=Grosssalary*0.05
    print("Tax:",tax)
    Netsalary=Grosssalary-tax
    print("Net Salary:",Netsalary)
