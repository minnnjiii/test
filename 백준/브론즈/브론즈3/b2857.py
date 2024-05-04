# FBI
# 2857

FBI = []
for _ in range(5):
    FBI.append(input()) 

ans = []
for i in FBI:
    if 'FBI' in i : 
        ans.append(FBI.index(i)+1)
    
    
    
    
if ans == [] :
    print("HE GOT AWAY!")

else:
    print(*ans)