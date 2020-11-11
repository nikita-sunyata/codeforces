while True :
    try:
        data=input()
        n,m,a,b = [int(i) for i in data.split()]

        #check if same
        if b == m * a:
            print( n * a )

        else:
            normal = n*a
            special_part1 = (n//m)*b
            if (n%m) * a <= b:
                special_part2 = (n%m)*a
                special = special_part1 + special_part2
            else:
                special_part2 = b
                special = special_part1 + special_part2


            if normal < special:
                print(normal)
            else:
                print(special)

    except:
        break