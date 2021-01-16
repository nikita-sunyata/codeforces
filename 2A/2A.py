import sys

while 1:
    try:
        test = int(sys.stdin.readline())
        rounds_list = list()
        total_score_dict = dict()
        for i in range(test):
            data = sys.stdin.readline().strip().split(' ')
            name = data[0]
            score = int(data[1])
            if total_score_dict.get(name)==None:
                total_score_dict[name] = 0
                total_score_dict[name]+= score
            else:
                total_score_dict[name] += score
            rounds_list.append((name,score))
        #when finish all data, find the highest number
        #set the initial one
        top_score = 0
        top_people = []

        for pair in total_score_dict.items():
            if pair[1] > top_score:
                top_score = pair[1]
                #reset top_people and add the new record holder
                top_people = [pair[0]]
            elif pair[1] == top_score:
                # add that person to top_people list , we'll find who hit the score first later.
                top_people.append(pair[0])
            else:
                #else we do nothing
                pass

        if len(top_people) == 1:
            print(top_people[0])
        else:
            #we find who hit the score first
            #add a dict of the top people
            top_people_dict = dict()
            for k in top_people:
                top_people_dict[k] = 0
            #set a counter and a dict to check who hit score first
            #counter = 0#to be delete
            #who_first_dict = dict()#to be delete
            who_first_list = list()
            
            for x in rounds_list :
                #if it is not one of the top people then do nothing
                # x[0] is name , x[1] is score
                if (top_people_dict.get(x[0])==None):
                    pass
                else:
                    top_people_dict[x[0]] += x[1]
                    if (top_people_dict[x[0]]) >= top_score:
                        #who_first_dict[x[0]]=counter#to be delete
                        #counter+=1#to be delete
                        who_first_list.append(x[0])
                        break
                    else:
                        pass
            """
            #let find who is the first to hit(or hit over) the score
            first_value = ''
            for j in who_first_dict.items():
                if first_value == '':
                    first_value = (j[0],j[1])
                else:
                    if first_value[1]>j[1]:
                        first_value = (j[0],j[1])
                    else:
                        pass
            print(first_value[0])
            """
            print(who_first_list[0])
    except:
        break
