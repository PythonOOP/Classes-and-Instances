# Python Object-Oriented Programming

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return self.first + " " + self.last

emp_1 = Employee("Lukasz", "Radzik", 6000)
emp_2 = Employee("Adam", "Nowak", 5000)

print(Employee.fullname(emp_1))
print(emp_1.fullname())
