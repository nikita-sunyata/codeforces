while 1:
    try:
        data1 = [ int(i) for i in input().split(' ')]
        how_many_data = data1[0]
        coach_time = data1[1]
        max_joy = 'Null'
        for times in range(how_many_data):
            data2 = [int(i) for i in input().split(' ')]
            restaurant_joy = data2[0]
            restaurant_time = data2[1]
            time_diff = restaurant_time - coach_time

            if time_diff > 0:
                current_joy = restaurant_joy - time_diff
            else:
                current_joy = restaurant_joy
            
            if max_joy == 'Null':
                max_joy = current_joy
            else:
                max_joy = max(max_joy,current_joy)
        print(max_joy)
    except:
        break
    