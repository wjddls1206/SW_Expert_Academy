
TC = int(input())

for i in range(TC):

    N = int(input())
    result = "No"

    if N > 81:
        result = "No"

    else:
        for j in range(1, 10):
            if N % j == 0 and N//j <= 9:
                result = "Yes"
                break

    print(f'#{i + 1} {result}')
