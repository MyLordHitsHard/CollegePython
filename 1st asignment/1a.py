        
def weired_number():
    n = int(input().strip())
    if n % 2 != 0:
        print('Weird')
    else:
        if n >= 2 and n <= 5:
            print('Not Weird')
        elif n >= 6 and n <= 20:
            print('Weird')
        elif n > 20:
            print('Not Weird')

def add_subtract_multiply():
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)

def divide():
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)
    
def print_for_range():
    n = int(input('enter how many numbers'))
    for i in range(0, n):
        print(i**2)

a,b,n=list(map(int,input('enter a,b,n').split()))

def week(i):
    switcher={
        0:weired_number(),
        1:add_subtract_multiply(),
        2:divide(),
        3:print_for_range()
       
    }
    return switcher.get(i,"Invalid option")

i=int(input('\n press 0 of weired_number \n press 1 for add_subtract_multiply \n press 2 for divide \n press 3 for print_for_range'))
week(i) # Call the function