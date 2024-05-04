# 평균 점수

score = 0
for i in range(5):
    tt = int(input())
    
    if tt < 40:
        tt = 40
        
    score += tt 
    
print(score // 5)