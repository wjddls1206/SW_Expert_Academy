
TC = int(input())

for _ in range(TC):
    a, b, c = map(int, input().split())

    sig_a = a * (a + 1) // 2
    sig_b = b * (b + 1) // 2
    sig_c = c * (c + 1) // 2

    result = sig_a * sig_b * sig_c

    print(result % 998244353)

# ΣΣΣijk 는 ΣiΣjΣk로 나타낼 수 있음 !!!
# for문 3개로 코드 작성하면 시간복잡도 너무 큼 !
# 따라서 Σi = i * (i + 1) / 2임을 사용해 O(1)인 코드 작성