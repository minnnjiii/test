# 파티가 끝나고 난 뒤 

L, P = map(int,input().split())
peoples = list(map(int,input().split()))

people = []
for i in peoples:
    people.append(-((L * P)-i))
    
print(people[0], people[1], people[2], people[3], people[4])
