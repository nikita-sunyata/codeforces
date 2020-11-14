while True:
    try:
        answer = 0
        boy_number = int(input())
        boy_data = [int(i) for i in input().split()]
        boy_data.sort()
        girl_number = int(input())
        girl_data = [int(i) for i in input().split()]
        girl_data.sort()

        # print(boy_number,'\n',boy_data,'\n',girl_number,'\n',girl_data)

        for boy in boy_data:
            for girl in girl_data:
                if girl == boy-1:
                    answer+=1
                    girl_data.remove(girl)
                    break
                elif girl == boy:
                    answer+=1
                    girl_data.remove(girl)
                    break
                elif girl == boy+1:
                    answer+=1
                    girl_data.remove(girl)
                    break
                else:
                    pass
                    #still need to check other girls cuz the skill of the first boy might be too high
        
        print(answer)
    except:
        break
    #i feel stupid writing 3 statments to check if girl and boy is nearby each other .
    #turns out i can actually done it with 1 statement。
    # >>> if (abs(boy-girl <= 1)): by simply just using the abs() concept。

    
    