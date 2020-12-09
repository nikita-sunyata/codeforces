for test in range(int(input())):
    last_player = 0
    last_clear = 0
    answer_is_wrong = 0
    for peeked in range(int(input())):
        player , clear = [int(i) for i in input().split(' ')]
        if answer_is_wrong != 1:
            if (player >= last_player ) and (clear >= last_clear) and (player >= clear):
                if (clear - last_clear)  > 0:
                    if player - (clear - last_clear) < last_player:
                        answer_is_wrong = 1
                last_player = player
                last_clear = clear
                pass
            else:
                answer_is_wrong = 1
                #can't break at this point since the program is still getting input
        else:
            pass
    if answer_is_wrong == 1:
        print('NO')
    else:
        print('YES')



