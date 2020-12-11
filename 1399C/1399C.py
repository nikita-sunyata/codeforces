# not quite sure how to slove this one
# but i will try brute force it first

# for test in range(int(input())):
#     number = int(input())
#     data = [int(i) for i in input().split(' ')]
#     if len(data) == 1:
#         print('0')
#     else:
#         my_dict = dict()
#         # turn into value count list , so we can check without running through a list
#         for i in data:
#             if i not in my_dict.keys():
#                 my_dict[i] = 1
#             else:
#                 my_dict[i] += 1
        
#         max_team = 0
#         # s must > min(my_dict.keys())  and  s must < max(my_dict.keys())*2 if that key has 2 of them
#         for s in range(min(my_dict.keys())+1,(max(my_dict.keys())*2)+1):
#             current_team = 0
#             # print('start s : ', s)
#             for key in my_dict.keys():
#                 goal = s - key
#                 if goal > 1:
#                     # if s = 2 key
#                     if s == key*2:
#                         if my_dict[key] == 1:
#                             current_team += 0
#                         else:
#                             current_team += my_dict[key]//2
#                     else:
#                         try:
#                             # only check if there is a bigger value to add
#                             # since we will have already count every key increasely
#                             add =  ( min( my_dict[key] , my_dict[goal] ) )
#                             if key < goal:
#                                 current_team += add
#                             else:
#                                 pass # current_team += 0
#                         except:
#                             pass #current_team += 0
#                 else:
#                     pass # current_team += 0

#                 # print('end of key , current_team : ' , current_team)
            
#             max_team = max(current_team,max_team)

#         print(max_team)

## =======================================================================================
# there are error in the above answer , not quite sure why 
# need to check it later
## =======================================================================================
