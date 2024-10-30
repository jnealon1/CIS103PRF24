class employee:


    num_of_emps = 0
    raise_amt = 1.04
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.'+ last + '@company.com'

        employee.num_of_emps += 1

    def fullname(self):
       return('{} {}'.format(self.first, self.last))
    
    def apply_raise(self):
        self.pay = int(self.pay *employee.raise_amt)



class developer(employee):
    raise_amt = 1.10
    
    def __init__(self,first,last,pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang



class Manager(employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp not in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->',emp.fullname())

        


dev_1 = developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager ('Sue', 'Smith' , 90000, [dev_1])
#mgr_1.add_emp(dev_2)
#mgr_1.print_emps()






print(issubclass(Manager, developer))












