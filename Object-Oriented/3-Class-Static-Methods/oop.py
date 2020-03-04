
class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):       #this is a regular method
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
        
#  regular method we called this instance variable self and there's a common
# convention for class variables too and that is CLS

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    
#  here so let's say that we wanted
# a simple function that would take in a
# date and return whether or not that was
# a workday so that has a logical
# connection to our employee class but it
# doesn't actually depend on any specific
# instance or class variable so instead 

    @staticmethod                   
    def is_workday(day):                                     #remember static methods don't take the
        if day.weekday() == 5 or day.weekday() == 6:         #instance or the class as the first
            return False                                     #argument so we can just pass in the
        return True                                          #arguments that we want to work with
    
# now sometimes people write regular methods or class methods that actually should be static
# methods and usually a giveaway that a method should be a static method is if
# you don't access the instance or the class anywhere within the function so
# say that I had this class method up here     
# @classmethod
#     def from_string(cls, emp_str):
#         first, last, pay = emp_str.split('-')
#         return cls(first, last, pay)
# you can see that I'm using that cls variable there but if I wasn't using it anywhere within that method then it
# probably doesn't need to be a class method and the same with regular methods
# if you're not using that self variable then  you probably want to
# check and see if that would be appropriate to use a static method 

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

first, last, pay = emp_str_1.split('-')

#new_emp_1 = Employee(first, last, pay)
new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

import datetime
my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))
