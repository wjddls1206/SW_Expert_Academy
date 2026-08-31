
T = int(input())

for _ in range(T):

    size_A, size_B = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    set_A = set(A)
    set_B = set(B)

    if set_A == set_B:
        print("=")

    elif set_A & set_B == set_A:
        print("<")

    elif set_A & set_B == set_B:
        print(">")

    else:
        print("?")

