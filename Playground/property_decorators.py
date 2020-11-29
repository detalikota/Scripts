class Employee:
    def __init__(self, name, surname, pay):
        self.name = name
        self.surname = surname
        self.pay = pay
        self.email = name + "." + surname + "@company.com"
    @property #makes it possible to call fullname without ()
    def fullname(self):
        return '{} {}'.format(self.name, self.surname)
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

 
emp = Employee("cat", "dog", 354355)
""" del emp.fullname"""
del emp.fullname


print (emp.fullname)