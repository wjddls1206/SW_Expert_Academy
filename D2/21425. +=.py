TC = int(input())

for _ in range(TC):
    A, B, N = map(int, input().split())

    result = 0

    while A <= N and B <= N:
        if A < B:
            A += B
        else:
            B += A

        result += 1

    print(result)

# while문 안의 조건문 : 왜 작은 값에 큰 값을 더하나?
# A = 3, B = 5 일 때,
# A += B = 8  --------> (8, 5)
# B += A = 8  --------> (3, 8)
# 둘 다 한 번의 연산 후에는 큰 값이 8이지만,
# 빠르게 N을 초과해야하기 때문에 작은 값에 큰 값을 더해 그 값으로 대체함으로써
# 작은 값을 담고있는 변수를 빨리 키워나가기 위해 작은 값에 큰 값을 더한다 !
