# OX퀴즈

n = int(input()) 

for _ in range(n) : 
    quiz = list(map(str,input()))
    score = [0]
    for i in range(len(quiz)):
        if quiz[i] == "O" : 
            if quiz[i-1] == "O" : 
                score.append(score[-1] + 1)
            else:
                score.append(1) 
        else: 
            score.append(0) 

    print(sum(score))