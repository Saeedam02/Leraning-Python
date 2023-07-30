
class error(Exception):
    pass

class valuetoosmallerror(error):
    pass
class valuetoobigerror(error):
    pass

number=10
while True:
    try:
        user=int(input('enter number:'))
        if user<number:
            raise valuetoosmallerror
        elif user>number:
            raise valuetoobigerror
        else:
            break
    except valuetoosmallerror:
        print('this value is small.try again')
    except valuetoobigerror:
        print('this value is big.try again')

print('good,you are done it very nice')




