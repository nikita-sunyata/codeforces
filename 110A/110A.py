
while 1:
    try:
        data = input()
        count = 0
        for letter in data:
            if int(letter) in (4,7):
                count += 1
        if count in (4,7):
            print('YES')
        else:
            print('NO')
    except:
        break