# 백준/20922번
# 겹치는 건 싫어

import sys
input = sys.stdin.readline

# 수열 길이 N 
# 수열에서 같은 정수 K개 
N, K = map(int,input().split()) 

# 수열 
arr = list(map(int,input().split()))

s = 0 # 시작 포인터
e = 0 # 끝 포인터

ans = 0 # 최대 문자열의 길이

# 숫자 개수를 검사할 수 있는 확인용 배열 만들기
counter = [0] * (max(arr) + 1 )

while e < N : 

    if counter[arr[e]] < K : # 현재 숫자의 개수가 k개보다 작으면
        counter[arr[e]] += 1 # 현재 숫자 추가! 
        e += 1 # 범위 확장
    else: # K개보다 큰거면
        counter[arr[s]] -= 1 # 현재 숫자 감소! 
        s += 1 # 범위 축소
    ans = max(ans, e - s) # e - s로 최대 증가 부분 수열의 길이를 갱신

print(ans)