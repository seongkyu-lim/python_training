
testcase = int(input())

floor_case_list = []
room_case_list = []
num_of_people = []
a = 0

for i in range(0, testcase) :

    floor = int(input())

    room = int(input())

    floor_case_list.insert(i, floor)

    room_case_list.insert(i,room)

for i in range(0, testcase) :

    if floor_case_list[i] == 0 :

        print(room_case_list[i])

    elif floor_case_list[i] == 1 :

        print(int(room_case_list[i]*(room_case_list[i]+1)/2))

    else :

        for j in range(1,floor_case_list[i]+1) :

            for k in range(0,room_case_list[i]) :

                if j == 1 :

                    num_of_people.insert(k, (k+2)*(k+1)/2)

                    print(num_of_people[k]) #test
                
                else :

                    print(num_of_people[k]) #test

                    a = a + num_of_people[k]
                    
                    num_of_people.insert(k, a)



        print(int(num_of_people[room_case_list[i]-1]))


        # else : 부분에서 J == 1 일 때 인원 수 넣어 주고 다음 반복문에서 넣어준게 다 1로 바뀜??








