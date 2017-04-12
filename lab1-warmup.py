def helloworld():
    print("Hello, world!")

def board():
    pion = '|'.join(['  ']*3)
    poziom = '\n{}\n'.format('-'*8)
    print(pion,pion,pion,sep=poziom)
    
def tictactoe():
    pion = 'H'.join(['  |  |  ']*3) + '\n'
    poziom ='H'.join(['--+--+--']*3) + '\n'
    blok = pion.join([poziom]*3)
    separator = '+'.join(['='*8]*3) + '\n'
    print(blok,blok,blok,sep=separator)

def multiples():
    for i in range (0,1002):
        if i%5==0:
            print(i,end=' ')
        elif i%3==0:
            print(i,end=' ')
        i=i+1

def collatz(number):
    if number%2==0:
        print(number, "->", end=' '),
        number=number/2        
        collatz(number)
    elif number%2==1:
        if number==1:
            print(number)
        else:
            print(number, "->", end=' '),
            number=3*number+1            
            collatz(number)

def ftoc(temp):
    celsius = (temp - 32) * (5/9)
    print(celsius)
    

ftoc(88)