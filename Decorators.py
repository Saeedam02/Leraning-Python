
def mydecorator(msg='massage'):
    def decorated(func):#this is a decorator.
        def wrapper(name):#this is an arranged name.
            print('inside decorator before')
            print(f'the massage is:{msg}')
            func(name)
            print('inside decorator after')
        return wrapper
    return decorated
@mydecorator('this is for test')
def printname(name):
    print(name)
printname('saeed')



