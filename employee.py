class Employee:
    def __init__(self, name, basic_pay, da, hra, cca):
        self.name = name
        self.basic_pay = basic_pay
        self.da = da
        self.hra = hra
        self.cca = cca

    def calculate_salary(self):
        return self.basic_pay + self.da + self.hra + self.cca

# Creating instances for 3 employees
employee1 = Employee("Alice", 50000, 10000, 8000, 2000)
employee2 = Employee("Bob", 45000, 9000, 7000, 1500)
employee3 = Employee("Charlie", 60000, 12000, 9000, 2500)

# Calculating and printing salaries
print(f"{employee1.name}'s salary: {employee1.calculate_salary()}")
print(f"{employee2.name}'s salary: {employee2.calculate_salary()}")
print(f"{employee3.name}'s salary: {employee3.calculate_salary()}")
