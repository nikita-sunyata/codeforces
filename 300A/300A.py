# while 1:
#     try:

#         data = int(input())
#         values = [int(i) for i in input().split(' ')]

#         negative_set = list()
#         positive_set = list()
#         zero_set = list()

#         # since it is guaranteed that the solution exitsts
#         # so i can just put 1 negative in the 1st set zeros in the 3rd set
#         # other can all be inside the 2nd set 
#         check_one_negative_number = 0
#         for i in values:
#             if i == 0:
#                 zero_set.append(i)
#             elif i > 0:
#                 positive_set.append(i)
#             else:
#                 if check_one_negative_number == 0:
#                     negative_set.append(i)
#                     check_one_negative_number = 1
#                 else:
#                     positive_set.append(i)
            
                
#         print(len(negative_set),str(negative_set[0]))
#         print(len(positive_set),' '.join(str(i) for i in positive_set))
#         print(len(zero_set),' '.join(str(i) for i in zero_set).strip())
#     except:
#         break

#=========================================================================
# i misunderstand the question
# set zero can put negative number in because if there is at least 1 zero in it 
# then the product of set zero must be zero
# so there are things the consider 

while 1:
    try:
        data = int(input())
        values = [int(i) for i in input().split(' ')]
            
        negative_set = list()
        positive_set = list()
        zero_set = list()
        
        # so we put every negative number in the negative set
        # if there are not enough positive number , we pop 2 of them to the positive
        # then we check if there are even number of negative numbers
        # if it's even , we pop 1 more negative number to the 3rd set
        # check_negative_number = 0
        for i in values:
            if i < 0:
                negative_set.append(i)
            elif i > 0:
                positive_set.append(i)
            else:
                zero_set.append(i)
        
        if len(positive_set) == 0:
            positive_set.append(negative_set[-1])
            positive_set.append(negative_set[-2])
            negative_set.pop()
            negative_set.pop()

        if len(negative_set) % 2 == 0:
            zero_set.append(negative_set[-1])
            negative_set.pop()
        
        print(len(negative_set),' '.join(str(i) for i in negative_set))
        print(len(positive_set),' '.join(str(i) for i in positive_set))
        print(len(zero_set),' '.join(str(i) for i in zero_set))
    except:
        break