while 1:
    try:
        data_dict = dict()
        check_dict = dict()
        for letter in input():
            if letter not in data_dict:
                data_dict[letter] = 1
            else:
                data_dict[letter] += 1
        for letter in input():
            if letter not in data_dict:
                data_dict[letter] = 1
            else:
                data_dict[letter] += 1
        for letter in input():
            if letter not in check_dict:
                check_dict[letter] = 1
            else:
                check_dict[letter] += 1
        
        if data_dict.keys()==check_dict.keys():
            answer = 'YES'
            for i in data_dict.keys():
                try:
                    if check_dict[i] == data_dict[i]:
                        continue
                    else:
                        answer = 'NO'
                        break
                except:
                    answer = 'NO'
                    break
            print(answer)
        else:
            print('NO')
    except:
        break