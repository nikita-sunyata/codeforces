for test in range(int(input())):
    
    # list_len = int(input())
    # data = [int(x) for x in input().split(' ')]
    # # start_index = 0
    # # end_index = list_len # cuz [start:end],so we don't need to -1
    # # deleted = 0
    # # test_list = data[start_index:end_index]
    # # for i in data:
    # #     if max()


    # # def check(a_list):
    # #     start_index = 0
    # #     end_index = len(a_list)
    # #     for i in a_list[]

    # start = 0
    # end = list_len - 1
    # deleted = 0
    # last_pick = 'NULL'

    def initialize():
        global start
        global end
        global last_pick
        #pick the first element
        start_end_diff = data[start] - data[end]
        if start_end_diff >= 0:
            last_pick = data[start]
            start += 1
        else:
            last_pick = data[end]
            end -= 1

    def check_if_pass(a_list:list)->bool:
        '''
        check which to element to chose
        '''
        global start
        global end
        global last_pick

        for check_times in range(list_len): # actually check len - 1 times
            check_list = a_list[start:end]
            if all(last_pick >= item for item in (data[start],data[end]) ):
                pass # is ok
            else:
                return False
            #pick the next number
            start_end_diff = check_list[start] - check_list[end]
            if start_end_diff >= 0: # i guess there is no difference which we pick if equal
                last_pick = check_list[start]
                start += 1
            else:
                last_pick = check_list[end]
                end -= 1
        return True


def main():
    for test in range(int(input())):
    
        list_len = int(input())
        data = [int(x) for x in input().split(' ')]
        start = 0
        end = list_len - 1
        deleted = 0
        last_pick = 'NULL'
        initialize()

        for 




    