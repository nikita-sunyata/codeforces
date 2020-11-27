
# for test in range(int(input())):
#     data = input().split(' ')
#     divisor = int(data[0])
#     request_index = int(data[1])
#     # print(data)
#     number = 1
#     index = 1
    
#     while index <= request_index:
#         print('current number: ',number)
#         if number % divisor != 0:
#             index+=1
#         else:
#             pass
#         number+=1

#     print(number-1)

# the solution above will definatily not pass the test
# since it's not efficient

#we can see the answer as k + x
# in which x is = to how many number can be divided by n 
answer_list = list()
for test in range(int(input())):

    data = input().split(' ')
    divisor = int(data[0])
    request_index = int(data[1])

    #answer = k + x

    #print(request_index+((request_index-1) // (divisor-1)))
    answer_list.append(request_index+((request_index-1) // (divisor-1)))
for i in answer_list:
    print(i)