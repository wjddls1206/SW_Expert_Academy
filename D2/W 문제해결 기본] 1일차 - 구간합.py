
T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    num = list(map(int, input().split()))

    index = 0
    sum_max = 0
    sum_min = 1000000

    while index <= N - M:
        sum_num = 0

        for j in range(M):
            sum_num += num[index + j]

        if sum_num > sum_max:
            sum_max = sum_num

        if sum_num < sum_min:
            sum_min = sum_num

        index += 1

    print(f'#{i + 1} {sum_max - sum_min}')