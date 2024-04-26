# 백준/2503번
# 숫자 야구

import sys
sys.setrecursionlimit(9999999) # 리밋 풀어주기 


# 힌트 개수 n 입력받기
n = int(input())

# n개의 줄에 질문한 세 자리 수와 스트라이크 개수, 볼의 개수 입력받기 
hint = [list(map(int,input().split())) for _ in range(n)]

# 답의 총 개수를 구하는 문제니까 답을 count할 변수 answer 만들기
answer = 0 


# 재귀함수를 만들어 만들 수 있는 모든 숫자들을 각각 비교할거임 
def recur(hint_idx,number) :
    global answer

    # 힌트 번호를 다 돌았다면
    # 영수가 준 힌트를 다 맞았다는거니까 
    # 정답 갯수 +1 증가
    if hint_idx == n:
        answer += 1
        recur(0,number+1) # 그리고 다음 숫자도 확인함 & 힌트 번호 0으로 초기화
        return
    
    
    # 문제에서 서로 다른 숫자 세 개라고 했으니까 
    # 숫자는 987까지 만들 수 있음 
    # 그 이상을 넘어가면 
    if number == 988:
        # 함수 종료
        return

    # 만약 힌트에 통과했다면
    # 스트라이크 카운트랑 볼 카운트가 동일하다면
    if checker(hint_idx,number):

        # 다음 힌트와도 동일한지 확인하기 위해 
        # 현재 힌트 번호에 +1을 해서
        # 다시 함수 호출
        recur(hint_idx+1,number) 
    # 만약 힌트에 통과하지 않았다면
    else: 
        recur(0,number+1) # 다음 숫자로 넘어감
        # 힌트 번호는 0으로 초기화



# 힌트 체크해주는 함수
def checker(hint_idx,number):
    # 힌트 숫자 세자리 가져오기
    hint_A = hint[hint_idx][0] // 100 
    hint_B = (hint[hint_idx][0] - (hint_A * 100)) // 10
    hint_C = hint[hint_idx][0] % 10
    
    # 내가 생각하는 숫자 세자리를 하나의 숫자로 가져오기 
    A = number // 100 
    B = (number - (A*100)) // 10
    C = number % 10 

    # 힌트의 strike와 ball 개수 가져오기
    hint_strike = hint[hint_idx][1]
    hint_ball = hint[hint_idx][2]
    
    # number가 조건에 일치할 때마다
    # 각각의 조건에 맞게 증가 시켜줄 strike, ball 정의하기 
    # 위의 hint_strke, ball과 비교할거임
    strike = 0
    ball = 0 

    # 서로 다른 숫자 세개니까 
    # 각각의 숫자가 동일하면 안됨 
    if A == B or B == C or A == C :
        return False
    
    # 1부터 9까지라고 했으니까 0이면 False
    if A == 0 or B == 0 or C == 0 :
        return False
    
    # 숫자, 위치까지 동일할 때
    if A == hint_A:
        strike += 1 # strke 증가
    
    # 마찬가지로 숫자, 위치까지 동일하다면
    if B == hint_B:
        strike += 1 # strke 증가
    
    if C == hint_C:
        strike += 1
    
    # 위치는 동일하지 않지만 숫자는 동일할 때 
    if A == hint_B or A == hint_C:
        ball += 1 # ball 증가

    if B == hint_A or B == hint_C:
        ball += 1

    if C == hint_A or C == hint_B:
        ball += 1

    # 위의 if문을 통해 계산된 strke와 ball의 개수가 
    # 힌트의 strke, ball 개수와 동일하다면
    if strike == hint_strike and ball == hint_ball:
        return True # 굿
    # 아니라면
    return False # ㄴㄴ
    





# 재귀함수 호출
recur(0,100) # 힌트번호 0, 세자리수 100 으로 시작

# 정답 출력
print(answer) 