class Employee:
    name = 'chaudhuree'
    age = 27
    designation = 'sales executive'
    salesMadeThisWeek = 4

    def target_acheived(self):
        if self.salesMadeThisWeek >= 5:
            return 'target acheived'
        else:
            return 'target not acheived'
    def change_name(self):
        # self.name='sOhan'
        # both are same ⬇⬆
        Employee.name = 'sOhan'
        return Employee.name



employee = Employee()
print(employee.target_acheived())
print(employee.name)
employee.change_name()
print(employee.name)
