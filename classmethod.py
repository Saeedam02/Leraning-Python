
from datetime import date
class person:
    
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def year(cls,name,year):
        return cls(name,date.today().year-year)


    def desplay(self):
        print(f'my name is {self.name} and i am {self.age} years old.')

p=person('saeed',30)
p.desplay()
p1=person.year('ali',1999)
p1.desplay()