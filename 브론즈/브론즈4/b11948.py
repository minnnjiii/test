# 과목선택_11948

# 과학 과목
science = [] 

for i in range(4):
    science.append(int(input()))
    
# 사회 과목
society = []

for i in range(2):
    society.append(int(input()))

# 과학 과목 내림차순으로 정렬하기    
science.sort(reverse=True)
print(sum(science[0:3],max(society)))