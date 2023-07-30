class car:
    def __init__(self,speed,color):
        self.__speed=speed
        self.color=color
        
    def set_speed(self,value):
        self.__speed=value

    def get_speed(self):
        return self.__speed

peykan=car(100,'red')
pride=car(120,'black')

pride.__speed=30
print(pride.get_speed())



