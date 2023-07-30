
try:
    f=open('a2.txt')
except FileNotFoundError as e:
    print(e)

else:
    print(f.read())
    f.close()

finally:
    print('I am running')