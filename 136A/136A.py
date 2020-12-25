while 1:
    try:
        number = int(input())
        data = [int(i) for i in input().split(' ')]

        current_i = 1
        my_dict=dict()
        for item in data:
            my_dict[item] = current_i
            current_i += 1
        answer = list()
        for times in range(number):
            times += 1
            answer.append(my_dict[times])

        print(*answer ,sep=' ')
    except:
        break