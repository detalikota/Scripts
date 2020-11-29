""" class SpecialString:
  def __init__(self, cont):
    self.cont = cont

  def __radd__(self, other):
    line = "=" * len(other.cont)
    return "\n".join([self.cont, line, other.cont])

spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam + hello) """


class Employee:
  raise_amount = 1.04
  num_of_emps = 0
  def __init__(self, name, surname, pay):
    self.name = name
    self.surname = surname
    self.pay = pay
    self.email = name + "." + surname + "@company.com"
    Employee.num_of_emps += 1
  def fullname(self):
    return '{} {}'.format(self.name, self.surname)
  def pay_raise(self):
    self.pay = int(self.pay*self.raise_amount)
  def __sub__(self,other):
    return self.pay - other.pay


emp1 = Employee("Jack", "Eddison", 10000)
emp2 = Employee("1","2",5000)
print (emp1.fullname())
emp1.raise_amount = 1.08
emp1.pay_raise()
print (emp1.pay)
print(emp1.__dict__)
print(Employee.num_of_emps)
print (emp1 - emp2)