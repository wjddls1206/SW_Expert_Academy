
TC = int(input())

for _ in range(TC):
    X, Y = map(int, input().split())

    A = (X + Y) // 2
    B = (X - Y) // 2

    print(A, B)
