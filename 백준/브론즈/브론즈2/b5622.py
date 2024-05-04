# 다이얼_5622번


callWord = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
call = list(input())
callNum = 0

for i in range(len(call)):
    for j in callWord:
        if call[i] in j:
            callNum += callWord.index(j) +3 
            
    
print(callNum)