#세로읽기 

word = []
for i in range(5):
    word.append(input())
   
big = [] 

for i in range(5):
    big.append(len(word[i])) 

answer = ''
for i in range(0,max(big)):
    for j in range(0,5):
       if i < len(word[j]):
            answer += word[j][i]
       
print(answer)