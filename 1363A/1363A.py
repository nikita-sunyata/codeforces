
# answer_list = list()
# for times in range(int(input())):
#     requirements = input().split(' ')
#     array_a = [False for i in input().split(' ') if int(i)%2 != 0 ]
#     length = int(requirements[0])
#     pick = int(requirements[1])

#     odd = len(array_a)
#     even = length - odd

#     # you need at least 1 odd number
#     # then the rest of the odd number ,
#     # i can use 2 odd number transform into a even number
#     if odd == 0:
#         # print("No")
#         answer_list.append("No")
#     else:
#         #we pick one odd number already
#         pick = pick - 1
#         if even - pick >= 0:
#             answer_list.append('Yes')
#         else:
#             #if not enough , then transform 2 odd into 1 even
#             #but also remember that means you pick two numbers
#             odd  = odd-1 # as you already pick one earlier
#             #if there is only 1 pick left
#             # there is no way you can pick an even number which is transformed by two odd nubmers
#             # the int() transform float number by just dropping the decimal part
#             #print('pick : ',pick , 'even : ',even , 'odd : ', odd)
#             left_to_pick = int( (pick - even) / 2)
#             #print('left to pick : ',left_to_pick)
#             transformed_even_left = int(odd // 2)
#             #print('transformed_even_left : ',transformed_even_left)
#             if left_to_pick == 0:
#                 answer_list.append('No')

#             elif left_to_pick >= transformed_even_left:
#                 answer_list.append('Yes')
#             else:
#                 answer_list.append('No')




# for i in answer_list:
#     print(i)

#==========================================================================
#the above have some problems 



answer_list = list()
for times in range(int(input())):
    requirements = input().split(' ')
    array_a = [False for i in input().split(' ') if int(i)%2 != 0 ]
    length = int(requirements[0])
    pick = int(requirements[1])

    odd = len(array_a)
    even = length - odd

    # you need at least 1 odd number
    if odd == 0:
        # print("No")
        answer_list.append("No")
    else:
        #check is to check if we triggered Yes this round
        check = 0
        # we iterate every odd numbers we can chose in the situation
        # we can chose 1,3,5...odd numbers to make the final result a odd number
        for odd_number in range(1,odd+1,2):
            #this is to count how many more we need to pick
            left_to_pick = pick-odd_number
            #so if there is more even numbers we have than we need to pick , for sure we can make the final number a odd number
            #remember , all the numbers we iterate , their sum will always be a odd number , so if left_to_pick is zero , you also achive the requirment
            if ( left_to_pick <= even )and (left_to_pick >= 0):
                answer_list.append("Yes")
                check = 1
                break
        #this is to check if we triggered Yes within those possible choses
        #if none of that triggers Yes , then it means there is no way we can make it a odd number
        if check != 1:
            answer_list.append("No")
        else:
            check = 0
for i in answer_list:
        print(i)
