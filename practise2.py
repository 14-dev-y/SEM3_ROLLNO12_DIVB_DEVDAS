class Employee:
    def __init__(self, emp_id, name, number, salary):
        self.emp_id = emp_id
        self.name = name
        self.number = number
        self.salary = salary
        
    def calculateSal(self):
        if self.salary <= 10000:
            hra = self.salary * 0.10
            da = self.salary * 0.05
            pf = self.salary * 0.08
        elif self.salary <= 20000:
            hra = self.salary * 0.15
            da = self.salary * 0.10
            pf = self.salary * 0.10
        else:
            hra = self.salary * 0.18
            da = self.salary * 0.07
            pf = self.salary * 0.09
            
        e_salary = self.salary + hra + da
        total_salary = e_salary - pf

        return hra, da, pf, e_salary, total_salary

    def displayData(self):
        hra, da, pf, e_salary, total_salary = self.calculateSal()

        print("\n--- Employee Details ---")
        print("Employee ID: ", self.emp_id)
        print("Employee Name: ", self.name)
        print("Employee Number: ", self.number)
        print("Salary: ", self.salary)
        print("HRA: ", hra)
        print("DA: ", da)
        print("PF: ", pf)
        print("Gross Salary: ", e_salary)
        print("Net Salary: ", total_salary)

employee = []

n = int(input("Enter Number of Employees: "))

for i in range(n):
    print(f"\nEntering details for Employee {i+1}:")
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    number = int(input("Enter Employee Number: "))
    
    # FIXED: The prompt previously asked for "Employee ID" again
    salary = float(input("Enter Employee Salary: ")) 

    # FIXED: Indented these two lines so they happen for every employee inside the loop
    emp = Employee(emp_id, name, number, salary)
    employee.append(emp)

# FIXED: Changed 'Employee' (the Class) to 'employee' (the List)
for emp in employee:
    emp.displayData()