def print_row(*col):
    for i in range(5):
        if i in col:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

def A():
    print_row(1, 2, 3)
    print_row(0, 4)
    print_row(0, 4)
    print_row(0, 1, 2, 3, 4)
    for i in range(3):
        print_row(0, 4)

def B():
    print_row(0, 1, 2, 3)
    print_row(0, 4)
    print_row(0, 4)
    print_row(0, 1, 2, 3)
    print_row(0, 4)
    print_row(0, 4)
    print_row(0, 1, 2, 3)

def C():
    print_row(1, 2, 3)
    print_row(0, 4)
    print_row(0)
    print_row(0)
    print_row(0)
    print_row(0, 4)
    print_row(1, 2, 3)

def D():
    print_row(0, 1, 2, 3)
    for i in range(5):
        print_row(0, 4) 
    print_row(0, 1, 2, 3)

def E():
    print_row(0, 1, 2, 3, 4)
    print_row(0)
    print_row(0)
    print_row(0, 1, 2, 3, 4)
    print_row(0)
    print_row(0)
    print_row(0, 1, 2, 3, 4)

def F():
    print_row(0, 1, 2, 3, 4)
    print_row(0)
    print_row(0)
    print_row(0, 1, 2, 3, 4)
    for i in range(3):
        print_row(0)

def G():
    print_row(1, 2, 3)
    print_row(0, 4)
    print_row(0)
    print_row(0, 2, 3, 4)
    print_row(0, 4)
    print_row(0, 4)
    print_row(1, 2, 3)

def H():
    for i in range(3):
        print_row(0, 4)
    print_row(0, 1, 2, 3, 4)
    for i in range(3):
        print_row(0, 4)

def I():
    print_row(0, 1, 2, 3, 4)
    for i in range(5):
        print_row(2)
    print_row(0, 1, 2, 3, 4)

def J():
    print_row(0, 1, 2, 3, 4)
    for i in range(4):
        print_row(2)
    print_row(0, 2)
    print_row(1)

def K():
    print_row(0, 4)
    print_row(0, 3)
    print_row(0, 2)
    print_row(0, 1)
    print_row(0, 2)
    print_row(0, 3)
    print_row(0, 4)

def L():
    for i in range(6):
        print_row(0)
    print_row(0, 1, 2, 3, 4)

def M():
    print_row(0, 4)
    print_row(0, 1, 3, 4)
    print_row(0, 2, 4)
    for i in range(4):
        print_row(0, 4)

def N():
    print_row(0, 4)
    print_row(0, 4)
    print_row(0, 1, 4)
    print_row(0, 2, 4)
    print_row(0, 3, 4)
    print_row(0, 4)
    print_row(0, 4)

def O():
    print_row(1, 2, 3)
    for i in range(5):
        print_row(0, 4)
    print_row(1, 2, 3)

def P():
    print_row(0, 1, 2, 3)
    print_row(0, 4)
    print_row(0, 4)
    print_row(0, 1, 2, 3)
    for i in range(3):
        print_row(0)

def Q():
    print_row(1, 2, 3)
    for i in range(3):
        print_row(0, 4)
    print_row(0, 2, 4)
    print_row(0, 3, 4)
    print_row(1, 2, 3, 4)

def R():
    print_row(0, 1, 2, 3)
    print_row(0, 4)
    print_row(0, 4)
    print_row(0, 1, 2, 3)
    print_row(0, 2)
    print_row(0, 3)
    print_row(0, 4)

def S():
    print_row(1, 2, 3)
    print_row(0, 4)
    print_row(0)
    print_row(1, 2, 3)
    print_row(4)
    print_row(0, 4)
    print_row(1, 2, 3)

def T():
    print_row(0, 1, 2, 3, 4)
    for i in range(7):
        print_row(2)

def U():
    for i in range(6):
        print_row(0, 4)
    print_row(1, 2, 3)

def V():
    for i in range(5):
        print_row(0, 4)
    print_row(1, 3)
    print_row(2)

def W():
    for i in range(4):
        print_row(0, 4)
    print_row(0, 2, 4)
    print_row(0, 1, 3, 4)
    print_row(0, 4)

def X():
    print_row(0, 4)
    print_row(0, 4)
    print_row(1, 3)
    print_row(2)
    print_row(1, 3)
    print_row(0, 4)
    print_row(0, 4)

def Y():
    print_row(0, 4)
    print_row(0, 4)
    print_row(1, 2, 3)
    for i in range(4):
        print_row(2)

def Z():
    print_row(0, 1, 2, 3, 4)
    print_row(4)
    print_row(3)
    print_row(2)
    print_row(1)
    print_row(0)
    print_row(0, 1, 2, 3, 4)

# Input to print any word vertically
word = input('Enter Any Word To Print Vertically: ').upper()
for ch in word:
    if ch in globals():
        exec(ch + '()')
        print()  
    else:
        print(f"Function for '{ch}' is not defined!")