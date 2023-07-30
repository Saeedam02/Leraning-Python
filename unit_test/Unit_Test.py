
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multipy(a,b):
    return a*b
def divide(a,b):
    if b==0:
        raise ValueError ('can not devide to zero')
    return a/b

print(add(2,8))