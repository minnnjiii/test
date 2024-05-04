# 최댓값

Min_list = []

for i in range(9):
    Min_list.append(int(input()))
    
print(max(Min_list))

print(Min_list.index(max(Min_list))+1)