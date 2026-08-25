TC = int(input())

for _ in range(TC):
    S, P = map(int, input().split())

    D = S * S - 4 * P

    # 판별식이 음수이면 해가 없음
    if D < 0:
        print("No")
        continue

    # 정수 제곱근 구하기
    left = 0
    right = S

    while left <= right:
        mid = (left + right) // 2

        if mid * mid < D:
            left = mid + 1
        elif mid * mid > D:
            right = mid - 1
        else:
            root = mid
            break
    else:
        print("No")
        continue

    # (S + root) / 2, (S - root) / 2가 정수인지 확인
    if (S + root) % 2 != 0:
        print("No")
        continue

    N = (S + root) // 2
    M = (S - root) // 2

    if N > 0 and M > 0:
        print("Yes")
    else:
        print("No")

# ======================================================
# 문제 풀이 방법의 key
# : n + m = s, n * m = p 에서 두 근의 합과 곱으로 바라보기
#
# 판별식 D가 완전 제곱수이면서 근이 자연수이어야 Yes를 출력
# 시간 복잡도를 O(log S)로 줄이기 위해
# 하나하나 계산해 비교하는 방법이 아닌 이진탐색을 사용함
# while 문이 이진탐색 부분임 !
