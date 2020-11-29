class Employee:

    raise_amt = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1

    def fullname(self): 
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amt)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

import datetime
my_date = datetime.date(2020, 11, 28)
print(Employee.is_workday(my_date))


emp_1 = Employee('Jack', 'Eddison', 50000)
emp_2 = Employee('Nick', 'Courtey', 100000)

Employee.set_raise_amount(1.05)
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

emp_str_1 = 'John-Doe-70000'

first, last, pay = emp_str_1.split('-')

emp_3 = Employee(first, last, pay)

print(emp_3.fullname())

emp_str_2 = 'Magomed-Rabadanov-999999999'
emp_4 = Employee.from_string(emp_str_2)
print(emp_4.fullname())