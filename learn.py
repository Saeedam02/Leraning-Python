
class Employee:
    'this is a sample docstring'
    riase_amnt=1.04
    num_of_emp=0
    def __init__(self,fname,lname,pay):
        self.fname=fname
        self.lname=lname
        self.pay=pay
        self.email=fname+'@nabegheha.com'
        Employee.num_of_emp+=1
    def fullname(self):
        return f'{self.fname} {self.lname}'

    def apply_raise(self):
        self.pay=int(self.pay* self.riase_amnt)

emp1=Employee('saeed','aghamohammadi',200)
emp2=Employee('ali','molae',200)

class developer(Employee):

    def __init__(self, fname, lname, pay,lang):
        super().__init__(fname, lname, pay)
        self.lang=lang

    def __str__(self):
        return "developer ('{}', '{}', {})".format(self.fname,self.lname,self.pay)
    def __repr__(self):
        return '{},{}'.format(self.fullname(),self.email)
        
class manager(Employee):
        def __init__(self, fname, lname, pay,emps=None):
           super().__init__(fname, lname, pay)
           if emps==None:
            self.emps=[]
           else:
            self.emps=emps
        def add_emps(self,emp):
            if emp not in self.emps:
                self.emps.append(emp)
        
        def remove_emp(self,emp):
            if emp in self.emps:
                self.emps.remove(emp)

        def print_emp(self):
            for emp in self.emps:
                print('--->',emp.fullname())

dev1=developer('saeed','aghamohammadi',200,'english')
emp1=Employee('ali','mohammadi',200)
mgr1= manager('mehdi','asghari',600,[dev1])
mgr1.add_emps(emp1)
mgr1.print_emp()

print(dev1.__str__())