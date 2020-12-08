while 1:
    try:
        data = input().split(' ')
        people = int(data[0])
        requirement = int(data[1])
        values = [int(i) for i in input().split(' ')]


        qualify = 0
        requirement
        for i in values:
            if (i + requirement) <= 5:
                qualify += 1
            else:
                pass

        answer = qualify // 3

        print(answer)
        
    except:
        break