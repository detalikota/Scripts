class Employee:
    pay_raise = 1.04
    def __init__(self, name, surname, pay):
        self.name = name
        self.surname = surname
        self.pay = pay
        self.email = name + '.' + surname + '@gmail.com'
        self.fullname = name + ' ' + surname
    def raising(self):
        self.pay = int(self.pay_raise * self.pay)

emp1 = Employee("Jack", "Maddison", 10000)
emp1.raising()
print (emp1.pay)
