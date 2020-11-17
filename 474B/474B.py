while 1:
    try:
        piles_total = input()
        piles = [int(i)for i in input().split(" ")]
        how_many_juicy_worms = int(input())
        juicy_worms = [int(i)for i in input().split(" ")]
        #answer is set to set because juicy worms might in the same group

        def pile_divider(x:list):
            first = x[0]
            new_list = [first]
            for i in x[1:]:
                new_list.append( max(new_list)+i )
            # print(new_list)
            return new_list
        
        checker_list = pile_divider(piles)

        current_pile = 1

        new_answer_list = list()
        for times in range(how_many_juicy_worms):
            new_answer_list.append(0)

        for times in range(sum(piles)):
            # print('currently running :',times)
            current_worm = times + 1
            if current_worm > checker_list[0]:
                current_pile += 1
                checker_list.pop(0)
            if current_worm in juicy_worms:
                new_answer_list[ juicy_worms.index(current_worm) ] += current_pile

        for i in new_answer_list:
            print(i)
    except:
        break
    
    #so i believe the solve is right , but it lack efficiency
    #i'm not able to pass the #2 test's input with 4000+ piles

    #===========================================================
    # starting new approach
    #===========================================================
        # piles_total = input()
        # piles = [int(i)for i in input().split(" ")]
        # how_many_juicy_worms = int(input())
        # juicy_worms = [int(i)for i in input().split(" ")]
        # #answer is set to set because juicy worms might in the same group

        # def pile_divider(x:list):
        #     first = x[0]
        #     new_list = [first]
        #     for i in x[1:]:
        #         new_list.append( max(new_list)+i )
        #     # print(new_list)
        #     return new_list
        
        # checker_list = pile_divider(piles)
        