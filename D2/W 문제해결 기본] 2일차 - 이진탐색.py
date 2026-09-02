
T = int(input())

for i in range(T):

    P, Pa, Pb = map(int, input().split())

    left = 1
    right = P

    # A
    count_A = 0
    count_B = 0

    while True:
        if left == right:
            count_A += 1
            break
        else:
            c = int((left + right) / 2)
            if c == Pa:
                count_A += 1
                break
            elif c < Pa:
                left = c
                count_A += 1
            else:
                right = c
                count_A += 1

    left = 1
    right = P

    # B
    while True:
        if left == right:
            count_B += 1
            break
        else:
            c = int((left + right) / 2)
            if c == Pb:
                count_B += 1
                break
            elif c < Pb:
                left = c
                count_B += 1
            else:
                right = c
                count_B += 1

    if count_A == count_B:
        ans = 0

    elif count_A < count_B:
        ans = 'A'

    else:
        ans = 'B'

    print(f'#{i + 1} {ans}')
