answer = ''
for test in range(int(input())):

    pick_up = input()

    first_digit = pick_up[0]

    numbers_to_subtract = 0
    if len(pick_up) == 1:
        numbers_to_subtract = 9
    elif len(pick_up) == 2:
        numbers_to_subtract = 7
    elif len(pick_up) == 3:
        numbers_to_subtract = 4
    else:
        numbers_to_subtract = 0

    answer += (str((int(first_digit)*10) - numbers_to_subtract))+'\n'
print(answer,end='')

    