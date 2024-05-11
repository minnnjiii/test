# 재활용 캠페인
# 백준/22988번
# 투 포인터

import sys
input = sys.stdin.readline


# 히나가 가진 헤어에센스 용기의 수 N 
# 헤어에센스 용기의 총 용량 X
N, X = map(int,input().split()) 

# 용기에 담겨 있는 헤어에센스의 용량들 
arr = sorted(list(map(int,input().split())))

# 왼쪽 포인터
s = 0 

# 오른쪽 포인터
e = N - 1

remain = 0 # 짜투리
cnt = 0 # 용기를 몇 개 만들 수 있는지 확인하는 count



while s <= e : # 포인터가 교차하면 while문 멈춤

    if arr[e] == X : # 용기의 용량 X와 남아있는 용량 arr 이 똑같다면
        cnt += 1 # 카운트 추가
        e -= 1 # 오른쪽 카운터 왼쪽으로 한칸 이동
        continue # 계속 

    if s == e : # 두 포인터들이 만났다면
        remain += 1 # 짜투리 하나 추가
        break # while문 나오기!
    
    if arr[e] + arr[s] >= X/2 : #왼쪽 카운터에 해당하는 용량과 오른쪽 카운터에 해당하는 용량의 합이 (용량/2)보다 크거나 같다면
        cnt += 1 # 카운트 추가
        s += 1 # 왼쪽 카운터 오른쪽으로 한 칸 이동
        e -= 1 # 오른쪽 카운터 왼쪽으로 한 칸 이동
    else: # 그게 아니라면
        s += 1 # 왼쪽 카운터만 오른쪽으로 한 칸 이동하고
        remain += 1 # 짜투리 추가

# 짜투리가 3개 있으면 용량 하나가 만들어지니까 
# remain//3 값과 카운트 값을 더해 
print(cnt + remain//3) 