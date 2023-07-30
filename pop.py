class pop_artist:
    def __init__(self,name):
        self.__name=name
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name=value

p=pop_artist('jahani')
print(p.name)