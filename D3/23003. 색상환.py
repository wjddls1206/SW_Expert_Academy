
TC = int(input())

color = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
#          0        1       2        3         4        5
for _ in range(TC):

    S, T = map(str, input().split())

    if S == T:
        ans = 'E'

    elif abs(color.index(S) - color.index(T)) == 1 or abs(color.index(S) - color.index(T)) == 5:
        ans = 'A'

    elif abs(color.index(S) - color.index(T)) == 3:
        ans = 'C'

    else:
        ans = 'X'

    print(f'{ans}')
