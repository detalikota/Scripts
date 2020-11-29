class Employee:
  raise_amount = 1.04
  
  def __init__(self, name, surname, pay):
    self.name = name
    self.surname = surname
    self.pay = pay
    self.email = name + "." + surname + "@company.com"

  def fullname(self):
    return '{} {}'.format(self.name, self.surname)

  def pay_raise(self):
    self.pay = int(self.pay*self.raise_amount)

class Developer(Employee):
    raise_amount = 1.1
    def __init__(self, name, surname, pay, prog_lang):
        super().__init__(name, surname, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, name, surname, pay, employees=None):
      super().__init__(name, surname, pay)
      if employees is None:
        self.employees = []
      else:
        self.employees = employees
    def add_employee(self, emp):
      if emp not in self.employees:
        self.employees.append(emp)
    def remove_employee(self, emp):
      if emp in self.employees:
        self.employees.remove(emp)
    def print_emps(self):
      for emp in self.employees:
        print('---->', emp.fullname())




dev_1 = Developer('sadf', 'sdf', 5000, 'python')
dev_2 = Developer('sdfwe', 'tewds', 30000, 'java')
mgr = Manager('yeah', 'cool', '90000', [dev_1])
mgr.add_employee(dev_2)
mgr.remove_employee(dev_1)
Manager.print_emps(mgr)
print(dev_1.prog_lang)
print(dev_1.pay)
dev_1.pay_raise()
print(dev_1.pay)
""" print(dev_1.email)
print(dev_2.email)
 """
#print (help(Developer))