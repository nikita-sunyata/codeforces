for test in range(int(input())):
    data = input()
    if len(data) > 10:
        number = len(data) - 2
        print(data[0]+f'{number}'+data[-1])
    else:
        print(data)
