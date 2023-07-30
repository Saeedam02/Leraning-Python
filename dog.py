
class dog:
    species='mammal'
    def __init__(self,breed,name,khaz=True):
        self.breed=breed
        self.name=name
        self.khaz=khaz

frank=dog('doberman','marshal',khaz=False)
print(frank.khaz)
  