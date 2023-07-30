
class mymath:
     
    @staticmethod
    def addnumbers(x,y): 
        return x+y

#print(mymath.addnumbers(5,8))

class dates:

    @staticmethod 
    def dash(date):
        return date.replace('/','-')

new='22/10/30'
removed_dash=dates.dash(new)
#print(removed_dash)

class person:

    age=24
    @classmethod
    def printage(cls):
        print('the age is:', cls.age )

person.printage()