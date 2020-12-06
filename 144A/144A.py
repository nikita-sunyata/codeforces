while 1:
    try:
        numbers = input()
        data = [int(i) for i in input().split()]
        
        #create variable
        max_by_far = data[0]
        min_by_far = data[0]
        max_location = 0
        min_location = 0
        current_index = 1
        # now data is a map object , but also iterable
        for i in data[1:]:
            #check max
            if i == max_by_far:
                #if equal , don't need to change max_location
                pass
            elif i > max_by_far:
                max_by_far = i
                max_location = current_index
            #check min
            if i == min_by_far:
                # if equal , change the min_location since it's near the end
                min_location = current_index
            elif i < min_by_far:
                min_by_far = i
                min_location = current_index


            current_index += 1
        
        max_move = max_location
        #min location is index , so it's actual place is index +1
        min_move = len(data) - (min_location+1)
        if max_location > min_location:
            # because they cross each other
            answer = (max_move + min_move) - 1
            print(answer)
            # print('type 1')
            # print("max_info :",max_by_far,max_location,max_move)
            # print('min_info :',min_by_far,min_location,min_move)
        else:
            answer = max_move + min_move
            print(answer)
            # print('type 2')
            # print("max_info :",max_by_far,max_location,max_move)
            # print('min_info :',min_by_far,min_location,min_move)
    except:
        break