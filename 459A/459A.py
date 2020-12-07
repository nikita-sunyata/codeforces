# parallel is the key
# if it's not parallel , i don't yet know how to solve it

while 1:
    try:
        data = [int(i) for i in input().split()]
        # there are two point , a and b
        a_x , a_y , b_x , b_y = data

        #check if a and b is vertical or horizontal
        if a_x == b_x:
            side_len =  abs(a_y-b_y)
            #now we can add 2 more point and answer
            c_x = a_x + side_len
            c_y = a_y
            d_x = b_x + side_len
            d_y = b_y
            print(c_x,c_y,d_x,d_y)
        elif a_y == b_y:
            side_len = abs(a_x-b_x)
            c_x = a_x
            c_y = a_y + side_len
            d_x = b_x
            d_y = b_y + side_len
            print(c_x,c_y,d_x,d_y)
        else:
            #check if side_len is the same else it's flase
            if abs(a_x-b_x) == abs(a_y-b_y):
                c_x = a_x
                c_y = b_y
                d_x = b_x
                d_y = a_y
                print(c_x,c_y,d_x,d_y)
            else:
                print(-1)
    except:
        break