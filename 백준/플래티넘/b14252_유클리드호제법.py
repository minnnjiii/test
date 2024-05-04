# 공약수열
# 백준/14252번

import sys
input = sys.stdin.readline

# 최대 공약수 구하기
def _gcd(m,n):
    if n == 0 :
        return m
    return _gcd(n,m%n)


# 입력받기
n = int(input()) 
nSet = list(map(int,input().split()))

# 리스트 정렬
nSet.sort()

# 숫자 추가 카운트
count = 0

# 인접한 두 수에 공약수 1 초과하는지 검사
for i in range(len(nSet)-1): 

    # 초과한다면(ex.7과 42)
    if _gcd(nSet[i],nSet[i+1]) != 1 : 
        # 두 수 사이에 최대 공약수 1이 되는 수가 있는지 검사 
        # 7과 42 사이에 숫자들 중 7과 최대 공약수 1이 되는 수가 있는지 검사
        for j in range(1,nSet[i+1]-nSet[i]):
            # 만약 최대 공약수 1이 되는 수가 있다면 (ex.11)
            # 7과 42 사이에 11이 있음
            if _gcd(nSet[i]+j,nSet[i+1]) == 1:
                # 그 추가된 수가 기존의 수와의 최대 공약수도 1이라면
                # 7과 11 사이에 최대 공약수는 1임 
                if _gcd(nSet[i]+j,nSet[i]) == 1:
                    # 카운트 += 1
                    count += 1 
                    break
        # 위의 조건들 중 만족하는 최대 공약수 1이 되는 수가 없다면 count +=2   
        else:
            count += 2
            
                
print(count)