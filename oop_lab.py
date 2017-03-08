
class Employee(object):

    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 25.00

class Intern(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 5

class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 10.00

    def full_time_wage(self, hours):
        return super(PartTimeEmployee, self).calculate_wage(hours)

if __name__ == "__main__":
    pitt = PartTimeEmployee("joy")
    print(pitt.full_time_wage(8))