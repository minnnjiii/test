# 점수계산
# 백준 2506번


n = int(input()) 
ans = [0]

scores = list(map(int,input().split())) 



for i in range(len(scores)):
    if i == 0 :
        if scores[0] == 1 : 
            ans.append(1)
    else:
        if scores[i] == 1 : 
            if scores[i-1] == 1 : 
                ans.append(ans[-1]+1) 
            else : 
                ans.append(1) 
        else: 
            ans.append(0) 

print(sum(ans))