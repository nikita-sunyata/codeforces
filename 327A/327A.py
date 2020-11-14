while True:
    try:
        # #thought: find the longest 0s first
        # #set the origin i and j to the begining and end of the longest 0s
        # number = input()
        # letters = input().replace(" ","")
        # # print(letters)
        # try:
        #     origin_i = letters.index('0')
        # except ValueError:
        #     print(len(letters-1))
        #     #if you must move 1 time, then the answer is -1 letter
        
        # steps_to_j = 0
        #...actually i think this idea is going to have a lot of problem
        # cuz the longest 0s might ,in some conditions, not in the final result.
        # so starting from the longest 0s seems not right anymore.

        #so after searching , i think this is a " Maximum subarray " problem
        # 
        #Maximum subarray is to find the maximum out of a continuous numbers out of a one dimentional array. 

        #define a flip function
        def flip(x:list,i:int,j:int)-> list:
            # print('input_list:',x)
            index=i
            temp_list = [element for element in x]
            for times in range(i,j+1):
                temp_list[index] = 1 - temp_list[index]
                index+=1
            #print('fliped list:',temp_list)
            return temp_list
            # remember if you set "temp_list = x", you will actually change the origin data
            # so don't do that , you have to create a new list to avoid this problem


        #start the program
        number = input()
        data = [int(x) for x in input().split(" ")]
        start_index=0
        #index will be the start point , aka , "i" in this question
        #end_index will be the end point , aka , "j" in this question

        current_sum = 0
        maximum_so_far = 0
        if len(data)>1:
            for times in data[:-1]: # in this line , every element is our start point "i".
                steps_to_end_index=0
                
                for every_element_remains in data[start_index:]:
                    #print('data is :', data)
                    end_index = start_index + steps_to_end_index
                    fliped_list = flip(data,start_index,end_index)
                    current_sum = sum(fliped_list)
                    if current_sum > maximum_so_far:
                        maximum_so_far = current_sum
                    else:
                        pass
                    
                    steps_to_end_index+=1
                start_index+=1
            print(maximum_so_far)
                    
        else:
            print(1-data[0])

    except:
        break

