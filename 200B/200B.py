while 1:
    try:
        len_of_data = int(input())
        data = [int(x) for x in input().split(' ')]
        cups = len(data)
        add_up = sum(data)
        percentage = add_up/cups
        print('{:.12f}'.format(percentage))
    except:
        break
