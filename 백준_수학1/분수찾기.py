count = int(input())

y_step = 0
x_step = 0

x = 1
y = 1

for i in range (0, count-1) :
    
    if x == 1 :

        x_step = 1
        y_step = 0

        if (x + y) % 2 == 0 :

            y = y + 1
        
        else :

            x = x + 1 
            y = y - 1

    elif y == 1 :

        y_step = 1
        x_step = 0

        if (x + y) % 2 == 1 :

            x = x + 1
        
        else :

            x = x - 1
            y = y + 1

    else : 

        if x_step == 1 :

            x = x + 1 
            y = y - 1

        elif y_step == 1 :

            x = x - 1
            y = y + 1

print(x, end='')
print('/', end='')
print(y)








    