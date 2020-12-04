for test in range(int(input())):
    n , k = [int(i) for i in input().split(' ')]
    
    #start checking
    if n < k:
        print('NO')

    elif n%k == 0:
        print('YES')
        print(' '.join( [ str(n//k) ] * k ))

    elif (n%k) % 2 == 0:
        print('YES')
        print(  
            '{}'.format((n//k)+(n%k)),' '.join([str(n//k)]*(k-1)) 
            )
    
    elif(n%k) % 2 != 0:

        if ((((n - ((n//k)-1)*k)) % 2 ) == 0 ) and ((n//k)-1)>0 :

            print('YES')
            print(((n//k)-1)+(n-(k*((n//k)-1)))  , '{} '.format((n//k)-1)*(k-1))
        else:
            print('NO')

