
for test in range(int(input())):
    digits = int(input())
    number = input()


    #there are two stage to consider
    # we divide the answer into two number , a and b.
    # a will be the biger one , b will be the smaller one.
    # first stage is before we enconter a "1"
    # if we see 2 , then split it to 1-1 for both a and b.
    # if we see 0 , then split it to 0-0 for both a and b.
    # second stage start when we first enconter a "1"
    # we then split to 1-0 , sign the 1 to a , 0 to b.
    # after that
    # everytime we enconter 2 , we split it into 0-2 , sign the 2 to b.
    # everytime we enconter 1 , we split it into 0-1 , sign the 1 to b.

    switch = 0
    a = ''
    b = ''

    for letter in number:
        if letter == '0':
            a += "0"
            b += '0'
        
        else:
            if switch == 0:
                if letter == "2":
                    a += '1'
                    b += '1'
                elif letter == '1':
                    a += '1'
                    b += '0'
                    switch = 1
            else:
                if letter == "2":
                    a += '0'
                    b += '2'
                elif letter =='1':
                    a += '0'
                    b += '1'

    print(a)
    print(b)