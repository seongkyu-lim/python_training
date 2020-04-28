
kg = int(input())

if kg < 5 :

    if (kg%3) == 0 :

        print(1)
    
    else :

        print(-1)

else : 

    if kg%5 == 0  :

        print (int(kg/5))

    elif  (kg%5)%3 == 0 :

        print( int((kg / 5) + 1))

    elif kg%3 == 0 :

        print (int(kg/3))

    elif (kg%3)%5 == 0 :

        print (int(kg / 3 + 1))


    