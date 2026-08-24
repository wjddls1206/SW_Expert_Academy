
T = int(input())

for i in range(T):

    num = {'9': 0, '8': 0, '7': 0, '6': 0, '5': 0, '4': 0, '3': 0, '2': 0, '1': 0, '0': 0}

    N = int(input())
    card = input()

    for j in range(N):
        num[card[j]] += 1

    max_value = max(num.values())

    print(f'#{i + 1} {max(num, key = num.get)} {max_value}')
