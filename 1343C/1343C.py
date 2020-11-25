# for test in range(int(input())):
#     sequence_length = input()
#     sequence = [int(i) for i in input().split(" ")]

#     #check if there is only 1 element in the list
#     if len(sequence) == 1:
#         print(sequence[0])
#         continue
        

#     #sign the initial value to previous_value
#     if sequence[0] > 0:
#         previous_value = 'positive'
#     else:
#         previous_value = 'negative'

#     #setting the required variables
    
#     current_length = 1
#     max_length_so_far = 1
#     current_sum = sequence[0]
#     max_sum_so_far = sequence[0]
    
#     #start the program
#     for number in sequence[1:]:
#         #check current number is negative or positive
#         if number > 0 :
#             current_value = 'positive'
#         else:
#             current_value = 'negative'

#         #now we can check if it is consecutive
#         if previous_value == current_value:
#             #then its not consecutive
#             current_length = 1
#             current_sum = number
#             #don't need to assign previous_value again since they are the same

#             #also have to check if max_sum_so_far change
#             if current_length == max_length_so_far:
#                 max_sum_so_far = max(max_sum_so_far,current_sum)

#         else:
#             #means that its consecutive
#             previous_value = current_value

#             current_length += 1
#             current_sum += number
#             #check if pass max_length_so_far(max sum only triggers if max length change)
#             if current_length > max_length_so_far:
#                 max_length_so_far = current_length
#                 max_sum_so_far = current_sum
            
#             elif current_length == max_length_so_far:
#                 max_sum_so_far = max(max_sum_so_far,current_sum)

#             else:
#                 pass
            

#     print(max_sum_so_far)

# i think i'm right , but the test says i'm wrong
# the test is 10 numbers:
#-2 8 3 8 -4 -15 5 -2 -3 1
# the answer they give is 6 , whitch means that they think the maximum length consecutive subarray is by length 2 digits
# but if you check it with my program , you can actually see that "-15 , 5 , -2" is a 3 digits consecutive subarray
# so the answer should be -12 

#=======================================================================================================================
# so ..... I misunderstand the question
# the question is not to first find the maximum length subarry and print out the max_sum of the maximum length subarray...
# the question is to ask you to 
# first , see the entire list as an (positive-negative-positive... or negative-positive-negative...) sequence
# which means that if you encounter a positive-positive...situation (or a negative-negative... situation , you know what i mean)  
# you can pick 1 number out of all the positive-postive.. part to represtent the whole positive-positive... part
# for example -2 8 3 8 -4 -15 5 -2 -3 1
#  we see this list as a sequence of negative-positive-negative-positive-negative-positive .
# so first we only have -2 to pick , then we can pick 8 or 3 or 8 for the second part(positive) , then we can pick -4 or -15 for the thrid part ... so on
# and the goal is to maximum the sum of that sequence.
# # so finally we chose -2 , 8 , -4 , 5 , -2 , 1 . and the sum of that sequence is 6.

# for test in range(int(input())):
#     sequence_length = int(input())
#     sequence = [int(i) for i in input().split(" ")]

#     if len(sequence) == 1:
#         print(sequence[0])
#         continue

#     previous_value = 'NULL'
#     current_max_number = 'NULL'
    
#     end_index = sequence_length - 1
#     current_index = 0

#     answer_list = list()

#     for number in sequence:

#         if number > 0:
#             current_value = 'positive'
#         else:
#             current_value = 'negative'

#         if previous_value == 'NULL':
            
#             previous_value = current_value
#             current_max_number = number
#         else:
#             if current_index == end_index:
#                 if previous_value == current_value:
#                     current_max_number = max(current_max_number,number)
#                     answer_list.append(current_max_number)
#                 else:
#                     answer_list.append(current_max_number)
#                     answer_list.append(number)
#             elif previous_value == current_value:
#                 current_max_number = max(current_max_number,number)
#             else:
#                 answer_list.append(current_max_number)
#                 current_max_number=number
#                 previous_value = current_value

#         current_index += 1

#     answer = sum(answer_list)
#     print(answer)

#=========================================================================================================
#above is the right answer , but now that i think of it , i think i don't really need to create a new list
#=========================================================================================================

for test in range(int(input())):
    sequence_length = int(input())
    sequence = [int(i) for i in input().split(" ")]

    if len(sequence) == 1:
        print(sequence[0])
        continue

    previous_value = 'NULL'
    current_max_number = 'NULL'
    
    end_index = sequence_length - 1
    current_index = 0

    # answer_list = list()
    answer = 0

    for number in sequence:

        if number > 0:
            current_value = 'positive'
        else:
            current_value = 'negative'

        if previous_value == 'NULL':
            
            previous_value = current_value
            current_max_number = number
        else:
            if current_index == end_index:
                if previous_value == current_value:
                    current_max_number = max(current_max_number,number)
                    answer += current_max_number
                else:
                    answer += current_max_number
                    answer += number
            elif previous_value == current_value:
                current_max_number = max(current_max_number,number)
            else:
                answer += current_max_number
                current_max_number=number
                previous_value = current_value

        current_index += 1

    print(answer)