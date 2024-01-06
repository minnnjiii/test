# 입력 받고 출력 하기

# 숫자를 입력 받을 때는 int(input())
# 문자를 입력 받을 때는 input()

# 여러가지 숫자들의 조합 = 수열
# 여러가지 문자들의 조합 = 문자열

# list(map(int,input().split()))
# list(map(str,input().split()))

listMin = list(map(int,input().split()))
listM = list(map(str,input().split()))

print(*listMin)
print(*listM)



