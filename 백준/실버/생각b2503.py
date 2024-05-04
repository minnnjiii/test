# 숫자야구

n = int(input())

hint = [list(map(int,input().split())) for _ in range(4)]


answer = 0
for a in range(1,10):
    for b in range(10):
        for c in range(10): 
            
            if (a ==b or b==c or c==a): 
                continue
            
            cnt = 0
            for arr in hint:
                number = hint[0]
                ball = hint[1]
                strike = hint[2]
                
                ball_count = 0
                strike_count = 0
                
                if ball == ball_count and strike == strike_count:
                    cnt += 1
            if cnt == n:
                answer += 1
                
print(answer)
                
        