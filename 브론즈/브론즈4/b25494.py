# 단순한 문제(Small)
# 25494번

t = int(input()) # 테스트 케이스의 수 

for i in range(t):
    a, b, c = map(int,input().split()) # 세 정수 
    print(min(a,b,c))