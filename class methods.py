class person:
    def __init__(self,name):
        self.__name=name
    @property   #this is a decorator(for getter)
    def name(self):
        #in fact it is getter
        #print('getting name')
        return self.__name

    @name.setter
    def name(self,value):
        #this is setter
        print(f'setting name to {value}')
        self.__name=value

    @name.deleter
    def name(self):
        print('deleting name')
        del self.__name

p=person('saeed')
print(f'the name is {p.name}')
p.name='ali'
print(f'the name is {p.name}')
del p.name
