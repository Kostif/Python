try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
        print('Shit :/')

x = 5
y = 0

try:
    z = x/y
except ZeroDivisionError:
    print("can't divide by zero")

def ask():
    while True:
        int(input('Give me an integer '))
        break

ask()