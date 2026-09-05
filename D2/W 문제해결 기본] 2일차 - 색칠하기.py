
T = int(input())

for i in range(T):

    N = int(input())

    # 10 X 10 배열 만들기
    array = [[0 for col in range(10)] for row in range(10)]

    ans = 0

    # 1 : 빨강 / 2 : 파랑 / 겹치는 곳 보라 -> 3 이라 하자
    for j in range(N):

        # 왼쪽 위 모서리(r1, c1), 오른쪽 아래 모서리(r2, c2), color 입력 받기
        r1, c1, r2, c2, color = map(int, input().split())

        # array[k][l] = 0 일때 -------> color 저장 하면 됨
        # array[k][l] = 1 일때 -------> (1) color = 1 이면 그대로, (2) color = 2이면 보라색 이므로 '3' 으로 변경
        # array[k][l] = 2 일때 -------> (1) color = 1 이면 보라색 이므로 '3' 으로 변경, (2) color = 2 이면 그대로
        # array[k][l] = 3 일때 -------> 이미 보라색 이므로 변경할 필요 없음
        for k in range(r1, r2 + 1):

            for l in range(c1, c2 + 1):

                if array[k][l] == 0:
                    array[k][l] = color

                elif (array[k][l] == 1 or array[k][l] == 2) and array[k][l] != color:
                    array[k][l] = 3
                    ans += 1

    print(f'#{i + 1} {ans}')
