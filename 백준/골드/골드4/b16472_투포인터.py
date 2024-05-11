# 백준/16472번
# 고냥이

import sys
input = sys.stdin.readline

N = int(input()) 
arr = list(map(str,input().strip()))

s = 0 # 시작 포인터
e = 0 # 끝 포인터

check = set(arr[0]) # 현재 부분 문자열에 포함된 문자들

ans = 0 # 최대 문자열의 길이
lenS = 1 # 현재 검사중인 부분 문자열의 길이

while s < len(arr) -1 and e < len(arr) -1:

    # 문자의 개수가 N을 초과한다면
    if len(check) > N :
        s += 1 # s를 오른쪽으로 한 칸 이동
        lenS -= 1 # 현재 부분 문자열의 길이에서 1을 뺌
        ans = max(ans,lenS) #최대 문자열 길이 ans와 비교하여 더 큰 값으로 갱신
        check = set(arr[s:e+1]) 
    else:
        e += 1 # e를 오른쪽으로 한 칸 이동
        lenS += 1 #현재 부분 문자열의 길이 1 증가
        check.add(arr[e]) #check에 새로운 문자 추가

if len(check) > N :
    ans = max(ans,lenS-1)
else:
    ans = max(ans,lenS) 
print(ans)