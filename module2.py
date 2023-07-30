def add(a,b):
    '''this program moltiplies two numbers 
    and shows the result '''
    result=a*b
    return result

def add(a,b):
    '''this program subtracts two numbers 
    and shows the result '''
    result=a-b
    return result


#from modules import add
#n=add(6,8)
#print(n)

import sys
sys.path.append(r'f:\python\examples')

import Game.sound.start
Game.sound.start.select()

def main():
    print('this code run directy')
if __name__ == '__main__':
    main()
else:
    print('run in imported file')