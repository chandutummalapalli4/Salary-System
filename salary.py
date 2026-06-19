salary = float(input("Enter Salary Amount: "))

if salary < 0:
    print("Invalid salary")

else:
    print("Basic Salary:", salary)

    hra = salary * 0.20
    da = salary * 0.10

    gross_salary = salary + hra + da

    if gross_salary > 50000:
        tax = gross_salary * 0.10
        tax_rate = "10%"
    else:
        tax = gross_salary * 0.05
        tax_rate = "5%"

    net_salary = gross_salary - tax

    print(f"HRA: {hra}")
    print(f"DA: {da}")
    print(f"Gross Salary: {gross_salary}")
    print(f"Tax ({tax_rate}): {tax}")
    print(f"Net Salary: {net_salary}")
