# the gaol is to not write a recursive algroithem

#dynamic programming ?


# i will use a1 as key , and arrey to value
# my_dict = dict()

# for i in  range(int(input())):
#     a1 , k = [int(i) for i in input().split(' ')]

#     #check if already exist 
#     # if already exist , check if there is already answer in it
#     # if not , start computing from the last element 
#     # also will continuously  append element to the key list along the way 
#     if a1 in  my_dict.keys():
#         # if there is already answer , print it out 
#         if k <= len(my_dict[a1]):
#             print(my_dict[a1][k-1])
#         # else i will start from the last part to solve it
#         else:
#             current_max = int(max(list(str( my_dict[a1][-1] ))))
#             current_mix = int(min(list(str( my_dict[a1][-1] ))))
#             last_element_index = my_dict[a1].index(my_dict[a1][-1])
#             for times in range(k - len(my_dict[a1])):
#                 new_element = my_dict[a1][last_element_index] + (current_max * current_mix)
#                 my_dict[a1].append(new_element)

#                 last_element_index += 1
#                 current_max = int(max(list(str(new_element))))
#                 current_mix = int(min(list(str(new_element))))
#             print(my_dict[a1][-1])

#     # else i will add it to the list and start computing
#     # and will continuously append element to the key list along the way
#     else:
#         # put the first element in
#         my_dict[a1]  = [a1]
#         current_max = int(max(list(str(a1))))
#         current_mix = int(min(list(str(a1))))
#         last_element_index = 0
#         for times in range(k-1):
#             new_element = my_dict[a1][last_element_index] + (current_max * current_mix)
#             my_dict[a1].append(new_element)

#             last_element_index += 1
#             current_max = int(max(list(str(new_element))))
#             current_mix = int(min(list(str(new_element))))

#         print(my_dict[a1][-1])
#         # print(my_dict)
#         # print(my_dict[a1].index(my_dict[a1][-1]))

# ========================================================================================
### I'm quite happy about my program , even though it didn't pass the test
# I hit the time limit , there is  one test data "871634532970971855 2257402923097884"
# that is just too many to compute , even with my algorithm.
# that means this question must have an math explaination that can easily know the answer
# =========================================================================================

# after research , there is a trick in the question 
# while computuing , at some point there is going to be zero in the max()*min() part
# and after that part happended , after that the number will always maintain the same
# so it's easy for me to just add a  check if last_element is zero 
# if it is zero , then i will simply just return list[-2] (since list[-1] is zero)

# =========================================================================================


my_dict = dict()

for i in  range(int(input())):
    a1 , k = [int(i) for i in input().split(' ')]

    #check if already exist 
    # if already exist , check if there is already answer in it
    # if not , start computing from the last element 
    # also will continuously  append element to the key list along the way 
    if a1 in  my_dict.keys():
        # if there is already answer , print it out 
        if k <= len(my_dict[a1]):
            print(my_dict[a1][k-1])
        # else i will start from the last part to solve it
        else:
            current_max = int(max(list(str( my_dict[a1][-1] ))))
            current_mix = int(min(list(str( my_dict[a1][-1] ))))
            last_element_index = my_dict[a1].index(my_dict[a1][-1])
            for times in range(k - len(my_dict[a1])):

                new_element = my_dict[a1][last_element_index] + (current_max * current_mix)
                my_dict[a1].append(new_element)

                last_element_index += 1
                current_max = int(max(list(str(new_element))))
                current_mix = int(min(list(str(new_element))))

                if my_dict[a1][-2] == my_dict[a1][-1]:
                    break


            if my_dict[a1][-1] == my_dict[a1][-2]:
                print(my_dict[a1][-2])
            else:
                print(my_dict[a1][-1])

    # else i will add it to the list and start computing
    # and will continuously append element to the key list along the way
    else:
        # put the first element in
        my_dict[a1]  = [a1]
        current_max = int(max(list(str(a1))))
        current_mix = int(min(list(str(a1))))
        last_element_index = 0
        if k == 1:
            print(a1)
        else:

            for times in range(k-1):

                new_element = my_dict[a1][last_element_index] + (current_max * current_mix)
                my_dict[a1].append(new_element)
        
                
                last_element_index += 1
                current_max = int(max(list(str(new_element))))
                current_mix = int(min(list(str(new_element))))

                if my_dict[a1][-2] == my_dict[a1][-1]:
                    break

            if my_dict[a1][-1] == my_dict[a1][-2]:
                print(my_dict[a1][-2])
            else:
                print(my_dict[a1][-1])
            # print(my_dict)
            # print(my_dict[a1].index(my_dict[a1][-1]))