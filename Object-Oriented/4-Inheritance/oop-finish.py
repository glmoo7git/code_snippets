
class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
    

class Developer(Employee):                           # even without any code of its own the developer class will have all of the
    raise_amt = 1.10                                 # attributes and methods of our employee class
    
    def __init__(self, first, last, pay, prog_lang):   # super.__init__ is going to pass first, last and pay to our 
        super().__init__(first, last, pay)             # employees and __init__ method and let that class handle those arguments
        self.prog_lang = prog_lang


class Manager(Employee):

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
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_2)

mgr_1.print_emps()

# python has these two built-in functions called is instance and 
# is subclass so is instance will tell us if an object is an instance of a class so for example 

print(isintance(mgr_1,manager))      # if I need to print this out I can print out whether manager one is an instance of manager
                                    # and if I print that out you can see that  it prints true now
print(isintance(mgr_1,Employee))    # if I was to check whether the manager is an instance of an employee then you can see that is also true

print(isintance(mgr_1,Developer))   # but if I check if manager one is an instance of a developer then thatreturns false
                                    # because even though developer and manager both inherit from employee 
                                    # they aren't part of each other's inheritance
        
# issubclass will tell us if a class is a subclass of another 

print(issubclass(Developer, Employee))  # is developer a subclass of employee that it returns true

print(issubclass(Maneger, Employee))    # is manager a subclass of employee that returns true also
 
print(issubclass(Maneger, Developer))  #  is manager a subclass of developer then that will return false




