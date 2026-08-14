
test = int(input())

for t in range(test):
    N, hexa = input().split()
    N = int(N)

    result = bin(int(hexa, 16))
    result = result[2:]
    result = result.zfill(N*4)
    # zfill 함수
    # 괄호 안의 숫자만큼 zero(0)을 채워서 자릿수를 맞춰줌
    # 단, zfill 함수는 문자열(str)만 사용 가능함

    print(f'#{t + 1} {result}')
    # f-string 포매팅
    # 문자열 맨 앞에 f를 붙여주고, 중괄호 안에 직접 변수 이름이나 출력하고 싶은 것을 바로 넣으면 됨
