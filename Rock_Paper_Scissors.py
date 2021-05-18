import random
y=0
z=0
while(True):
    n=input('''Enter.......\nr for Rock\np for Paper\ns for Scissors\n''')
    if(n=='r'):
        a=1
    elif(n=='p'):
        a=2
    elif(n=='s'):
        a=3
    else:
        print('Invalid choice')
        a=0
    
    b=random.randint(1,3)

    if(a!=0):

        print('Your choice is '+n)
        if(b==1):
            print('Computer choice is r')
        elif(b==2):
            print('Computer choice is p')
        elif(b==3):
            print('Computer choice is s')

    if(a==b):
        print('Tie')
    elif(a==1):
        if(b==2):
            print('You Lost')
            z=z+1
        else:
            print('You Won')
            y=y+1
    elif(a==2):
        if(b==3):
            print('You Lost')
            z=z+1
        else:
            print('You Won')
            y=y+1
    elif(a==3):
        if(b==1):
            print('You Lost')
            z=z+1
        else:
            print('You Won')
            y=y+1
    
    if(a!=0):
        print('Your score: ',y)
        print('Computer score: ',z)

    c=input('Enter x to exit, something else to continue\n')
    if(c=='x'):
        break
