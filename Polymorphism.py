class shark:
    def swim(self):
        print('the shark is swiming')
    def swim_back(self):
        print('the shark can not swim backward')
    def skeleton(self):
        print('shark has big skeleton')
class clownfish:
    def swim(self):
        print('the clownfish is swiming')
    def swim_back(self):
        print('the clownfish can not swim backward')
    def skeleton(self):
        print('clownfish has big skeleton')
        
def in_the_pacific(fish):
    fish.swim_back()
a1=shark()
a2=clownfish()
#in_the_pacific(a2)
for fish in (a1,a2):
    fish.swim()
    fish.swim_back()
    fish.skeleton()

class dog:
    def sound(self):
        print('the sound of dog')

class cat:
    def sound(self):
        print('the sound of cat')

def make_sound(animal):
    animal.sound()

cat1=cat()
dog1=dog()
#make_sound(cat1)