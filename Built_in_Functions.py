
from typing import Collection


def even(n):
    if n%2==0:
        return True
    else:
        return False
l=range(20)
#print(list(filter(even,l)))

from collections import namedtuple 

animal=namedtuple('animal','name age type')

dog=animal(name='marshal',age=1,type='deberman')

print(dog.name)
