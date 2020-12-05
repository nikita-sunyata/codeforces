# for test in range(int(input())):
#     numbers = int(input())
#     abilities = [ int(i) for i in input().split(' ')]

#     #we sort abilities list first
#     abilities.sort()

#     #create the variables we need 
#     group = 0 
#     consecutive = 1
#     previous_ability = abilities[0]


#     for ability in abilities[1:]:
        
#         #if it's not the same then we start counting how many group we add
#         if ability != previous_ability:

#             add_group = consecutive//previous_ability
#             group += add_group

#             left_number = consecutive%previous_ability
#             # 1 is for the current number
#             consecutive = 1 + left_number

#             previous_ability = ability


#         else:
#             consecutive += 1

        
#     #add the last group if there are any to add
#     group += consecutive//previous_ability

#     print(group)

##===============================================================================
# the above code worked , but i think it's the sorting make the code unefficient
# i will try to use dictionary to approch this problem
# can't pass test 22
##===============================================================================

# for test in range(int(input())):
#     numbers = int(input())
#     abilities = [ int(i) for i in input().split(' ')]

#     abilities_dict = dict()

#     if len(abilities) == 1:
#         print(1)
#     else:
#         for ability in abilities:
#             if abilities_dict.get(ability) == None:
#                 abilities_dict[ability] = 1
#             else:
#                 abilities_dict[ability] += 1
        
#         # print(abilities_dict)
#         # now we start to count
#         group = 0
#         left_number = 0
#         for current_number in sorted(abilities_dict.keys()):
#             how_many = abilities_dict[current_number]
#             how_many += left_number
#             add_group = how_many//current_number
#             group += add_group
#             #add the rest numbers to the next group if there are any
#             left_number = how_many%current_number

#         print(group)

#=================================================================
# improving , but can't pass test 26
# i'll add one check if len() of the list is greater then 1
#=================================================================
# wow , it actually worked. it's just too many 1s in test 26
# i will learn how to solve it quicker in the future of course
#=================================================================


# so after my research , there is a blog also using python
# the auther said the python "print" function actually slow the time down
# by a lot, so the auther use string+"\n"to store the answer
# and print only 1 time at the end
# let's try it with my code can see if it really matters

answer = ''
for test in range(int(input())):
    numbers = int(input())
    abilities = [ int(i) for i in input().split(' ')]

    abilities_dict = dict()



    if len(abilities) == 1:
        answer += '1\n'
    else:
        for ability in abilities:
            if abilities_dict.get(ability) == None:
                abilities_dict[ability] = 1
            else:
                abilities_dict[ability] += 1
        
        group = 0
        left_number = 0
        for current_number in sorted(abilities_dict.keys()):
            how_many = abilities_dict[current_number]
            how_many += left_number
            add_group = how_many//current_number
            group += add_group
            #add the rest numbers to the next group if there are any
            left_number = how_many%current_number
        
        answer+=str(group)+'\n'

print(answer,end='')

#===================================================================
# wow , it really matters !! 
# i went from 1950 ms (limit is 2000ms) suddently down to only 685ms
# damn , i won't forget this super useful tip
#===================================================================