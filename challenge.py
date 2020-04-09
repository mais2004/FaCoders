print("                       Numbers from 1 to 10                       ")

x = int(input('Guess the number : '))
y = 7
while x != y:
    x = int(input('Guess the number :'))
       
if x == y:
    print('Great! you did it!')
