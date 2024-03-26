# 강의실 배정
# b11000.py






# 💡 알고리즘 분류
# 자료구조 
# 그리디 알고리즘
# 정렬
# 우선순위 큐

'''

# 틀린 코드 (근데 왜 틀렸는지 모르겠음 ㅜ... )
# 알고리즘 분류에 그리디 말고 우선순위 큐가 있던데 우선순위 큐 공부해야겠다. 

n = int(input()) 

lecture = [] 
for _ in range(n): 
    s, t = map(int,input().split()) 

    lecture.append((s,t)) 

lecture.sort(key=lambda x : (x[1],x[0]))

last_lecture = 0 # 마지막 강의실 사용종료 시간
count = 0 # 강의실 개수
for s, t in lecture : 
    if s >= last_lecture : 
        count += 1
        last_lecture = t

print(count)

'''
