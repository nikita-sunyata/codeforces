#while 1:
#    try:
#        piles_total = input()
#        piles = [int(i)for i in input().split(" ")]
#        how_many_juicy_worms = int(input())
#        juicy_worms = [int(i)for i in input().split(" ")]
#        #answer is set to set because juicy worms might in the same group
#
#        def pile_divider(x:list):
#            first = x[0]
#            new_list = [first]
#            for i in x[1:]:
#                new_list.append( max(new_list)+i )
#            # print(new_list)
#            return new_list
#        
#        checker_list = pile_divider(piles)
#
#        current_pile = 1
#
#        new_answer_list = list()
#        for times in range(how_many_juicy_worms):
#            new_answer_list.append(0)
#
#        for times in range(sum(piles)):
#            # print('currently running :',times)
#            current_worm = times + 1
#            if current_worm > checker_list[0]:
#                current_pile += 1
#                checker_list.pop(0)
#            if current_worm in juicy_worms:
#                new_answer_list[ juicy_worms.index(current_worm) ] += current_pile
#
#        for i in new_answer_list:
#            print(i)
#    except:
#        break
#    
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
#===============================================================
#define state
#===============================================================
# def binary_search(alist:list,target:int):
#     first_index = 0
#     last_index = len(alist) - 1
#     checkpoint = False 
#     if len(alist)==0:
#         return "input list is None"
#     else:
#         first_index = 0
#         last_index = len(alist) - 1
#         while first_index <= last_index and not checkpoint:
#             middle_point = (first_index + last_index) // 2
#             if middle_point == target:

# def pile_divider(x:list):
#     first = x[0]
#     new_list = [first]
#     for i in x[1:]:
#         new_list.append( max(new_list)+i )
#     # print(new_list)
#     return new_list
    
while 1:
    try:
        piles_total = input()
        piles = [int(i)for i in input().split(" ")]
        how_many_juicy_worms = int(input())
        juicy_worms = [int(i)for i in input().split(" ")]
        # total_worms = sum(piles)


        current_pile = 0
        
        # checker_list = pile_divider(piles)
        answer_list = list()

        for i in piles:
            current_pile += 1
            for i in range(i):
                answer_list.append(current_pile)
        # print(answer_list)
        for worm in juicy_worms:
            print(answer_list[worm-1])
    except:
        break

    # new_answer_list = list()
    # for times in range(how_many_juicy_worms):
    #     new_answer_list.append(0)

    # for times in range(sum(piles)):
    #     # print('currently running :',times)
    #     current_worm = times + 1
    #     if current_worm > checker_list[0]:
    #         current_pile += 1
    #         checker_list.pop(0)
    #     if current_worm in juicy_worms:
    #         new_answer_list[ juicy_worms.index(current_worm) ] += current_pile

    # for i in new_answer_list:
    #     print(i)
    

