
testcase = int(input())

start = 0
end = 0

start_list = []
end_list = []

for i in range(0,testcase) :

    start, end = map(int,input().split())

    start_list.insert(i, start)

    end_list.insert(i, end)
    


for i in range(0,testcase) :

    travel_distance = 0

    count = 0

    while start_list[i] < end_list[i] :

        if start_list[i] + travel_distance + 1 < end_list[i]-1 :

            start_list[i] = start_list[i] + travel_distance + 1

            travel_distance = travel_distance + 1

            count = count + 1

        elif start_list[i] + travel_distance + 1 == end_list[i]-1 :

            count = count + 1

            print(count+1)

            break

        elif start_list[i] + travel_distance + 1 > end_list[i]-1 :

            if start_list[i] + travel_distance < end_list[i]-1 :

                start_list[i] = start_list[i] + travel_distance

                count = count + 1
            
            elif start_list[i] + travel_distance == end_list[i]-1 :

                count = count + 1

                print(count+1)

                break

            elif start_list[i] + travel_distance > end_list[i]-1 :

                if start_list[i] + travel_distance - 1 < end_list[i]-1 :

                    start_list[i] = start_list[i] + travel_distance - 1

                    travel_distance  = travel_distance - 1

                    count = count + 1
                
                elif start_list[i] + travel_distance - 1 == end_list[i]-1 :

                    count = count + 1

                    print(count+1)

                    break



