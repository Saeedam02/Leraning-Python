import datetime

today=datetime.datetime.now()

#print(str(today))
#print('##############')
#print(repr(today))

class book:
    def __init__(self,title,author,pages):
        print('book has been created')
        self.title=title
        self.author=author
        self.pages=pages
 
    def __str__(self):
        return 'title:{}, author:{} ,pages:{}'.format(self.title,self.author,self.pages)

    def __len__(self):
        return self.pages
b=book('python','saeed',300)
print(len(b))
 