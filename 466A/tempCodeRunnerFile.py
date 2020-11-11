    data=input()
    n,m,a,b = data.split()
    #check if same
    if b == m * a:
        print( n * a )

    else:
        normal = n*a
        special = (n//m)*b + (n%m)*a
        if normal < special:
            print(normal)
        else:
            print(special)