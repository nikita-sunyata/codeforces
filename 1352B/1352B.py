for test in range(int(input())):
    n , k = [int(i) for i in input().split(' ')]
    
    #start checking
    if n < k:
        print('NO')

    elif n%k == 0:
        print('YES')
        print(' '.join( [ str(n//k) ] * k ))

    #if the remainder % 2 == 0 , means that we can first have k  "n//k"s , then you add the remainder to the first one  
    elif (n%k) % 2 == 0:
        print('YES')
        print( '{}'.format((n//k)+(n%k)),' '.join([str(n//k)]*(k-1)) )
    
    elif(n%k) % 2 != 0:

        # so first is that we set to have k "n//k-1" (achiving the fact that we have to have k numbers)
        # then we still have to add the rest of the number ( n - ( k * ((n//k)-1) to the first number
        # of course we have to first check if the rest of the number will be able to "%2=0"
        # else the parity won't be the same
        # finally we also have to first check if ((n//k)-1) > 0 , since you need every element > 0.
        if ((((n - ((n//k)-1)*k)) % 2 ) == 0 ) and ((n//k)-1)>0 :

            print('YES')
            print(((n//k)-1)+(n-(k*((n//k)-1)))  , '{} '.format((n//k)-1)*(k-1))
        else:
            print('NO')

